#testi

class Sensor:
    def __init__(self,sensor_type):
        self.__sensor_type=sensor_type

    def getsensor(self):
        return self.__sensor_type

    def read_value(self):
        return "test"

class Room:
    def __init__(self,name,sensor_type):
        self.__name = name
        self.__sensors=[]
        self.__sensor = Sensor(sensor_type) #Komposition

    def add_new_sensor(self,sensor_type):
        n=Sensor(sensor_type)
        self.__sensors.append(n) #sensortyp wird der Liste sensor übergeben
    def getlistesensor(self):
        return self.__sensors


class AlarmSystem:
    def __init__(self,security_level):
        self.__security_level = security_level
        self.__active_sensors=[]

    def getsecurity(self):
        return self.__security_level
    def getactive_sensor(self):
        return self.__active_sensors
    
    def add_external_sensor(self):
        pass

    def trigger_alarm():
        pass


ein_Room=Room("D1","licht_sensor")
#ein_Room.add_new_sensor("lampe")
#ein_sensor=Sensor()
n=input("Eingabe Anzahl der Sensoren: -> ")
#Add input von Variable n in die liste_sensor
for i in range(int(n)):
    ein_Room.add_new_sensor(input(f"Eingabe der {i+1} von {n} Sensoren: -> "))

liste=ein_Room.getlistesensor() #Methode liste auslesen aufrufen
#Liste_sensor aus der Klasse Raum auslesen
for i in range(len(liste)):
    print(liste[i].getsensor())