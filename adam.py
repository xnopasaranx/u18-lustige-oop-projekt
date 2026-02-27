class Device:
    __is_on=None
    __device_id=None
    def __init__(self,device_id):
        self.__device=device_id
    def turn_on():
        pass
    def turn_off():
        pass
    def getinfo(self):
        return self.__device, self.__on
    
class Light(Device):
    __brightness=None
    def __init__(self, device_id, brightness):
        super().__init__(device_id)
        self.__brightness=brightness

    def set_brightness(self,level):
        self.__brightness=level

    def turn_off(self):
        self.__is_on=False

    def turn_on(self):
        self.__is_on=True


class Thermostat(Device):
    __current_temp=None
    def __init__(self, device_id,target_temp):
        super().__init__(device_id)
        self.__target_temp=float
        self.__target_temp=target_temp

    def set_temp(self,temp):
        self.__target_temp=temp

    def turn_off(self):
        self.__is_on=False

    def turn_on(self):
        self.__is_on=True
