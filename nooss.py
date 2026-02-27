class Device(object):
    pass

class Management(object):
    __owner = None
    __all_devices = None

    def __init__(self, owner: str):
        self.__owner = owner
        self.__all_devices = []

    def register_device(self, d: Device):
        self.__all_devices.append(d)
    
    def status_report(self):
        return [device for device in self.__all_devices]
