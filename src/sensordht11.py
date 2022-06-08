from machine import Pin
# from utime import sleep_ms

from dht import DHT11


# Sensor DHT11 config
DHT11PIN = Pin(0, Pin.IN, Pin.PULL_UP)
sensor = DHT11(DHT11PIN)


# Funcoes
def medirDHT11_t_h():
    sensor.measure()
    return sensor.temperature(), sensor.humidity()


#  TESTE:
# def printarDHT11(sleep_time=2000):
#     sensor.measure()
#     print(f"Temperature: {sensor.temperature()}°C\nHumidity: {sensor.humidity()}%\n--------------\n")
#     sleep_ms(sleep_time)
# while True:
#     printarDHT11()