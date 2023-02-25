# Biblioteca PLC_timers @ Luís Dias 2023
# A seguinte biblioteca implementa as seguintes estruturas:
# ======================================================================
# Extended pulse              ->  extendPulse
#     
# Retentive on-delay timer    ->  timerON
#
# Switch-off delay            ->  timerOFF
#
# Cyclic timer                ->  clockPulse
# ======================================================================

# BrainStorm
# 1º - O utilizador podera adicionar timer segundo um indice
#  - Criar lista em python



class extendPulse:                                     
    def __init__(self):
        pass

class timerON:                                    
    def __init__(self):
        pass

class timerOFF:                                   
    def __init__(self):
        pass
    
    def input(self, bool):
        if bool == True:
            print("Input a 1")
        else:
            print("Input a 0")
        pass
    
    def output(self):
        return 0
    
    def reset(self, bool):
        return 0
    
    def preset_time(self, float):
        return 0
    
    
class clockPulse:                                    
    def __init__(self):
        pass

        
        
        


