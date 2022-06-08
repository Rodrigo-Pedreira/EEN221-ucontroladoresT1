from machine import Pin
from time import ticks_ms, ticks_diff


# Constantes
RAIORODA = 0.5
CIRCUNFERENCIA = 2 * 3.1415 * RAIORODA


# Init
tick_anterior = ticks_ms()

hall_interrupt = Pin(14,Pin.IN, Pin.PULL_UP)
hall = False
vel = 0


# Funcoes:
def hall_handler(Pin):
    global hall
    hall = True

def calcular_velocidade():
    global hall
    global vel
    global tick_anterior
    tempogiro = calcular_tempo_giro()
    if hall:
        hall = False
        tick_anterior = ticks_ms()
        vel = round((CIRCUNFERENCIA/tempogiro)*3600, 1)
        return 120 if vel > 120 else vel
    elif (tempogiro > 1000):
        vel = 0
        return 0
    else:
        return 120 if vel > 120 else vel

def calcular_tempo_giro():
    global tick_anterior
    tempo_giro = ticks_diff(ticks_ms(), tick_anterior)
    return tempo_giro

hall_interrupt.irq(trigger=Pin.IRQ_RISING, handler=hall_handler)
