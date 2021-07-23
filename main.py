# This is an Aerodynamics calculator by Nathaniel Igot
# All code is written by me.

import math

# This is just a test

def getDPT():
    grav = 32.2
    rConst = 1716.0
    a = -0.00356
    T = 519.0
    press = 2116.2
    dens = 0.00238
    alt = float(input("Please enter an altidude: "))
    oatCheck = input("Do you have an OAT? (Type in yes or no): ")
    if oatCheck == "yes":
        oat = float(input("Please enter the OAT: "))
        altTemp = oat + 460
    else:
        altTemp = T + a * alt
    if alt > 36000:
        a = 0
        T = 390.5
        press = 472.6
        dens = 0.00071
    altPress = getPressure(a, press, alt, T, grav, rConst)
    altDens = getDensity(altPress, altTemp, rConst)

def getPressure(a, p, height, temp, grav, const):
    pressAlt = p*(1+(a*height/temp))**(-grav/(a*const))
    return pressAlt

def getDensity(p, temp, const):
    densAlt = p/(temp*const)
    return densAlt

def getNewWeight():
    # Example: New weight = 1750 lbs
    # alpha = constant
    # New weight = Lift = 1/2 Cl*density*velocity^2*Planform Area (S)
    #   Velocity needs to be adjusted
    # Max weight = Lift = 1/2 Cl*density*velocity^2*Planform Area (S)
    #   NewWeight/Max Weight = NewVelocity^2/MaxVelocity^2 => NewVelocity = MaxVelocity*sqrt(NewWeight/MaxWeight)
    newWeight = input("Please enter the new weight")
    maxWeight = input("Please enter the max weight")
    velocityNew = velocityMax*math.sqrt(newWeight/maxWeight)
    return velocityNew

def getNewDrag():


def main():
    print("Your altitude's temperature at " + str(alt) + " feet is: " + str(altTemp))
    print("Your altitude's pressure at " + str(alt) + " feet is: " + str(altPress))
    print("Your altitude's Density at " + str(alt) + " feet is: " + str(altDens))
    print("Main menu:")
    print("0) Reset all data")
    print("1) Get Density, Pressure, and Temperature at altitude")
    print("2) Get the stall speeds")
    print("3) Get Horsepower")
    print("4) Get the Rate of Climb (ROC)")
    print("5) Get the ceiling (H)")
    print("6) Time to climb")
    print("7) Get Energy Height")
    print("8) Drag equation")
    print("9) Get the Range of the Aircraft")
    print("10)")
    option = int(input("Please enter what you are trying to find :"))
    if option == 1:
        getDPT()
    else if option == 2:
        getStall()
    else if option == 3:
        getHorsepower()
    else if option == 4:
        getRateofClimb()
    else if option == 5:
        getCeiling()
    else if option == 6:
        getTime()
    else if option == 7:
        getEnergyHeight()
    else if option == 2:
        getStall()
    else if option == 3:
        getHorsepower()
    else if option == 4:
        getRateofClimb()
    else if option == 5:
        getCeiling()
    else if option == 6:
        getTime()
    else if option == 7:
        getEnergyHeight()
    else if option

main()