import Biblioteca as lib
import time

teste = lib.timerOFF()

# ==========================================================================================================================================
#     Estrutura de declaração de timerOFF 
#===========================================================================================================================================         
timersOFF =[]                                        # Declaro uma lista de timers

timeroff_0 = 0                                    # Crio um Timer para cada ulitização que pretenda 
timerDoPlacar = 1                                 # . . . . . .
meuNovoTimer = 2                                  # . . . . . .
timernovo3 = 3
# ====================================
# Crie uma nova variavel de timer e a 
# cada variavel incremente o timer 
# timerInicialization
# ====================================
timerInicialization = 4                           # não apagar este ponteiro, adicionar o timer novo no antepenultimo e incrementar o ultimo  

# Inicialização dos timers

for i in range(timerInicialization):
    timersOFF.append(lib.timerOFF())


timersOFF[timeroff_0].set_input(0)
timersOFF[timerDoPlacar].set_input(1)
timersOFF[meuNovoTimer].set_input(True)


timersOFF[timernovo3].set_input(False)
print(timersOFF[timernovo3].output())
time.sleep(2)
print(timersOFF[timernovo3].output())
time.sleep(2)
timersOFF[timernovo3].reset_pulse(True)
timersOFF[timernovo3].set_input(True)
print(timersOFF[timernovo3].output())
time.sleep(2)
print(timersOFF[timernovo3].output())
