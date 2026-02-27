from management import SmartHome
from core import Device
from beleuchtung import Light
from klima import Thermostat

def init_demo():
    demo_management = SmartHome(owner="Demo Besitzer")

    licht1 = Light(device_id="licht1", brightness=0)
    licht2 = Light(device_id="licht2", brightness=0)

    therm1 = Thermostat(device_id="therm1", target_temp=20)
    therm2 = Thermostat(device_id="therm2", target_temp=20)

    devices = [licht1, licht2, therm1, therm2]

    for dev in devices:
        demo_management.register_device(dev)

    return demo_management.status_report()

print(init_demo())