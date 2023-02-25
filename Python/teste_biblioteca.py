import Biblioteca as lib

# ==========================================================================================================================================
#     Estrutura de declaração de timerOFF 
#===========================================================================================================================================         
timers =[]                                        # Declaro uma lista de timers

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
    timers.append(lib.timerOFF())


timers[timeroff_0].input(0)
timers[timerDoPlacar].input(1)
timers[meuNovoTimer].input(True)
timers[timernovo3].input(False)