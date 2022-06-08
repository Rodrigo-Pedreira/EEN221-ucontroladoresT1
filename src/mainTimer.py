# MicroPython v1.18 on 2022-01-17; Raspberry Pi Pico with RP2040
from utime import sleep_ms
from machine import Timer
import _thread

import displaylcd  as lcd
import sensordht11 as dht
import sensorhall  as hall
import bateria     as bat
import botao       as botao

# Variaveis Global
velocidade = 0

timer_principalNoVel = Timer()
timer_principalVel = Timer()
timer_thread_vel = Timer()


# THREAD velocidade
def thread_vel():
    global velocidade
    def velocidadeAtualizada(nada=None): # sem arg "nada" da warnings
        global velocidade
        velocidade = hall.calcular_velocidade()
    timer_thread_vel.init(mode=Timer.PERIODIC, period=90, callback=velocidadeAtualizada)
# Fim THREAD velocidade


# Funcoes
def tela_principalVel(nada=None): # sem arg "nada" da warnings
    global velocidade
    if(botao.tela):
        return None
    lcd.oled.fill_rect(40, 17, 128, 32, 0)
    lcd.buffer_vel(velocidade)
    lcd.oled.show()

def tela_principalNoVel(nada=None): # sem arg "nada" da warnings
    if(botao.tela):
        return None
    lcd.oled.fill_rect(0, 0, 128, 15, 0)
    lcd.oled.fill_rect(0, 17, 40, 32, 0)
    lcd.buffer_dht(dht.medirDHT11_t_h)
    lcd.buffer_bateria(bat.medir_bateria)
    lcd.oled.show()

def tela_secundaria():
    lcd.clear_display()
    lcd.oled.text("Bem vindo a", 7, 10)
    lcd.oled.text("tela 2 :)", 7, 20)
    lcd.refresh_display()

def iniciarExecucao():
    global timer_principalNoVel
    global timer_principalVel
    lcd.clear_display()
    lcd.buffer_linha_media()
    lcd.oled.show()
    
    tela_principalNoVel()
    tela_principalVel()

    _thread.start_new_thread(thread_vel, ()) # Thread exclusiva para calculo da velocidade

    timer_principalNoVel.init(mode=Timer.PERIODIC, period=5000, callback=tela_principalNoVel)
    timer_principalVel.init(mode=Timer.PERIODIC, period=200, callback=tela_principalVel)

    
def botao_apertado(nada=None):
    if(botao.tela):
        tela_secundaria()
    else:
        lcd.buffer_linha_media()
        tela_principalNoVel()
        tela_principalVel()


# Programa
iniciarExecucao()


# Executar no repl para finalizar a execucao, de fato
#
# timer_thread_vel.deinit()
# timer_principalNoVel.deinit()
# timer_principalVel.deinit()


# TODO:
# - Add botao (usar schedule() ou timer - https://docs.micropython.org/en/latest/reference/isr_rules.html );
# - Contemplar necessidade de um loop (os timers não param apesar de o programa ter "terminado");
# - Testar fluxo de execucao com timer (chama e vai embora ou fica ali?, importante para usar interrupts);