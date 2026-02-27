
class Room(object):                     # klasse Room erbt von (object)
    room_name = None                     # klassen attribut (nur für mich nicht wirklich benutzt)

    def __init__(self, room_name: str):        # konstruktor  wird automatisch beim erstellen aufgerufen
        self.room_name = room_name              # instanz attribut gehört zu diesem (objekt)
        self.sensors = []                   # liste für sensor-Objekte (komposition)


    def add_new_sensor(self, typ: str):
        neu_sensor = Sensor(typ)                # neu attribute
        self.sensors.append(neu_sensor)


    def auslesen(self):
        for i in range(len(self.sensors)):
            print(self.sensors[i].get_typ())


class Sensor(object):
    __sensor_type = None

    def __init__(self, sensor_type: str):
        self.__sensor_type = sensor_type

    def getsensor(self) -> str:
        return self.__sensor_type

    def read_value(self) -> float:
        # testdaten...
        return 0.5