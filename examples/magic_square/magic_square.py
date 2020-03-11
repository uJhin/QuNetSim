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
WAIT_TIME = 10
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
    # print('Alice1: ' + qa.id)
    qc = host.get_epr(other_player, epr_id2)
    # print('Alice2: ' + qc.id)
    row = int(host.get_classical(jury)[0].content)

    N = 3
    M = 3

    res_row = [[0 for i in range(N)] for j in range(M)]

    res_row[0][0] = parity_meas([qa, qc], "IZ", host, True)
    res_row[0][1] = parity_meas([qa, qc], "ZI", host, True)
    res_row[0][2] = parity_meas([qa, qc], "ZZ", host)

    res_row[1][0] = parity_meas([qa, qc], "XI", host, True)
    res_row[1][1] = parity_meas([qa, qc], "IX", host, True)
    res_row[1][2] = parity_meas([qa, qc], "XX", host)

    res_row[2][0] = parity_meas([qa, qc], "XZ", host, True)
    res_row[2][1] = parity_meas([qa, qc], "ZX", host, True)
    res_row[2][2] = parity_meas([qa, qc], "YY", host)

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

    print('ROW:' + str(row) + ',', res_row[row][0], res_row[row][1], res_row[row][2])
    print(res_row)

    # print('m0_r')
    # print(m_0)
    # print('m1_r')
    # print(m_1)
    # print('m2_r')
    # print(m_2)

    return


def player_2(host, other_player, jury):
    global res_col
    qb = host.get_epr(other_player, wait=WAIT_TIME)
    # print('Bob1: ' + qb.id)
    qd = host.get_epr(other_player, wait=WAIT_TIME)
    # print('Bob2: ' + qd.id)
    col = int(host.get_classical(jury, wait=WAIT_TIME)[0].content)
    # print('COL')
    # print(col)

    N = 3
    M = 3

    res_col = [[0 for i in range(N)] for j in range(M)]

    res_col[0][0] = parity_meas([qb, qd], "IZ", host, True)
    res_col[0][1] = parity_meas([qb, qd], "XI", host, True)
    res_col[0][2] = parity_meas([qb, qd], "XZ", host, True)

    res_col[1][0] = parity_meas([qb, qd], "ZI", host, True)
    res_col[1][1] = parity_meas([qb, qd], "IX", host, True)
    res_col[1][2] = parity_meas([qb, qd], "ZX", host, True)

    res_col[2][0] = parity_meas([qb, qd], "ZZ", host)
    res_col[2][1] = parity_meas([qb, qd], "XX", host)
    res_col[2][2] = parity_meas([qb, qd], "YY", host)

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

    print('COL:' + str(col) + ',', res_col[col][0], res_col[col][1], res_col[col][2])
    print(res_col)
    # print('m0_c')
    # print(m_0)
    # print('m1_c')
    # print(m_1)
    # print('m2_c')
    # print(m_2)

    # host.send_classical(jury, )
    return


def judge(host, first_player, second_player):
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    host.send_classical(first_player, str(row), True)
    host.send_classical(second_player, str(col), True)

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

    # For first person turn.
    turn = 1

    # main_flag = 0
    # results = 0
    # if main_flag == 0:
    #     results = DaemonThread(mgl.process())
    #     main_flag = 1

    def clicked1():
        global turn
        if btn1["text"] == " ":  # For getting the text of a button
            if turn == 1:
                turn = 2
                btn1["text"] = "X"
            elif turn == 2:
                turn = 1;
                btn1["text"] = "O"
            check();

    def clicked2():
        global turn
        if btn2["text"] == " ":
            if turn == 1:
                turn = 2;
                btn2["text"] = "X"
            elif turn == 2:
                turn = 1;
                btn2["text"] = "O"
            check();

    def clicked3():
        global turn
        if btn3["text"] == " ":
            if turn == 1:
                turn = 2;
                btn3["text"] = "X"
            elif turn == 2:
                turn = 1;
                btn3["text"] = "O"
            check();

    def clicked4():
        global turn
        if btn4["text"] == " ":
            if turn == 1:
                turn = 2;
                btn4["text"] = "X"
            elif turn == 2:
                turn = 1;
                btn4["text"] = "O"
            check();

    def clicked5():
        global turn
        if btn5["text"] == " ":
            if turn == 1:
                turn = 2;
                btn5["text"] = "X"
            elif turn == 2:
                turn = 1;
                btn5["text"] = "O"
            check();

    def clicked6():
        global turn
        if btn6["text"] == " ":
            if turn == 1:
                turn = 2;
                btn6["text"] = "X"
            elif turn == 2:
                turn = 1;
                btn6["text"] = "O"
            check();

    def clicked7():
        global turn
        if btn7["text"] == " ":
            if turn == 1:
                turn = 2;
                btn7["text"] = "X"
            elif turn == 2:
                turn = 1;
                btn7["text"] = "O"
            check();

    def clicked8():
        global turn
        if btn8["text"] == " ":
            if turn == 1:
                turn = 2;
                btn8["text"] = "X"
            elif turn == 2:
                turn = 1;
                btn8["text"] = "O"
            check();

    def clicked9():
        global turn
        if btn9["text"] == " ":
            if turn == 1:
                turn = 2;
                btn9["text"] = "X"
            elif turn == 2:
                turn = 1;
                btn9["text"] = "O"
            check();

    flag = 1;

    window = Tk()
    window.title("TIC-Tac-Toe ")
    window.geometry("800x500")
    lbl = Label(window, text="Tic-tac-toe Game", font=('Helvetica', '15'))
    lbl.grid(row=0, column=0)
    Label(window, text="Row").grid(row=3)
    Label(window, text="Column").grid(row=4)

    row_entry = Entry(window)
    col_entry = Entry(window)

    row_entry.grid(row=3, column=1)
    col_entry.grid(row=4, column=1)

    print('ENTRY 1')
    print(row_entry)

    def check():
        global flag;
        b1 = btn1["text"];
        b2 = btn2["text"];
        b3 = btn3["text"];
        b4 = btn4["text"];
        b5 = btn5["text"];
        b6 = btn6["text"];
        b7 = btn7["text"];
        b8 = btn8["text"];
        b9 = btn9["text"];

        if row_entry == '1':
            btn1["text"] = res_row[0][0]
            btn2["text"] = res_row[0][1]
            btn3["text"] = res_row[0][2]

        print('ENTRY 1')
        print(row_entry)

        # flag = flag + 1;
        # if b1 == b2 and b1 == b3 and b1 == "O" or b1 == b2 and b1 == b3 and b1 == "X":
        #     win(btn1["text"])
        # if b4 == b5 and b4 == b6 and b4 == "O" or b4 == b5 and b4 == b6 and b4 == "X":
        #     win(btn4["text"]);
        # if b7 == b8 and b7 == b9 and b7 == "O" or b7 == b8 and b7 == b9 and b7 == "X":
        #     win(btn7["text"]);
        # if b1 == b4 and b1 == b7 and b1 == "O" or b1 == b4 and b1 == b7 and b1 == "X":
        #     win(btn1["text"]);
        # if b2 == b5 and b2 == b8 and b2 == "O" or b2 == b5 and b2 == b8 and b2 == "X":
        #     win(btn2["text"]);
        # if b3 == b6 and b3 == b9 and b3 == "O" or b3 == b6 and b3 == b9 and b3 == "X":
        #     win(btn3["text"]);
        # if b1 == b5 and b1 == b9 and b1 == "O" or b1 == b5 and b1 == b9 and b1 == "X":
        #     win(btn1["text"]);
        # if b7 == b5 and b7 == b3 and b7 == "O" or b7 == b5 and b7 == b3 and b7 == "X":
        #     win(btn7["text"]);
        # if flag == 10:
        #     messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        #     window.destroy()

    def win(player):
        ans = "Game complete " + player + " wins ";
        messagebox.showinfo("Congratulations", ans)
        window.destroy()  # is used to close the program

    btn1 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=clicked1)
    btn1.grid(column=4, row=1)
    btn2 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=clicked2)
    btn2.grid(column=5, row=1)
    btn3 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=clicked3)
    btn3.grid(column=6, row=1)
    btn4 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=clicked4)
    btn4.grid(column=4, row=2)
    btn5 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=clicked5)
    btn5.grid(column=5, row=2)
    btn6 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=clicked6)
    btn6.grid(column=6, row=2)
    btn7 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=clicked7)
    btn7.grid(column=4, row=3)
    btn8 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=clicked8)
    btn8.grid(column=5, row=3)
    btn9 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=clicked9)
    btn9.grid(column=6, row=3)

    window.mainloop()


if __name__ == '__main__':
    main()
