from components.host import Host
from components.network import Network
from objects.qubit import Qubit
from objects.logger import Logger
from backends.projectq_backend import ProjectQBackend
from backends.cqc_backend import CQCBackend


Logger.DISABLED = True


def parity_meas(qubits, bases, node, negative=False):

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

        m = q.measure(True)

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
        m = anc.measure()

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


def sniff(sender, receiver, qubit):
    print('did')
    qubit.measure(True)


def main():
   try:
      network = Network.get_instance()
      nodes = ['A', 'B']

      backend = CQCBackend()

      network.start(nodes, backend)
      network.delay = 0.1

      host_A = Host('A', backend)
      host_A.add_connections(['B'])
      host_A.start()

      host_B = Host('B', backend)
      host_B.add_connections(['A'])
      host_B.start()

      network.add_host(host_A)
      network.add_host(host_B)

      q_a_id, _ = host_A.send_epr('B', await_ack=True)
      q_c_id, _ = host_A.send_epr('B', await_ack=True)

      q_a = host_A.get_epr('B', q_a_id)
      q_c = host_A.get_epr('B', q_c_id)

      q_b = host_B.get_epr('A', wait=5)
      q_d = host_B.get_epr('A', wait=5)

      # row 3
      r0 = parity_meas([q_a, q_c], 'IX', host_A)
      r1 = parity_meas([q_a, q_c], 'ZZ', host_A)
      r2 = parity_meas([q_a, q_c], 'ZI', host_A)

      # col 2
      c0 = parity_meas([q_b, q_d], 'XX', host_B)
      c1 = parity_meas([q_b, q_d], 'YY', host_B)
      c2 = parity_meas([q_b, q_d], 'ZZ', host_B)

      print('row', r0, r1, r2)
      print('col', c0, c1, c2)


      network.stop(True)
   except Exception as e:
      print(e)

if __name__ == '__main__':
    main()
