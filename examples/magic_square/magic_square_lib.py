import numpy as np
import random

from components.host import Host
from components.network import Network
from objects.qubit import Qubit
from objects.logger import Logger
# from backends.projectq_backend import ProjectQBackend
# from backends.eqsn_backend import EQSNBackend
from backends.cqc_backend import CQCBackend

Logger.DISABLED = True
WAIT_TIME = 10
global thread_1_return
global thread_2_return
thread_1_return = None
thread_2_return = None
global row
global col
row = 0
col = 0


def parity_meas(qubits, bases, node, negative=False):
    """
    Performs a parity measurement on the provided qubits in the Pauli bases specified by 'bases'.
    'bases' should be a string with letters in "IXYZ" and have the same length as the number of qubits provided.
    If 'negative' is true the measurement outcome is flipped.
    If more than one letter of 'bases' is not identity, then an ancilla qubit will be used, which is created using the
    provided 'node'.

    :param qubits: List of qubits to be measured.
    :type qubits: list of :obj: `cqc.pythonLib.qubit`
    :param bases: String specifying the Pauli-bases of the measurement. Example bases="IXY" for three qubits.
    :type bases: str
    :param node: The node storing the qubits. Used for creating an ancilla qubit.
    :type node: :obj: `cqc.pythonLib.CQCConnection`
    :param negative: If the measurement outcome should be flipped or not.
    :type negative: bool
    :return: The measurement outcome 0 or 1, where 0 correspond to the +1 eigenvalue of the measurement operator.
    """

    if not (len(qubits) == len(bases)):
        raise ValueError("Number of bases needs to be the number of qubits.")
    if not all([(B in "IXYZ") for B in bases]):
        raise ValueError("All elements of bases need to be in 'IXYZ'.")

    num_qubits = len(qubits)

    flip_basis = ["I"] * num_qubits
    non_identity_bases = []

    # Check if we need to flip the bases of the qubits
    for i in range(len(bases)):
        B = bases[i]
        if B == "X":
            flip_basis[i] = "H"
            non_identity_bases.append(i)
        elif B == "Y":
            flip_basis[i] = "K"
            non_identity_bases.append(i)
        elif B == "Z":
            non_identity_bases.append(i)
        else:
            pass

    if len(non_identity_bases) == 0:
        # Trivial measurement
        m = 0

    elif len(non_identity_bases) == 1:
        # Single_qubit measurement
        q_index = non_identity_bases[0]
        q = qubits[q_index]

        # Flip to correct basis
        if flip_basis[q_index] == "H":
            q.H()
        if flip_basis[q_index] == "K":
            q.K()

        m = q.measure(non_destructive=True)

        # Flip the qubit back
        if flip_basis[q_index] == "H":
            q.H()
        if flip_basis[q_index] == "K":
            q.K()

    else:
        # Parity measurement, ancilla needed

        # Initialize ancilla qubit
        anc = Qubit(node)

        # Flip to correct basis
        for i in range(len(bases)):
            if flip_basis[i] == "H":
                qubits[i].H()
            if flip_basis[i] == "K":
                qubits[i].K()

                # Transfer parity information to ancilla qubit
        for i in non_identity_bases:
            qubits[i].cnot(anc)

            # Measure ancilla qubit
        m = anc.measure(non_destructive=True)

        # Flip to correct basis
        for i in range(len(bases)):
            if flip_basis[i] == "H":
                qubits[i].H()
            if flip_basis[i] == "K":
                qubits[i].K()

    if negative:
        return (m + 1) % 2
    else:
        return m


def player_1(host, other_player, jury):
    global thread_1_return
    epr_id, _ = host.send_epr(other_player, await_ack=True)
    epr_id2, _ = host.send_epr(other_player, await_ack=True)
    qa = host.get_epr(other_player, epr_id)
    # print('Alice1: ' + qa.id)
    qc = host.get_epr(other_player, epr_id2)
    # print('Alice2: ' + qc.id)
    row = int(host.get_classical(jury)[0].content)

    if row == 0:
        m_0 = parity_meas([qa, qc], "IZ", host, True)
        m_1 = parity_meas([qa, qc], "ZI", host, True)
        m_2 = parity_meas([qa, qc], "ZZ", host)

    if row == 1:
        m_0 = parity_meas([qa, qc], "XI", host, True)
        m_1 = parity_meas([qa, qc], "IX", host, True)
        m_2 = parity_meas([qa, qc], "XX", host)

    if row == 2:
        m_0 = parity_meas([qa, qc], "XZ", host, True)
        m_1 = parity_meas([qa, qc], "ZX", host, True)
        m_2 = parity_meas([qa, qc], "YY", host)

    # if row == 0:
    #     m_0 = parity_meas([qa, qc], "XI", host)
    #     m_1 = parity_meas([qa, qc], "XX", host)
    #     m_2 = parity_meas([qa, qc], "IX", host)
    #
    # if row == 1:
    #     m_0 = parity_meas([qa, qc], "XZ", host, True)
    #     m_1 = parity_meas([qa, qc], "YY", host)
    #     m_2 = parity_meas([qa, qc], "ZX", host, True)
    #
    # if row == 2:
    #     m_0 = parity_meas([qa, qc], "IX", host)
    #     m_1 = parity_meas([qa, qc], "ZZ", host)
    #     m_2 = parity_meas([qa, qc], "ZI", host)

    print('ROW:' + str(row) + ',', m_0, m_1, m_2)

    thread_1_return = [m_0, m_1, m_2]
    return


def player_2(host, other_player, jury):
    global thread_2_return
    qb = host.get_epr(other_player, wait=WAIT_TIME)
    # print('Bob1: ' + qb.id)
    qd = host.get_epr(other_player, wait=WAIT_TIME)
    # print('Bob2: ' + qd.id)
    col = int(host.get_classical(jury, wait=WAIT_TIME)[0].content)
    # print('COL')
    # print(col)

    if col == 0:
        m_0 = parity_meas([qb, qd], "IZ", host, True)
        m_1 = parity_meas([qb, qd], "XI", host, True)
        m_2 = parity_meas([qb, qd], "XZ", host, True)

    if col == 1:
        m_0 = parity_meas([qb, qd], "ZI", host, True)
        m_1 = parity_meas([qb, qd], "IX", host, True)
        m_2 = parity_meas([qb, qd], "ZX", host, True)

    if col == 2:
        m_0 = parity_meas([qb, qd], "ZZ", host)
        m_1 = parity_meas([qb, qd], "XX", host)
        m_2 = parity_meas([qb, qd], "YY", host)

    # if col == 0:
    #     m_0 = parity_meas([qb, qd], "XI", host)
    #     m_1 = parity_meas([qb, qd], "XZ", host, True)
    #     m_2 = parity_meas([qb, qd], "IX", host)
    #
    # if col == 1:
    #     m_0 = parity_meas([qb, qd], "XX", host)
    #     m_1 = parity_meas([qb, qd], "YY", host)
    #     m_2 = parity_meas([qb, qd], "ZZ", host)
    #
    # if col == 2:
    #     m_0 = parity_meas([qb, qd], "IX", host)
    #     m_1 = parity_meas([qb, qd], "ZX", host, True)
    #     m_2 = parity_meas([qb, qd], "ZI", host)

    print('COL:' + str(col) + ',', m_0, m_1, m_2)

    thread_2_return = [m_0, m_1, m_2]
    return


def judge(host, first_player, second_player, row, col):
    # row = random.randint(0, 2)
    # col = random.randint(0, 2)
    host.send_classical(first_player, str(row), True)
    host.send_classical(second_player, str(col), True)

    return


# def judge_row(host, first_player, row):
#     host.send_classical(first_player, str(row), True)
#
#     return
#
# def judge_row(host, first_player, row):
#     host.send_classical(first_player, str(row), True)
#
#     return


def process():
    global thread_1_return
    global thread_2_return
    global row
    global col
    # Initialize a network
    network = Network.get_instance()
    #backend = CQCBackend()
    # Define the host IDs in the network
    nodes = ['Alice', 'Bob', 'Eve']

    network.delay = 0

    # Start the network with the defined hosts
    network.start(nodes)

    # Initialize the host Alice
    host_alice = Host('Alice')

    # Add a one-way connection (classical and quantum) to Bob
    host_alice.add_connection('Bob')
    host_alice.delay = 0

    # Start listening
    host_alice.start()

    host_bob = Host('Bob')
    # Bob adds his own one-way connection to Alice and Eve
    host_bob.add_connection('Alice')
    host_bob.add_connection('Eve')
    host_bob.delay = 0
    host_bob.start()

    host_eve = Host('Eve')
    host_eve.add_connection('Bob')
    host_eve.delay = 0
    host_eve.start()

    # Add the hosts to the network
    # The network is: Alice <--> Bob <--> Eve
    network.add_host(host_alice)
    network.add_host(host_bob)
    network.add_host(host_eve)

    # def process(row, col):
    #     host_alice.run_protocol(player_1, (host_bob.host_id, host_eve.host_id))
    #     host_bob.run_protocol(player_2, (host_alice.host_id, host_eve.host_id))
    #     host_eve.run_protocol(judge, (host_alice.host_id, host_bob.host_id, row, col))
    #     return thread_1_return,thread_2_return

    row = 1
    col = 1

    host_alice.run_protocol(player_1, (host_bob.host_id, host_eve.host_id))
    host_bob.run_protocol(player_2, (host_alice.host_id, host_eve.host_id))
    host_eve.run_protocol(judge, (host_alice.host_id, host_bob.host_id, row, col))

    # process(1,1)

    # t1 = host_alice.run_protocol(alice_func, ())
    # t2 = host_eve.run_protocol(eve_func, ())

    # t1.join()
    # t2.join()

    return thread_1_return, thread_2_return


# def main():
#     global thread_1_return
#     global thread_2_return
#     global row
#     global col
#     # Initialize a network
#     network = Network.get_instance()
#     # backend = CQCBackend()
#     # Define the host IDs in the network
#     nodes = ['Alice', 'Bob', 'Eve']
#
#     network.delay = 0
#
#     # Start the network with the defined hosts
#     network.start(nodes)
#
#     # Initialize the host Alice
#     host_alice = Host('Alice')
#
#     # Add a one-way connection (classical and quantum) to Bob
#     host_alice.add_connection('Bob')
#     host_alice.delay = 0
#
#     # Start listening
#     host_alice.start()
#
#     host_bob = Host('Bob')
#     # Bob adds his own one-way connection to Alice and Eve
#     host_bob.add_connection('Alice')
#     host_bob.add_connection('Eve')
#     host_bob.delay = 0
#     host_bob.start()
#
#     host_eve = Host('Eve')
#     host_eve.add_connection('Bob')
#     host_eve.delay = 0
#     host_eve.start()
#
#     # Add the hosts to the network
#     # The network is: Alice <--> Bob <--> Eve
#     network.add_host(host_alice)
#     network.add_host(host_bob)
#     network.add_host(host_eve)
#
#     # def process(row, col):
#     #     host_alice.run_protocol(player_1, (host_bob.host_id, host_eve.host_id))
#     #     host_bob.run_protocol(player_2, (host_alice.host_id, host_eve.host_id))
#     #     host_eve.run_protocol(judge, (host_alice.host_id, host_bob.host_id, row, col))
#     #     return thread_1_return,thread_2_return
#
#     host_alice.run_protocol(player_1, (host_bob.host_id, host_eve.host_id))
#     host_bob.run_protocol(player_2, (host_alice.host_id, host_eve.host_id))
#     host_eve.run_protocol(judge, (host_alice.host_id, host_bob.host_id, row, col))
#
#     # process(1,1)
#
#     # t1 = host_alice.run_protocol(alice_func, ())
#     # t2 = host_eve.run_protocol(eve_func, ())
#
#     # t1.join()
#     # t2.join()
#
#     return thread_1_return


# if __name__ == '__main__':
#     freeze_support()
#     main()
