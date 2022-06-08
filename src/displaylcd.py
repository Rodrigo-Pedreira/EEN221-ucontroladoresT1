from machine import Pin, SPI
from ssd1306 import SSD1306_SPI

from sensordht11 import medirDHT11_t_h
from sensorhall import calcular_velocidade


# Tamanho das letras no display.
XLETRA = 8
YLETRA = 8

XOLED = 128
YOLED = 32

# Pinos Display.

DC =   Pin(16)
CS =   Pin(17)
SCK =  Pin(18)

MOSI = Pin(19)
RST =  Pin(20)

# Config inicial display.
spi = SPI(0, mosi = MOSI, sck = SCK)
oled = SSD1306_SPI(XOLED, YOLED, spi, DC, RST, CS) # (WIDTH, HEIGHT, spi, dc,rst, cs)
# Estado inicial display.
oled.contrast(255)
oled.fill(0)
oled.show()


#Funcoes:

def clear_display():
    oled.fill(0)
    oled.show()

def refresh_display():
    oled.show()
    oled.fill(0)

def buffer_vel(medida_vel):
    texto = f"{medida_vel} km/h"
    xoffset = XOLED-len(texto)*XLETRA
    yoffset = YOLED-YLETRA
    oled.text(texto, xoffset, yoffset)

def buffer_dht(medirdht11):
    temp, hum = medirdht11()
    texto = f"{temp}C Hum: {hum}%"
    xoffset = XOLED-len(texto)*XLETRA
    yoffset = 0
    oled.text(texto, xoffset, yoffset)
    
def buffer_bateria(medir_bateria):
    xoffset = 0
    yoffset = YOLED-YLETRA
    oled.text(f"{medir_bateria()}%", xoffset, yoffset)
    

def buffer_linha_media():
    oled.hline(0, YOLED//2 , XOLED, 1)



# TESTE:
# def teste_lcd():
#     buffer_vel(calcular_velocidade)
#     buffer_dht(medirDHT11_t_h)
#     buffer_linha_media()
#     refresh_display()
# teste_lcd()

# def pisca_on():
#     oled.fill(1)
#     oled.show()
#     
# def pisca_off():
#     oled.fill(0)
#     oled.show()
