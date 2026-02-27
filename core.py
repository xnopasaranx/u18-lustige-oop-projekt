class Device(object):
    __is_on = None
    __device_id = None

    def __init__(self,device_id: str):
        self.__device_id = device_id
    
    def turn_on():
        pass
    
    def turn_off():
        pass
    
    def getinfo(self):
        return self.__device_id