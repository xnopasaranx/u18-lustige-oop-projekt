class Sensor(object):
    __sensor_type =None

    def __init__(self, sensor_type: str ):
        self.__sensor_type = sensor_type

    def getsensor(self):
        return self.__sensor_type

    def read_value(self) -> float:
        # testdaten...
        return 0.5