import math
from math import cos, pi, sin, acos, atan, sqrt


# Dimensions used for the PhantomX robot :
'''constL1 = 54.8
constL2 = 65.3
constL3 = 133
theta2Correction = 0  # A completer
theta3Correction = 0  # A completer'''

# Dimensions used for the simple arm simulation
bx = 0.07
bz = 0.25
constL1 = 0.085
constL2 = 0.185
constL3 = 0.250

def AlKashi(a,b,c):
    if a!=0 or b!=0:
        return acos(((a**2) + (b**2) - (c**2)) / (2*(a*b)))

def rotaton_2D(x, y, z, theta):
    # A compléter
    return 



def computeDK(theta1, theta2, theta3, l1=constL1, l2=constL2, l3=constL3):
    ##############TERMINAL##########################
    '''theta1rad = (theta1*(pi/180))
    theta2rad = (theta2*(pi/180))
    theta3rad = (theta3*(pi/180))

    x = ((l1+l2*cos(theta2rad)+l3*cos(theta3rad+theta2rad))*cos(theta1rad))
    y = ((l1+l2*cos(theta2rad)+l3*cos(theta3rad+theta2rad))*sin(theta1rad))
    z = (l2*sin(theta2rad)+l3*sin(theta2rad+theta3rad))'''


    ##############SIMULATION########################
    x = ((l1 + l2*cos(theta2) + l3*cos(theta3+theta2)) * cos(theta1))
    y = ((l1 + l2*cos(theta2) + l3*cos(theta3+theta2)) * sin(theta1))
    z = -(l2*sin(theta2) + l3*sin(theta2+theta3))



    return [x, y, z]


def computeIK(x, y, z, l1=constL1, l2=constL2, l3=constL3):

    pasttheta1 = 0
    pasttheta2 = 0
    pasttheta3 = 0

# 'dp' = 'dproj' => projection au sol de la distance P0 et P3proj
    dp = sqrt((x**2) + (y**2))
# 'd1' = 'd13'  => distance P1 - P3proj 
    d1 = dp - l1

    if d1 < 0:
# 
        d1 = 1

# 'd' hypothénuse de (P1, P3, P3proj)
    d = sqrt(d1**2+z**2)

    if d > l2+l3:
#'l2+l3' est la longueur MAX de 'd'
        d = l2+l3
    if d < -1:
        d = 1

    a = atan(z/d1.real)
    b = AlKashi(l2, d, l3)

    if x==0 and y==0:
        theta1 = pasttheta1
        theta2 = pasttheta2
        theta3 = pasttheta3


    elif x<0:
        theta1 = -atan(y/x+1)
        theta2 = (a + b)
        theta3 = -AlKashi(l2,l3,d)+pi

        pasttheta1 = theta1
        pasttheta2 = -theta2
        pasttheta3 = -theta3

    else:
        theta1 = atan(y/ x)                                            
        theta2 = a + b                                    
        theta3 = AlKashi(l2,l3,d)+pi

        pasttheta1 = theta1
        pasttheta2 = -theta2
        pasttheta3 = -theta3

    return [theta1, -theta2, -theta3]


def main():
    
    
   
    print("Testing the kinematic funtions...")
    print("L1 + L2 + L3= {}".format(
        constL1+constL2+constL3
    ) )

    ############ TEST COMPUTEIK ###################
    print(
        "computeIK(10, 90, 99) = {}".format(
            computeIK(10, 90, 99, l1=constL1, l2=constL2, l3=constL3) # attendu: [253.1, 0, 0]

        )
    )
    print(
        "computeIK(90, 7, 11) = {}".format(
            computeIK(90, 7, 11, l1=constL1, l2=constL2, l3=constL3)# attendu: [0, 246, 49]

        )
    )
    print(
        "computeIK(90, 88, 63) = {}".format(
            computeIK(90, 88, 63, l1=constL1, l2=constL2, l3=constL3)# arrendu: [0, -59, 129]

        )
    )
    ############ TEST COMPUTEDK ####################
    '''
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
    '''

if __name__ == "__main__":
    main()
