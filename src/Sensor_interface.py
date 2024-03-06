import lib16inpind
import json

class Sensor_Iface:
    def __init__(self):
        self.STACK = 0
        self.CHANNEL_NUMBER = 1
        self.total = 0
        self.prev_sensor_state = self.get_sensor_state()
        self.monitor_event_detect()  # Start monitoring immediately upon initialization

    def monitor_event_detect(self):
        while True:
            current_sensor_state = self.get_sensor_state()
            if not self.prev_sensor_state and current_sensor_state:
                self.sensor_action()  # Call sensor_action if sensor state changes from False to True
            self.prev_sensor_state = current_sensor_state

    def sensor_action(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
            data["CASES"][0] += 1
            print(data)
        with open('data.json', 'w') as file:
            file.write(json.dumps(data, indent=4))
            
        


    def get_sensor_state(self):
        return lib16inpind.readCh(self.STACK, self.CHANNEL_NUMBER) == 1


