
class Singleton(object):
    _instance = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__new__(cls)
            cls._instance[cls] = instance
        return cls._instance[cls]
