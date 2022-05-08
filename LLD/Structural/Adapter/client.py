

class Client:
    def __init__(self, target) -> None:
        self.target = target

    def get_name(self, data):
        return self.target.request(data)
        