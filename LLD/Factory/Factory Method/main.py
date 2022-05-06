from auto_factory import AutoFactory
if __name__ == "__main__":
    factory = AutoFactory()
    for vehical in ["FordFusion", "JeepSahara", "ChevyVolt"]:
        car = factory.get_auto(vehical)
        car.start()
        car.stop()