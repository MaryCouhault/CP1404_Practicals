from Pract_08.SilverServiceTaxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Test Fancy Fake Taxi", 90, 1)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
