from sensorik import Sensor

class AlarmSystem(object):
    __security_level = None
    __active_sensors = None

    def __init__(self, security_level: int):
        self.__security_level = security_level
        self.__active_sensors = []

    def get_security_level(self) -> int:
        return self.__security_level
    
    def get_active_sensors(self) -> list:
        return self.__active_sensors
    
    def trigger_alarm(self):
        return f"\033[91mHalte Ein, Abschaum!!!So WEHRE DICH NICHT!!! Auf das Ich dir sonst verpasse, eine Fraktur!!!\033[0m"

    def add_external_sensors(self, sensor: Sensor):
        # Von andre heißt die get-Methode zu der Klasse Sensor --> getsensor()
        # Füge mit der get-Methode, den ausgelesesenen Sensor-Typ, der mit dem Argument übegeben wurde, der Liste hinzu
        self.__active_sensors.append(sensor.getsensor())
        print(f"\033[95m{self.__active_sensors}\033[0m")
    
    # -------FALLS eine Liste übergeben wird!--------

    # def add_external_sensors(self,sensor):
    #     # Von andre heißt die get-Methode zu der Klasse Sensor --> getsensor()
    #     # Füge mit der get-Methode, den ausgelesesenen Sensor-Typ, der mit dem Argument übegeben wurde, der Liste hinzu
    #     for i in range(len(sensor)):
    #         self.__active_sensors.append(sensor[i].getsensor())
    #         print(f"\033[95m{self.__active_sensors[i]}\033[0m")