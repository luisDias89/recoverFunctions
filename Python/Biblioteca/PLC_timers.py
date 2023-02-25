# Biblioteca PLC_timers @ Luís Dias 2023
# A seguinte biblioteca implementa as seguintes estruturas:
# ======================================================================
# Extended pulse
#     
# Retentive on-delay timer
#
# Switch-off delay
#
# Cyclic timer
# ======================================================================

class timerOFF:
    def __init__(self, valor):
        self.valor = valor
    
    def dobrar_valor(self):
        self.valor *= 2
        
        
class timerON:
    def __init__(self, valor):
        self.valor = valor
    
    def dobrar_valor(self):
        self.valor *= 2

