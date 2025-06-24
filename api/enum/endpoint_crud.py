from enum import Enum

class EndpointCrud(Enum):
    CREATE= ""
    UPDATE= ""
    GET_BY = "/by"
    GET_ALL =""
    GET = ''
    DELETE = ""

    def get(self):
        return str.split(self.value, '/')[1]