from machine import Pin, Timer
from micropython import schedule

import displaylcd as lcd


botao_interrupt=Pin(27,Pin.IN, Pin.PULL_UP)
tela = False
timer = Timer()


def handle_interrupt(Pin):
    from mainTimer import botao_apertado
    global tela
    if(not botao_interrupt.value()):
        tela = not tela
        schedule(botao_apertado,0)

def debounce(pin):
    timer.init(mode=Timer.ONE_SHOT, period=40, callback=handle_interrupt)

botao_interrupt.irq(trigger=Pin.IRQ_FALLING, handler=debounce)
 
# def teste():
#     if(botao):
#         lcd.pisca_on()
#         botao = False
#     else:
#         lcd.pisca_off()
# teste()
