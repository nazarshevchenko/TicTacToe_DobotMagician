import numpy as np
import random


class Game:
    def __init__(void):

        void.reset()

    def reset(void):
        void.mass = [[" ", "|", " ", "|", " "],
                     ["-", "+", "-", "+", "-"],
                     [" ", "|", " ", "|", " "],
                     ["-", "+", "-", "+", "-"],
                     [" ", "|", " ", "|", " "]]
        void.count = 0
        void.draw = False
        void.massO = np.zeros([9], dtype=np.uint8)
        void.massX = np.zeros([9], dtype=np.uint8)

    def get(void, s):

        if s == "O":
            return void.massO
        elif s == "X":
            return void.massX

    def show(void):
        print()
        q = ""
        for i in void.mass:
            for j in i:
                q += j

            print(q)
            q = ""
        print()

    def make(void, data, s):

        void.count += 1

        if s != "O" and s != "X":
            void.count -= 1
            return False

        void.__getCoordinate__(data)

        if void.y != None and void.x != None:
            if void.mass[void.y][void.x] == " ":
                void.mass[void.y][void.x] = s

                if s == "O":
                    void.massO[data - 1] = 1
                if s == "X":
                    void.massX[data - 1] = 1

                return True

            else:
                void.count -= 1
                return False

        else:
            void.count -= 1
            return False

    def __getCoordinate__(void, data):

        if data > 0 and data < 10:
            if data < 4:
                void.x = data
                void.y = 1
            elif data > 3 and data < 7:
                void.x = data - 3
                void.y = 2
            else:
                void.x = data - 6
                void.y = 3

            if void.x == 1:
                void.x = 0

            if void.y == 1:
                void.y = 0

            if void.x == 2:
                void.x = 2

            if void.y == 2:
                void.y = 2

            if void.x == 3:
                void.x = 4

            if void.y == 3:
                void.y = 4

        else:
            void.x = None
            void.y = None

    def isWin(void, s):
        if void.draw:
            return "D"
        return void.__Win__(s)

    def isfinish(void):

        if void.count == 9:
            void.draw = True
            return True

        elif void.__Win__("X"):
            return True
        elif void.__Win__("O"):
            return True

        else:
            return False

    def __Win__(void, s):

        if s == "O":
            void.win = void.massO.reshape([3, 3])
        else:
            void.win = void.massX.reshape([3, 3])

        for i in void.win:
            if i.all() == 1:
                return True

        void.some = 0
        for i in void.win:
            if i[0] == 1:
                void.some += 1
        if void.some == 3:
            return True

        void.some = 0
        for i in void.win:
            if i[1] == 1:
                void.some += 1
        if void.some == 3:
            return True

        void.some = 0
        for i in void.win:
            if i[2] == 1:
                void.some += 1
        if void.some == 3:
            return True

        void.some = 0
        for i in range(3):
            if void.win[i][i] == 1:
                void.some += 1

        if void.some == 3:
            return True

        if void.win[0][2] == 1 and void.win[1][1] == 1 and void.win[2][0]:
            return True

        return False


class AI:
    def __init__(void, sign):
        void.sign = sign

        # void.q_table = np.zeros([512, 512, 9])
        void.q_table = np.random.rand(512, 512, 9)

    def get_hex(void, hex):

        void.n = hex.shape[0]
        void.res = 0
        for i in reversed(hex):
            void.n -= 1
            void.res += i * (2 ** void.n)

        return int(void.res)

    def action(void, my, enemy):

        # void.my = void.get_hex(my)
        # void.enemy = void.get_hex(enemy)

        # void.action = np.argmax(void.q_table[void.my][void.enemy])
        void.action = np.argmax(void.q_table[my][enemy])
        return void.action

    def train(void, episodes, a, y, e):
        void.a = a
        void.y = y
        void.e = e

        for i in range(episodes):

            void.done = False

            while not void.done:

                if random.uniform(0, 1) < void.e:
                    void.actions = void.action()
                else:
                    void.actions = random.radint(0, 9)


