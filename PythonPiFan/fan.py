from gpiozero import PWMOutputDevice, CPUTemperature
import configparser
import time

class PiFan(object):

    def __init__(self):
        self.read_settings()
        self.device = PWMOutputDevice(17,initial_value = 1)
        self.temp =CPUTemperature(min_temp = self.minimum_temperature, max_temp = self.maximum_temperature, threshold = self.minimum_temperature)
        self.debug = 1
    def fan_on(self):
        self.device.on()

    def fan_off(self):
        self.device.off()

    def fan_value(self, value):
        self.device.value = value

    def get_temperature(self):
        return self.temp.temperature

    def read_settings(self):
        cfg = configparser.ConfigParser()
        cfg.read('settings.ini')
        cfg.sections()
        self.minimum_temperature = float(cfg['MAIN']['MinimumTemperature'])
        self.maximum_temperature = float(cfg['MAIN']['MaximumTemperature'])
        self.interval = int(cfg['MAIN']['UpdateInterval'])
        self.minimum_fan = int(cfg['MAIN']['MinimumFanSpeed'])/100
        self.maximum_fan = int(cfg['MAIN']['MaximumFanSpeed'])/100
        self.debug = int(cfg['MAIN']['Debug'])

    def get_fan_value_from_temp(self):
        if self.temp.value < self.minimum_fan:
            return self.minimum_fan
        elif self.temp.value > self.maximum_fan:
            return self.maximum_fan
        return self.temp.value

if __name__ == '__main__':
    pifan = PiFan()
    pifan.read_settings()
    if pifan.debug == 1:
        print("Current Settings:")
        print("Fan Update Interval Speed:" + str(pifan.interval))
        print("Maximum Temperature:" + str(pifan.maximum_temperature))
        print("Minimum Temperature:" + str(pifan.minimum_temperature))
        print("Maximum Fan Speed:" + str(pifan.maximum_fan*100))
        print("Minimum Fan Speed:" + str(pifan.minimum_fan*100))
    while 1:
        time.sleep(pifan.interval)
        pifan.fan_value(pifan.get_fan_value_from_temp())
        if pifan.debug == 1:
            print("Current Temperature " + str(round(pifan.temp.temperature,1)) + " | Current Speed " + str(int(pifan.get_fan_value_from_temp() *100))+ "%")
        