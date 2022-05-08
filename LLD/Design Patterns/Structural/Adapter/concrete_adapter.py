from abstract_adapter import AbstractAdapter

class ConcreteAdapter(AbstractAdapter):
    def request(self, json_data):
        # converted json data to xml data
        xml_data = json_data
        # call the adaptee's specific request method
        return self._adaptee.specific_request_to_xml(xml_data)

