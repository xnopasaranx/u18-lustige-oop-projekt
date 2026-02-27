# klasse Room erbt von (object)
class Room(object):                     
    # klassen attribut (nur für mich nicht wirklich benutzt)
    __room_name = None                     
    __sensors = None

    # konstruktor  wird automatisch beim erstellen aufgerufen
    def __init__(self, room_name: str):
        # instanz attribut gehört zu diesem (objekt)        
        self.__room_name = room_name
        # liste für sensor-Objekte (komposition)              
        self.__sensors = []                   


    def add_new_sensor(self, typ: str):
        # neue attribute
        neu_sensor = Sensor(typ)                
        self.__sensors.append(neu_sensor)

    def get_sensors(self) -> list:
        return self.__sensors

    def auslesen(self):
        for i in range(len(self.__sensors)):
            print(self.__sensors[i].getsensor())


class Sensor(object):
    __sensor_type = None

    def __init__(self, sensor_type: str):
        self.__sensor_type = sensor_type

    def getsensor(self) -> str:
        return self.__sensor_type

    def read_value(self) -> float:
        # testdaten...
        return 0.5