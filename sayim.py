#Das ist meins Cod Finger weg !

class Room(object):                     # klasse Room erbt von (object)
    room_name= None                     # klassen attribut (nur für mich nicht wirklich benutzt)

    def __init__(self, room_name : str):        # konstruktor  wird automatisch beim erstellen aufgerufen
        self.room_name = room_name              # instanz attribut gehört zu diesem (objekt)
        self.sensors = []                   # liste für sensor-Objekte (komposition)


    def add_new_sensor(self, typ :str):
        neu_sensor = Sensor(typ)                # neu attribute
        self.sensors.append(neu_sensor)


    def auslessen(self):
        for i in range(len(self.sensors)):
            print(self.sensors[i].get_typ())



class Sensor(object):                       # klasse sensor
    sensor_type= None                   # klassen attribut (nur für mich nicht wirklich benutzt)

    def __init__(self, sensor_typ : str):       # konstruktor sind hier
        self.sensor_typ = sensor_typ


    def read_volue(self):
       return 0.0

    
    def get_typ(self):
        return self.sensor_typ




meineRoom = Room("N1")              #room kommt oben init metode rein nicht vergessen
meineRoom.add_new_sensor("sensor no1")
meineRoom.auslessen()

# was hat ein calssen (object) = die haben atributen und methode
# atribute sind privat
# methode sind öffenlich kann alles sehen und abgerufen wender für alle..

# attribute:
#  speichern Daten
#  gehören zu einem Objekt (Instanzattribute)
# → Können privat sein (mit __ vor dem Namen)

# Methoden:
# → Sind Funktionen innerhalb einer Klasse
# → Können auf Attribute zugreifen
# → Meist öffentlich und von außen aufrufbar



