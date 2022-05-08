from client import Client
from concrete_adapter import ConcreteAdapter
from target_json import TargetJSON
from adaptee import XMLProcessor
if __name__ == "__main__":
    target = TargetJSON()
    client = Client(target)
    print(client.get_name({"name": "my name"}))
    xml_processor = XMLProcessor()
    adapter = ConcreteAdapter(xml_processor)
    client1 = Client(adapter)
    print(client1.get_name({"name": "my name"}))
