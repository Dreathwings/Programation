import math
from math import cos, pi,sin

# Dimensions used for the PhantomX robot :
#constL1 = 54.8
#constL2 = 65.3
#constL3 = 133
#theta2Correction = 0  # A completer
#theta3Correction = 0  # A completer

# Dimensions used for the simple arm simulation
bx = 0.07
bz = 0.25
constL1 = 0.085
constL2 = 0.185
constL3 = 0.250


def computeDK(theta1, theta2, theta3, l1=constL1, l2=constL2, l3=constL3):
    ''' Terminal
    theta1rad = (theta1*(pi/180))
    theta2rad = (theta2*(pi/180))
    theta3rad = (theta3*(pi/180))

    x = ((l1+l2*cos(theta2rad)+l3*cos(theta3rad+theta2rad))*cos(theta1rad))
    y = ((l1+l2*cos(theta2rad)+l3*cos(theta3rad+theta2rad))*sin(theta1rad))
    z = (l2*sin(theta2rad)+l3*sin(theta2rad+theta3rad))'''

    '''Simulation'''
    x = ((l1 + l2*cos(theta2) + l3*cos(theta3+theta2)) * cos(theta1))
    y = ((l1 + l2*cos(theta2) + l3*cos(theta3+theta2)) * sin(theta1))
    z = -(l2*sin(theta2) + l3*sin(theta2+theta3))



    return [x, y, z]


def computeIK(x, y, z, l1=constL1, l2=constL2, l3=constL3):
    theta1 = 0
    theta2 = 0
    theta3 = 0

    return [theta1, theta2, theta3]


def main():
    print("Testing the kinematic funtions...")
    print("L1 + L2 + L3= {}".format(
        constL1+constL2+constL3
    ) )
    print(
        "computeDK(0, 0, 0) = {}".format(
            computeDK(0, 0, 0, l1=constL1, l2=constL2, l3=constL3) # attendu: [253.1, 0, 0]

        )
    )
    print(
        "computeDK(90, 7, 11) = {}".format(
            computeDK(90, 7, 11, l1=constL1, l2=constL2, l3=constL3)# attendu: [0, 246, 49]

        )
    )
    print(
        "computeDK(90, 88, 63) = {}".format(
            computeDK(90, 88, 63, l1=constL1, l2=constL2, l3=constL3)# arrendu: [0, -59, 129]

        )
    )
if __name__ == "__main__":
    main()
