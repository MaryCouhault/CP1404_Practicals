from Pract_06.car import Car
from Pract_08.taxi import Taxi
from Pract_08.SilverServiceTaxi import SilverServiceTaxi

MENU = "Q)uit, C)hoose taxi, D)rive"


def main():
    total_bill = 0
    taxis_selection = [Taxi("Mitisubishi", 90), SilverServiceTaxi("BMW", 140, 2),
                       SilverServiceTaxi("Landrover", 150, 3)]
    taxi_choice = None
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis_selection)
            taxi_choice = int(input("Choose taxi: "))
            try:
                taxi_choice = taxis_selection[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            if taxi_choice:
                taxi_choice.start_fare()
                drive_distance = float(input("How far will it drive you? "))
                taxi_choice.drive(drive_distance)
                taxi_fare = taxi_choice.get_fare()
                print("Your {} trip cost you ${:.2f}".format(taxi_choice.name, taxi_fare))
                total_bill += taxi_fare
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis_selection)


def run_tests():
    bus = Car("Beetle", 110)
    bus.drive(20)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo = ", bus.odometer)
    print(bus)

    distance = int(input("How far will it drive you"))
    while distance > 0:
        travelled = bus.drive(distance)
        print("{} travelled {}".format(str(bus), travelled))
        distance = int(input("How far will it drive you? "))

    t = Taxi("Lambo 1", 100)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())
    sst = SilverServiceTaxi("Limo", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())


def display_taxis(taxis_selection):
    for i, taxi in enumerate(taxis_selection):
        print("{} - {}".format(i, taxi))


main()
