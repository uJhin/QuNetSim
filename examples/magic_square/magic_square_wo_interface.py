import numpy as np
import random
from tkinter import *
from tkinter import messagebox
from components.host import Host
from components.network import Network
from objects.qubit import Qubit
from objects.logger import Logger
from backends.projectq_backend import ProjectQBackend
# from backends.eqsn_backend import EQSNBackend
from backends.cqc_backend import CQCBackend

Logger.DISABLED = False
WAIT_TIME = 15
global turn
global flag
global res_row
global res_col


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
    global res_row
    epr_id, _ = host.send_epr(other_player, await_ack=True)
    epr_id2, _ = host.send_epr(other_player, await_ack=True)
    qa = host.get_epr(other_player, epr_id)
    qc = host.get_epr(other_player, epr_id2)
    row = int(host.get_classical(jury)[0].content)

    N = 3
    M = 3

    res_row = [[0 for i in range(N)] for j in range(M)]

    if row == 0:
        res_row[0][0] = parity_meas([qa, qc], "IZ", host, True)
        res_row[0][1] = parity_meas([qa, qc], "ZI", host, True)
        res_row[0][2] = parity_meas([qa, qc], "ZZ", host)

    if row == 1:
        res_row[1][0] = parity_meas([qa, qc], "XI", host, True)
        res_row[1][1] = parity_meas([qa, qc], "IX", host, True)
        res_row[1][2] = parity_meas([qa, qc], "XX", host)

    if row == 2:
        res_row[2][0] = parity_meas([qa, qc], "XZ", host, True)
        res_row[2][1] = parity_meas([qa, qc], "ZX", host, True)
        res_row[2][2] = parity_meas([qa, qc], "YY", host)

    print('ROW:' + str(row) + ',', res_row[row][0], res_row[row][1], res_row[row][2])
    print(res_row)

    host.send_classical(jury, str(res_row[row][0]) + str(res_row[row][1]) + str(res_row[row][2]))

    return


def player_2(host, other_player, jury):
    global res_col
    qb = host.get_epr(other_player, wait=WAIT_TIME)
    qd = host.get_epr(other_player, wait=WAIT_TIME)
    col = int(host.get_classical(jury, wait=WAIT_TIME)[0].content)

    N = 3
    M = 3

    res_col = [[0 for i in range(N)] for j in range(M)]

    if col == 0:
        res_col[0][0] = parity_meas([qb, qd], "IZ", host, True)
        res_col[0][1] = parity_meas([qb, qd], "XI", host, True)
        res_col[0][2] = parity_meas([qb, qd], "XZ", host, True)

    if col == 1:
        res_col[1][0] = parity_meas([qb, qd], "ZI", host, True)
        res_col[1][1] = parity_meas([qb, qd], "IX", host, True)
        res_col[1][2] = parity_meas([qb, qd], "ZX", host, True)

    if col == 2:
        res_col[2][0] = parity_meas([qb, qd], "ZZ", host)
        res_col[2][1] = parity_meas([qb, qd], "XX", host)
        res_col[2][2] = parity_meas([qb, qd], "YY", host)

    print('COL:' + str(col) + ',', res_col[col][0], res_col[col][1], res_col[col][2])
    print(res_col)

    host.send_classical(jury, str(res_col[col][0])+str(res_col[col][1])+str(res_col[col][2]))
    return


def judge(host, first_player, second_player):
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    host.send_classical(first_player, str(row), True)
    host.send_classical(second_player, str(col), True)

    pl1_row = host.get_classical(first_player, wait=WAIT_TIME)[0].content
    pl2_col = host.get_classical(second_player, wait=WAIT_TIME)[0].content

    print(pl1_row)
    print(pl2_col)

    win_flag = True
    if (int(pl1_row[0])+int(pl1_row[1])+int(pl1_row[2])) % 2 != 0:
        win_flag = False

    if (int(pl2_col[0])+int(pl2_col[1])+int(pl2_col[2])) % 2 != 1:
        win_flag = False

    if int(pl1_row[col]) != int(pl2_col[row]):
        win_flag = False

    if win_flag is False:
        print('ROUND LOST')

    if win_flag is True:
        print('ROUND WON')


    return


def main():
    global turn
    global flag
    global res_row
    global res_col
    # Initialize a network
    network = Network.get_instance()
    backend = CQCBackend()
    # Define the host IDs in the network
    nodes = ['Alice', 'Bob', 'Eve']

    network.delay = 0

    # Start the network with the defined hosts
    network.start(nodes, backend)

    # Initialize the host Alice
    host_alice = Host('Alice', backend)

    # Add a one-way connection (classical and quantum) to Bob
    host_alice.add_connection('Bob')
    host_alice.delay = 0

    # Start listening
    host_alice.start()

    host_bob = Host('Bob', backend)
    # Bob adds his own one-way connection to Alice and Eve
    host_bob.add_connection('Alice')
    host_bob.add_connection('Eve')
    host_bob.delay = 0
    host_bob.start()

    host_eve = Host('Eve', backend)
    host_eve.add_connection('Bob')
    host_eve.delay = 0
    host_eve.start()

    # Add the hosts to the network
    # The network is: Alice <--> Bob <--> Eve
    network.add_host(host_alice)
    network.add_host(host_bob)
    network.add_host(host_eve)

    host_alice.run_protocol(player_1, (host_bob.host_id, host_eve.host_id))
    host_bob.run_protocol(player_2, (host_alice.host_id, host_eve.host_id))
    host_eve.run_protocol(judge, (host_alice.host_id, host_bob.host_id))

    # t1 = host_alice.run_protocol(alice_func, ())
    # t2 = host_eve.run_protocol(eve_func, ())

    # t1.join()
    # t2.join()

if __name__ == '__main__':
    main()
