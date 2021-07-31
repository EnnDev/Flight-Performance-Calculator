# This is an Aerodynamics calculator by Nathaniel Igot
# All code is written by me.

import math


def standard_constants():
    grav = 32.2
    r_const = 1716
    a = -0.00356
    t = 519
    press = 2116.2
    dens = 0.00238
    return grav, r_const, a, t, press, dens


def isothermal_constants():
    grav = 32.2
    r_const = 1716
    a = 0
    t = 390.5
    press = 472.6
    dens = 0.00071
    return grav, r_const, a, t, press, dens


def get_dpt():
    grav, r_const, a, t, press, dens = standard_constants()
    alt = float(input("Please enter an altitude in feet: "))
    oat_check = input("Do you have an OAT? (Type in yes or no): ")
    if oat_check == "yes":
        oat = float(input("Please enter the OAT: "))
        alt_temp = round(oat + 460, 1)
        alt_press = round(press * (1 + (a * alt / t)) ** (-grav / (a * r_const)), 1)
        if alt == 10000:
            alt_dens = .00176
        else:
            alt_dens = round(alt_press / (alt_temp * r_const), 5)
        return alt_dens, alt_press, alt_temp
    else:
        alt_temp = round(t + a * alt, 1)
        alt_press = round(press * (1 + (a * alt / t)) ** (-grav / (a * r_const)), 1)
        if alt == 10000:
            alt_dens = .00176
        else:
            alt_dens = round(alt_press / (alt_temp * r_const), 5)
        return alt_dens, alt_press, alt_temp


def get_dens_altitude():
    grav, r_const, a, t, press, dens = standard_constants()
    alt_dens, alt_press, alt_temp = get_dpt()
    dens_alt = t/a*(((alt_dens/dens)**(1/(grav/((a*r_const)-1))))-1)
    return dens_alt

# def getStall():

def get_speed():
    option = input("Is the speed in MPH or FPS?: ")
    while option:
        if option == "MPH" or "mph":
            print("Horsepower Calculations need to be in FPS.")
            convert = input("Would you like to convert to FPS? (yes or no): ")
            while convert:
                if convert == "yes":
                    speed = float(input("Please enter the speed : "))
                    new_speed = speed * 88 / 60
                    return new_speed
                elif convert == "no":
                    speed = float(input("Please enter the speed : "))
                    return speed
                else:
                    convert = input("Wrong input.\nWould you like to convert to FPS? (yes or no): ")
        elif option == "FPS" or "fps":
            convert = input("Would you like to convert to MPH? (yes or no): ")
            while convert:
                if convert == "yes":
                    speed = float(input("Please enter the speed : "))
                    new_speed = speed * 60 / 88
                    return new_speed
                elif convert == "no":
                    speed = float(input("Please enter the speed : "))
                    return speed
                else:
                    convert = input("Wrong input.\nWould you like to convert to FPS? (yes or no): ")
        else:
            option = input("Try Again.\nIs the speed in MPH or FPS?: ")


def get_velocity(speed):
    option = input("Are you looking for IAS or TAS?: ")
    dens_alt, press_alt, temp_alt = get_dpt()
    dens = 0.00238
    while option:
        if option == "ias" or "IAS":
            print("Input the TAS: ")
            tas = get_speed(speed)
            return 0
        elif option == "tas" or "TAS":
            print("Input the IAS: ")
            ias = get_speed(speed)
            tas = ias*math.sqrt(dens/dens_alt)
            return tas
        else:
            option = input("Try again.\nAre you looking for IAS or TAS?: ")


def get_horsepower_a():
    option = input("Do you need HPA at an altitude? (yes or no): ")
    while option:
        if option == "yes":
            dens = 0.00238
            dens_alt, pres, alt = get_dpt()
            option2 = input("Do you have Propeller Efficiency (n) and Brake Horsepower? (yes or no): ")
            while option2:
                if option2 == "yes":
                    prop_eff = float(input("Please Enter the Prop Efficiency: "))
                    bhp = float(input("Please Enter the Brake Horsepower: "))
                    horsepower_a = prop_eff * bhp
                    hp_alt = horsepower_a * (dens_alt / dens)
                    return hp_alt
                elif option2 == "no":
                    thrust = float(input("Please enter the Thrust of the aircraft: "))
                    speed = get_speed()
                    horsepower_a = thrust * speed
                    hp_alt = horsepower_a * (dens_alt / dens)
                    return hp_alt
        elif option == "no":
            option2 = input("Do you have Propeller Efficiency (n) and Brake Horsepower? (yes or no): ")
            while option2:
                if option2 == "yes":
                    prop_eff = float(input("Please Enter the Prop Efficiency: "))
                    bhp = float(input("Please Enter the Brake Horsepower: "))
                    horsepower_a = prop_eff * bhp
                    return horsepower_a
                elif option2 == "no":
                    thrust = float(input("Please enter the Thrust of the aircraft: "))
                    speed = get_speed()
                    horsepower_a = thrust * speed
                    return horsepower_a
                else:
                    option = input(
                        "Please try again.\nDo you have Propeller Efficiency (n) and Brake Horsepower? (yes or no): ")
        else:
            option = input("Wrong input, try again.\nDo you need HPA at an altitude? (yes or no): ")


def get_horsepower_r():
    option = input("Do you need HPR at an altitude? (yes or no): ")
    while option:
        if option == "yes":
            dens = 0.00238
            dens_alt, pres, alt = get_dpt()
        elif option == "no":
            drag = float(input("Enter the drag: "))
            speed = float(input("Enter the velocity: "))
            convert = input("velocity needs to be in TAS. Convert? (yes or no): ")
            while convert:
                if convert == "yes":
                    newspeed = drag * (speed * 88 / 60) / 550
                    return newspeed
                elif convert == "no":
                    newspeed = drag * speed / 550
                    return newspeed
                else:
                    convert = input("Try again.\nvelocity needs to be in TAS. Convert? (yes or no): ")
        else:
            option = input("Wrong input, try again.\nDo you need HPR at an altitude? (yes or no): ")

    return 0


def get_new_weight():
    # Example: New weight = 1750 lbs
    # alpha = constant
    # New weight = Lift = 1/2 Cl*density*velocity^2*Planform Area (S)
    #   Velocity needs to be adjusted
    # Max weight = Lift = 1/2 Cl*density*velocity^2*Planform Area (S)
    #   NewWeight/Max Weight = NewVelocity^2/MaxVelocity^2 => NewVelocity = MaxVelocity*sqrt(NewWeight/MaxWeight)
    newWeight = input("Please enter the new weight")
    maxWeight = input("Please enter the max weight")
    velocityNew = velocityMax * math.sqrt(newWeight / maxWeight)
    return velocityNew

def get_glide_angle():
    weight = float(input("Enter the weight of the aircraft in lbs: "))
    drag = float(input("Enter the drag in lbs: "))
    angle_deg = degrees(atan(drag/weight))
    angle_rad = atan(drag/weight)
    return angle_deg, angle_rad

def get_feul_burn():
    return 0

def get_range():
    return 0

def get_endurance():
    return 0

def get_takeoff_distance():
    weight = float(input("Please Enter the Weight of the aircraft in lbs: "))
    speed = float(input("Enter the ground speed in fps: "))
    thrust_av = float(input("Enter the average thrust in lbs: "))
    drag_av = float(input("Enter the average drag in lbs: "))
    roll_res = float(input("Enter the rolling resistance in lbs: "))
    tan_comp = float(input("Enter the tangential component in lbs: "))
    takeoff_distance = round(weight*speed**2/(2*32.2*(thrust_av-drag_av-roll_res-tan_comp)), 1)
    return takeoff_distance

def main():
    print("Main menu:")
    print("0) Exit program")
    print("1) Get Density, Pressure, and Temperature at altitude")
    print("2) Get Density Altitude")
    print("3) Get Horsepower Available")
    print("4) Get Horsepower Required")
    print("5) Get Takeoff Distance")

    #    print("5) Get the ceiling (H)")
    #    print("6) Time to climb")
    #    print("7) Get Energy Height")
    #    print("8) Drag equation")
    #    print("9) Get Aircraft Range")
    #    print("10) Get Aircraft Endurance")
    option = int(input("Please enter what you are trying to find: "))
    while option != 0:
        if option == 1:
            a, b, c = get_dpt()
            print("Density at altitude: " + str(a) + "\nPressure at altitude: " + str(
                b) + "\nTemperature at altitude: " + str(c))
            option = int(input("Please enter what you are trying to find: "))
        elif option == 2:
            dens_alt = get_dens_altitude()
            print(dens_alt)
        elif option == 3:
            HP = get_horsepower_a()
            print("Horsepower Available at MSL is " + str(HP) + " HP")
            option = int(input("Please enter what you are trying to find: "))
        elif option == 4:
            get_horsepower_r()
            option = int(input("Please enter what you are trying to find: "))
        elif option == 5:
            takeoff_distance = get_takeoff_distance()
            print(takeoff_distance)
            option = int(input("Please enter what you are trying to find: "))
    #        elif option == 5:
    #            getCeiling()
    #            option = int(input("Please enter what you are trying to find: "))
    #        elif option == 6:
    #            getTime()
    #            option = int(input("Please enter what you are trying to find: "))
    #        elif option == 7:
    #            getEnergyHeight()
    #            option = int(input("Please enter what you are trying to find: "))
    return 0


main()
