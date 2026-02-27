from core import Device

class Thermostat(Device):
    __current_temp = None
    __target_temp = None

    def __init__(self, device_id: str, target_temp: float):
        super().__init__(device_id)
        self.__target_temp = target_temp

    def set_temp(self, temp: float):
        self.__target_temp = temp

    def turn_off(self):
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True

    def get_temp(self):
        temp = self.__current_temp
        temp2 = self.__target_temp
        return temp, temp2