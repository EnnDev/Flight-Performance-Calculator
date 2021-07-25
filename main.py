# This is an Aerodynamics calculator by Nathaniel Igot
# All code is written by me.

import math

def standardConstants():
    grav = 32.2
    rConst = 1716.0
    a = -0.00356
    T = 519.0
    press = 2116.2
    dens = 0.00238
    return grav, rConst, a, T, press, dens

def isothermalConstants():
    grav = 32.2
    rConst = 1716.0
    a = -0.00356
    T = 390.5
    press = 472.6
    dens = 0.00071
    return grav, rConst, a, T, press, dens

def getDPT():
    grav, rConst, a, T, press, dens = standardConstants()
    alt = float(input("Please enter an altitude in feet: "))
    oatCheck = input("Do you have an OAT? (Type in yes or no): ")
    if oatCheck == "yes":
        oat = float(input("Please enter the OAT: "))
        altTemp = oat + 460
        altPress = press * (1 + (a * alt / T)) ** (-grav / (a * rConst))
        altDens = altPress/(altTemp * rConst)
        return (altDens, altTemp, altPress)
    else:
        altTemp = T + a * alt
        altPress = press * (1 + (a * alt / T)) ** (-grav / (a * rConst))
        altDens = altPress/(altTemp*rConst)
        return (altDens, altTemp, altPress)

#def getStall():


def getSpeed():
    speed = float(input("Please enter the speed: "))
    option = input("Enter 1 for MPH conversion, Enter 2 for FPS, Enter 3 to skip conversion: ")
    while option != "1" or "2" or "3":
        if option == "1":
            newSpeed = speed*88/60
            return newSpeed
        elif option == "2":
            newSpeed = speed*60/88
            return newSpeed
        elif option ==  "3":
            return speed

def getHorsepower():
    option = input("Are you looking for Horsepower Available or Horsepower Required? \nEnter 1 for Available, 2 for Required: ")
    while option != "1" or "2":
        if option == "1":
            option2 = input("Do you have Propeller Efficiency (n) and Brake Horsepower? (yes or no): ")
            while option2 != "yes" or "no":
                if option2 == "yes":
                    propEff = float(input("Please Enter the Prop Efficiency: "))
                    BHP = float(input("Please Enter the Brake Horsepower: "))
                    horsepowerAvialable = propEff*BHP
                    return horsepowerAvialable
                elif option2 == "no":
                    thrust = float(input("Please enter the Thrust of the aircraft: "))
                    speed = getSpeed()
                    horsepowerAvailable = thrust*speed
                    return horsepowerAvailable
                else:
                    option2 = input("Please try again.\nDo you have Propeller Efficiency (n) and Brake Horsepower? (yes or no): ")
        elif option == "2":
            print("test")
        else:
            option = input("Please try again. \nAre you looking for Horsepower Available or Horsepower Required? \nEnter 1 for Available, 2 for Required: ")


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

def main():
    print("Main menu:")
    print("0) Exit program")
    print("1) Get Density, Pressure, and Temperature at altitude")
    print("2) Get the stall speeds")
    print("3) Get Horsepower")
    print("4) Get the Rate of Climb (ROC)")
    print("5) Get the ceiling (H)")
    print("6) Time to climb")
    print("7) Get Energy Height")
    print("8) Drag equation")
    print("9) Get Aircraft Range")
    print("10) Get Aircraft Endurance")
    option = int(input("Please enter what you are trying to find :"))
    if option == 1:
        a, b, c = getDPT()
        print("Density at altitude: "+str(a)+"\nTemperature at altitude: "+str(b)+"\nPressure at altitude: "+str(c))
    elif option == 2:
        getStall()
    elif option == 3:
        getHorsepower()
    elif option == 4:
        getRateofClimb()
    elif option == 5:
        getCeiling()
    elif option == 6:
        getTime()
    elif option == 7:
        getEnergyHeight()
main()