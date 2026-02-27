from core import Device

class Light(Device):
    __brightness = None
    __is_on = None
    
    def __init__(self, device_id: str, brightness: int):
        super().__init__(device_id)
        self.__brightness = brightness

    def set_brightness(self, level: int):
        self.__brightness = level

    def turn_off(self):
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True