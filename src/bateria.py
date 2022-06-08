from machine import Pin, ADC

bat = ADC(26)

# 9V = ~~ 2.948V = ~~ 59614
# 8V = ~~ 2.608V = ~~ 53004

# R1 = 1K  = ~~ 983 (junto com Vcc)
# R2 = 470 = ~~ 475 (junto com GND)

BATMAX = 59614               # 9V = ~~ 2.948V = ~~ 59614
BATOFFMIN = 53004            # 8V = ~~ 2.608V = ~~ 53004
BATDIFF = BATMAX - BATOFFMIN #                  ~~  6610

def medir_bateria():
    lvl = round( (bat.read_u16() - BATOFFMIN)/BATDIFF, 2)
    lvl = 0 if lvl < 0 else lvl
    lvl = 1 if lvl > 1 else lvl
    return int(lvl*100)

def teste_bateria():
    print(f"lvl {medir_bateria()}%")
    print(f"read {bat.read_u16()}")


# teste_bateria()