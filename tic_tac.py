import cv2
from Game import Game, AI  # Імпорт середовища гри (власний)
import random
import numpy as np
import sys

#import threading
import DobotDllType as dType
from time import sleep, time

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

api = dType.load()

state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])

dType.SetQueuedCmdClear(api)

dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

pos = dType.GetPose(api)

x = pos[0]
y = pos[1]
z = pos[2]
r = pos[3]

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# sys.setrecursionlimit(45000)
play = Game()

first = AI("O")
second = AI("X")


### for X
def min(alpha, beta):
    minv = 2

    q = None
    result = play.isfinish()

    if result:

        some = play.isWin("X")
        if some == True:

            return (-1, 0)
        elif some == "D":
            return (0, 0)
        else:
            return (1, 0)

    for i in range(9):
        X = play.get("X")
        O = play.get("O")

        if X[i] == 0 and O[i] == 0:
            play.massX[i] = 1
            play.count += 1
            # play.make(i + 1, "X")

            m, max_i = max(alpha, beta)

            if m < minv:
                minv = m
                q = i

            if play.count == 9:
                play.draw = False
            play.massX[i] = 0
            play.count -= 1
            if minv <= alpha:
                return minv, q

            if minv < beta:
                beta = minv
    return minv, q


###for O
def max(alpha, beta):
    maxv = -2

    q = None

    result = play.isfinish()

    if result:

        some = play.isWin("X")

        if some == True:
            return (-1, 0)
        elif some == "D":
            return (0, 0)
        else:
            print(some)
            return (1, 0)

    for i in range(9):
        X = play.get("X")
        O = play.get("O")
        if X[i] == 0 and O[i] == 0:
            play.massO[i] = 1
            play.count += 1
            # play.make(i + 1, "O")
            m, min_i = min(alpha, beta)

            if m > maxv:
                maxv = m
                q = i

            if play.count == 9:
                play.draw = False

            play.massO[i] = 0
            play.count -= 1
            if maxv >= beta:
                return (maxv, q)

            if maxv > alpha:
                alpha = maxv
    return maxv, q

def move_to(cord):
    if cord == 1:
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 190, -45, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 190, -45, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, -15, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, -15, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 150, 0, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)

    elif cord == 2:
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 190, -15, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 190, -15, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, 15, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, 15, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 150, 0, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)

    elif cord == 3:
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 190, 15, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 190, 15, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, 45, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, 45, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 150, 0, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)

    elif cord == 4:
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, -45, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, -45, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, -15, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, -15, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 150, 0, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
    elif cord == 5:
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, -15, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, -15, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 15, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 15, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 150, 0, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)

    elif cord == 6:
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, 15, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, 15, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 45, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 45, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 150, 0, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)

    elif cord == 7:
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, -45, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, -45, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 280, -15, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 280, -15, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 150, 0, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)

    elif cord == 8:

        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, -15, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, -15, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 280, 15, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 280, 15, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 150, 0, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)

    elif cord == 9:

        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 15, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 15, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 280, 45, -60, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 280, 45, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 150, 0, 0, 0, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)

    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(1000)

    dType.SetQueuedCmdStopExec(api)


def get_pos():
    frame = cap.read()[1]
    #cv2.imwrite('data.jpg', frame)

    #img = cv2.imread('data.jpg', 0)
    #img = frame.copy()
    #img = cv2.medianBlur(img, 5)

    img = cv2.medianBlur(cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY),5)

  #  cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50,
                               param1=50, param2=30, minRadius=20, maxRadius=100)


    mass = []
    try:
        circles = np.uint16(np.around(circles))
    except:
        cv2.destroyAllWindows()
        return mass

    print(circles)
   # cv2.destroyAllWindows()
    print(circles)
    for i in circles[0,:]:
        x = i[0]
        y = i[1]

        if (x > 336 and x < 386) and (y > 50 and y < 90):
            mass.append(1)

        elif (x > 332 and x < 382) and (y > 152 and y < 192):
            mass.append(2)

        elif (x > 300 and x < 368) and (y > 240 and y < 320):
            mass.append(3)

        elif (x > 228 and x < 272) and (y > 64 and y < 138):
            mass.append(4)

        elif (x > 225 and x < 260) and (y > 155 and y < 230):
            mass.append(5)

        elif (x > 210 and x < 260) and (y > 236 and y < 296):
            mass.append(6)

        elif (x > 136 and x < 186) and (y > 52 and y < 112):
            mass.append(7)

        elif (x > 126 and x < 176) and (y > 134 and y < 194):
            mass.append(8)

        elif (x > 110 and x < 160) and (y > 234 and y < 294):
            mass.append(9)
        else:
            print(i)

    return mass


def eviroment():
    r = 0
    ########################
    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, -45, 0, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, -45, -60, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, 45, -60, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 220, 45, 0, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    ########################
    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, -45, 0, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, -45, -60, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 45, -60, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 45, 0, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)
    ################
    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 190, -15, 0, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 190, -15, -60, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 280, -15, -60, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 280, -15, 0, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    ########################
    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 190, 15, 0, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 190, 15, -60, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 280, 15, -60, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 280, 15, 0, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)
    # dType.SetQueuedCmdStopExec(api)

    # lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x-20, y, z, r, isQueued = 1)[0]
    # dType.SetQueuedCmdStartExec(api)

    ######

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 150, 0, 0, r, isQueued=1)[0]
    dType.SetQueuedCmdStartExec(api)

    ######

    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(1000)

    dType.SetQueuedCmdStopExec(api)

def is_change(data):
    #a = len(data)
    some = get_pos()
    for i in some:
        if i not in data:
            sleep(0.5)
            if i not in data:
                return True
    return False
def start():

    eviroment()
    play.reset()
    done = False
    play.show()
    data = []
    while not done:
        m, q = min(-2, 2)
        play.make(q + 1, "X")
        move_to(q + 1)
        done = play.isfinish()
        if done:
            break
        play.show()
        #a = input("Go ")
        while True:
            T = is_change(data)
            if T:
                p = 0
                for i in range(2):
                    T = is_change(data)
                    if T:
                        p += 1

                if p == 2:
                    cor = get_pos()
                    for i in cor:
                        if i not in data:
                            data.append(i)
                            action = i
                break

        play.make(action, "O")
        play.show()
        done = play.isfinish()



start()

cv2.destroyAllWindows()

dType.DisconnectDobot(api)