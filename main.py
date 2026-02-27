# importe der Klassen aus den externen Modulen

from management import SmartHome
from beleuchtung import Light
from klima import Thermostat

from security import AlarmSystem
from sensorik import Room, Sensor

# Eine Demo Funktion um einmal eine SmartHome Instanz zu erzeugen und zu demonstrieren 
# wie die Aggregation und Instanziierung der anderen Klassen funktioniert

def init_demo():
    # SmartHome Instanz erzeugen
    demo_management = SmartHome(owner="Demo Besitzer")

    # Ein paar Devices mit Subklassen Instanziieren 
    licht1 = Light(device_id="licht1", brightness=0)
    licht2 = Light(device_id="licht2", brightness=0)

    therm1 = Thermostat(device_id="therm1", target_temp=20)
    therm2 = Thermostat(device_id="therm2", target_temp=20)

    # Eine Liste mit den Instanzen bauen
    devices = [licht1, licht2, therm1, therm2]

    # In der Schleife hängen wir jetzt jedes Objekt aus der Liste in unser SmartHome Objekt
    for dev in devices:
        demo_management.register_device(dev)

    # Rückgabe der device_id mit dem getter aus der Device Parentklasse, in einer kleinen List Comprehension...
    return [dev.getinfo() for dev in demo_management.status_report()]

print(init_demo())


meineRoom = Room("N1")
meineRoom.add_new_sensor("sensor Nr:1")
meineRoom.auslesen()