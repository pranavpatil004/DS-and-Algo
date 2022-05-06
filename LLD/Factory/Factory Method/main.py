from auto_factory import AutoFactory
if __name__ == "__main__":
    factory = AutoFactory()
    for vehical in ["Ford", "Jeep", "Chevy"]:
        car = factory.get_auto(vehical)
        car.start()
        car.stop()