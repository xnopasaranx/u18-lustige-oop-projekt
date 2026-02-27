# importe der Klassen aus den externen Modulen

from management import SmartHome
from beleuchtung import Light
from klima import Thermostat

from security import AlarmSystem
from sensorik import Room

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
    ret_liste = []
    for dev in demo_management.status_report():
        ret_liste.append(dev.getinfo())

    return ret_liste

print(init_demo())

def init_alarm_demo():
    # Raum instanziieren
    meineRoom = Room("N1")

    # 3 Sensoren zum Test hinzufügen
    meineRoom.add_new_sensor("sensor Nr:1")
    meineRoom.add_new_sensor("sensor Nr:2")
    meineRoom.add_new_sensor("sensor Nr:3")

    # hier kriegen wir nun eine Testausgabe
    meineRoom.auslesen()

    # Ein neues Alarmsystem instanziieren
    alarm_sys = AlarmSystem(security_level=5)
    
    # Jeden Sensor aus dem Raum durchgehen
    for sensor in meineRoom.get_sensors():
        # jede Sensor Instanz zu Alarm System hinzufügen
        alarm_sys.add_external_sensors(sensor)
    
    # Daten ausgeben um zu testen ob das alles funktioniert
    print(alarm_sys.get_active_sensors())
    print(alarm_sys.get_security_level())
    print(alarm_sys.trigger_alarm())

# init_alarm_demo()