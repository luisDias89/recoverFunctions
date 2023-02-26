# Biblioteca PLC_timers @ Luís Dias 2023
# A seguinte biblioteca implementa as seguintes estruturas:
# ======================================================================
# Extended pulse              ->  extendPulse
#     
# Retentive on-delay timer    ->  timerON
#
# Switch-off delay            ->  timerOFF
#             /``|
#            /   |    /| 
#           /    |   / | 
# _________/     |__/  |
# _______________|``|__            
# ________|```|_____|``|
# ________|`````````|__|``|__|```````|
#
# Cyclic timer                ->  clockPulse
# ======================================================================

# BrainStorm
# 1º - O utilizador podera adicionar timer segundo um indice
#  - Criar lista em python

"""
Duas funções de temporização, a tic() guarda o tempo no momento em que ela é chamada
a função toc() retorna o tempo entre o tic() e o toc() 
"""

from time import time as Time

#           ================ Extend PULSE =========================
#               ****************************************
#
#              IMPLEMENTA A FUNÇÃO DE PLC DE Extend PULSE
#           ==================================================

class extendPulse:                                     
    # Memorias do timer
    _inputVal = False                           # Inicia o _inputVal = False    
    _resetVal = False                           # Inicia o _resetVal = False
    _start = 0                                  # variavel auxiliar do TIC/TOC
    _elapsedTime = 0.0                          # Tempo de _elapsedTime
    _preset_timeVal = 1.0                       # _preset_timeVal inicial = 1.0 segundos
    _triger         = False                     # A contagem só é valida quanto o disparao está a 1
    
    def __init__(self):
        self._tic()
        self._elapsedTime = self._preset_timeVal # Garante que a saida começa em 0
    
    def _tic(self):
        self._start = Time()

    def _toc(self):
        delta_t = Time() - self._start
        #print("Elapser ime is " + str(delta_t) + " second.")
        return delta_t
                                     
    def input_pulse(self):
        """Input pulse

        The input pulse is active when there is no active reset
        """
        
        if self._resetVal == False:                     # e se não estiver ativo o reset
            self._triger=True                           # então abilito o triger que inicia a contagem
            self._tic()                                 # e marca o inicio da contagem
        self._inputVal= False                           # coloco sempre o input a falso
        
    
    def get__elapsedTime(self):
        """Returns the counting time

        Returns:
            Returns the time elapsed since the start of the pulse, when it reaches the preset_time, stops the time counter
        """
        self._elapsedTime =self._toc()
        if self._resetVal == True or self._triger==False:   # Se o reset time estiver a 1, então retorna 0.0, ou seja está em estado de reset. não existe contagem
            self._elapsedTime = 0.0
            return self._elapsedTime
        else:
            self._elapsedTime = self._toc()
            if self._elapsedTime >= self._preset_timeVal:
                return self._preset_timeVal                      # Se o tempo estourou devolte o tempo de preset_time
            else:
                return self._elapsedTime                         # Caso contrario devolve o tempo que passou desde a marcação do tic
    
    
    def set_input(self, bool):
        """Permanently forces the input to True or False
        
            If True : If there is no reset, then I can start counting. IF: False, set inputVal to zero 
        """
        
        if bool == True and self._inputVal==False:           # Deteta borda de subida então
            if self._resetVal == False:                      # Se não houver reset, então posso iniciar contagem
                self._triger = True                  
                self._tic()                                      # e marca o tempo inicial do contador
            self._inputVal= True                             # se o utilizador pedir para colocar o input a 1, faz set do input a 1
        elif bool == False and self._inputVal==True:         # Deteta borda de descida então:
            self._inputVal= False
             
      
    def output(self):
        """output of the timerOFF

        If there is no reset or counting permission, or if the elapsed time value is 
        greater than the resetTime, then the output is False. Otherwise, the output 
        is True, and the reason is that it is within the counting time
        """
        # Calcula o novo elapseTime
        self._elapsedTime=self._toc()
        if self._resetVal == True or self._triger == False :    # Se tiver um reset ou não tiver permisão de contagem então
            return False                                        # a saida é sempre falsa
        elif self._elapsedTime >= self._preset_timeVal:         # senão se o tempo de contagem for superior ou igual ao reset_time, faz a função de timeOFF e a saida vai a zero
            return False
        else:
            return True                                         # Caso contrario retorna verdadeiro, porque esta na janela de contagem
    
    def reset_pulse(self, bool):
        """Reset pulse
        On the reset pulse, the output is turned off and counting only resumes when there is a new rising edge on the input
        """
        if bool == True: 
            self._triger = False                                # Um pulso de reset é o mesmo que colocar a contagem a Falso
                                                                # e só quando uma nova borda de subida é inicializada é que existe nova contagem
    
    def set_reset(self, bool):
        """Assigns a state to the Reset.

        If the reset is set to false, a new counting will only start when there is a new rising edge on the input
        """
        if bool == True:                                        # Se o pedido por para reset então
            self._resetVal = True                                   # O timer fica em estado de reset
            self._triger = False                                    # Garante que quando o reset vier a Falso, não inicia contagem
        else:                                                   # Senão
           self._resetVal= False                                    # Desbloqueia o reset
            
    
    def set_presetTime(self, preset_time):
        """Insert preset time (float) in seconds
           When the counting time is inputted, the output goes to zero
        """
        self._triger = False                                    # Garante que a saida vai a zero
        self._preset_timeVal = preset_time                      # Atribui o novo tempo de contagem


#           ================ TIME ON =========================
#               ****************************************
#
#              IMPLEMENTA A FUNÇÃO DE PLC DE TIMER ON DELAY
#           ==================================================

class timerON:                                    
        
    # Memorias do timer
    _inputVal = False                           # Inicia o _inputVal = False    
    _resetVal = False                           # Inicia o _resetVal = False
    _start = 0                                  # variavel auxiliar do TIC/TOC
    _elapsedTime = 0.0                          # Tempo de _elapsedTime
    _preset_timeVal = 1.0                       # _preset_timeVal inicial = 1.0 segundos
    _triger         = False                     # A contagem só é valida quanto o disparao está a 1
    
    def __init__(self):
        self._tic()
        self._elapsedTime = self._preset_timeVal # Garante que a saida começa em 0
    
    def _tic(self):
        self._start = Time()

    def _toc(self):
        delta_t = Time() - self._start
        #print("Elapser ime is " + str(delta_t) + " second.")
        return delta_t
                                     
    def input_pulse(self, bool):
        """Input pulse

        The input pulse is active when there is no active reset
        """
        
        if self._resetVal == False:                     # e se não estiver ativo o reset
            self._triger=True                           # então abilito o triger que inicia a contagem
            self._tic()                                 # e marca o inicio da contagem
        self._inputVal= False                           # coloco sempre o input a falso
    
    def get__elapsedTime(self):
        """Returns the counting time

        Returns:
            Returns the time elapsed since the start of the pulse, when it reaches the preset_time, stops the time counter
        """
        self._elapsedTime = self._toc()
        if self._resetVal == True or self._triger==False:   # Se o reset time estiver a 1, então retorna 0.0, ou seja está em estado de reset. não existe contagem
            self._elapsedTime = 0.0
            return self._elapsedTime
        else:
            self._elapsedTime = self._toc()
            if self._elapsedTime >= self._preset_timeVal:
                return self._preset_timeVal                      # Se o tempo estourou devolte o tempo de preset_time
            else:
                return self._elapsedTime                         # Caso contrario devolve o tempo que passou desde a marcação do tic
    
    def set_input(self, bool):
        """Permanently forces the input to True or False
        
            If True : If there is no reset, then I can start counting. IF: False, set inputVal to zero 
        """
        if bool == True and self._inputVal==False:           # Deteta borda de subida então:
            if self._resetVal == False:                      # Se não houver reset, então posso iniciar contagem
                self._triger = True                              # habilita a contagem, que é colocada a zero no inicio ou nos resets
                self._tic()                                      # e marca o tempo inicial do contador
            self._inputVal= True                             # se o utilizador pedir para colocar o input a 1, faz set do input a 1
        elif bool == False and self._inputVal==True:         # Deteta borda de descida então:
            self._inputVal= False
      
    def output(self):
        """output of the timerON

        If there is no reset or counting permission, or if the elapsed time value is 
        greater than the resetTime, then the output is True. Otherwise, the output 
        is False.
        """
        # Calcula o novo elapseTime
        self._elapsedTime=self._toc()
        if self._resetVal == True or self._triger == False :    # Se tiver um reset ou não tiver permisão de contagem então
            return False                                        # a saida é sempre falsa
        elif self._elapsedTime >= self._preset_timeVal:         # senão se o tempo de contagem for superior ou igual ao preset_timeVal, n a função de timeON a saida vai a 1
            return True
        else:
            return False                                         # Caso contrario retorna Falso, porque esta na janela de contagem ainda
    
    def reset_pulse(self, bool):
        """Reset pulse
        On the reset pulse, the output is turned off and counting only resumes when there is a new rising edge on the input
        """
        if bool == True: 
            self._triger = False                                # Um pulso de reset é o mesmo que colocar a contagem a Falso
                                                                # e só quando uma nova borda de subida é inicializada é que existe nova contagem
    
    def set_reset(self, bool):
        """Assigns a state to the Reset.

        If the reset is set to false, a new counting will only start when there is a new rising edge on the input
        """
        if bool == True:                                        # Se o pedido for para reset então
            self._resetVal = True                                   # O timer fica em estado de reset
            self._triger = False                                    # Garante que quando o reset vier a Falso, não inicia contagem
        else:                                                   # Senão
           self._resetVal= False                                    # Desbloqueia apenas o reset, e o triger de contagem tem que vir de um pulso no IN
            
    
    def set_presetTime(self, preset_time):
        """Insert preset time (float) in seconds
           When the counting time is inputted, the output goes to zero
        """
        self._triger = False                                    # Garante que a saida vai a zero, só com novo pulso no in é que a saida vai a 1
        self._preset_timeVal = preset_time                      # Atribui o novo tempo de contagem




#           ================ TIME OFF =========================
#               ****************************************
#
#              IMPLEMENTA A FUNÇÃO DE PLC DE TIMER OFF DELAY
#           ==================================================

class timerOFF():
            
    # Memorias do timer
    _inputVal = False                           # Inicia o _inputVal = False    
    _resetVal = False                           # Inicia o _resetVal = False
    _start = 0                                  # variavel auxiliar do TIC/TOC
    _elapsedTime = 0.0                          # Tempo de _elapsedTime
    _preset_timeVal = 1.0                       # _preset_timeVal inicial = 1.0 segundos
    _triger         = False                     # A contagem só é valida quanto o disparao está a 1
    
    def __init__(self):
        self._tic()
        self._elapsedTime = self._preset_timeVal # Garante que a saida começa em 0
    
    def _tic(self):
        self._start = Time()

    def _toc(self):
        delta_t = Time() - self._start
        #print("Elapser ime is " + str(delta_t) + " second.")
        return delta_t
                                     
    def input_pulse(self):                            
        """Input pulse

        The input pulse is active when there is no active reset
        """
        if self._resetVal == False:                     # e se não estiver ativo o reset
            self._triger=True                           # então abilito o triger que inicia a contagem
            self._tic()                                 # e marca o inicio da contagem
        self._inputVal= False                           # coloco sempre o input a falso, pois é um pulso
    
    def set_input(self, bool):
        """Permanently forces the input to True or False
        
            Detects rising and falling edges, if it's a falling edge and there's
            no active reset, then it starts counting
        """
        if bool == True and self._inputVal==False:           # Deteta borda de subida então:
            
            self._inputVal= True                             # se o utilizador pedir para colocar o input a 1, faz set do input a 1
        elif bool == False and self._inputVal==True:         # Deteta borda de descida então:
            if self._resetVal == False:                      # Se não houver reset, então posso iniciar contagem
                self._triger = True                              # habilita a contagem, que é colocada a zero no inicio ou nos resets
                self._tic()                                      # e marca o tempo inicial do contador
            self._inputVal= False
    
    def get__elapsedTime(self):
        """Returns the counting time

        Returns:
            Returns the time elapsed since the start of the pulse, when it reaches the preset_time, stops the time counter
        """
        self._elapsedTime = self._toc()
        if self._resetVal == True or self._triger==False:   # Se o reset time estiver a 1, então retorna 0.0, ou seja está em estado de reset. não existe contagem
            self._elapsedTime = 0.0
            return self._elapsedTime
        else:
            self._elapsedTime = self._toc()
            if self._elapsedTime >= self._preset_timeVal:
                return self._preset_timeVal                      # Se o tempo estourou devolte o tempo de preset_time
            else:
                return self._elapsedTime                         # Caso contrario devolve o tempo que passou desde a marcação do tic
    
    def output(self):
        """output of the timerOFF

        If the timer is in reset or counting is disabled, the output is 0. 
        Otherwise, if the input is 1, then the output is 1; else if the counter
        hasn't reached the end yet, the output is True; otherwise, the output is 0
        """
        # Calcula o novo elapseTime
        self._elapsedTime=self._toc()
        
        if self._resetVal == True :    # Se tiver um reset 
            return False                                                            # a saida é sempre falsa
        elif self._inputVal == True:
            return True
        elif (self._elapsedTime <= self._preset_timeVal) and self._triger == True:   # senão se o tempo de contagem for superior ou igual ao preset_timeVal, n a função de timeON a saida vai a 1
            return True
        else:
            return False                                         # Caso contrario retorna Falso, porque esta na janela de contagem ainda
    
    def reset_pulse(self):
        """Reset pulse
        On the reset pulse, the output is turned off and counting only resumes when there is a new rising edge on the input
        """
        self._triger = False                                    # Garante que quando o reset vier a Falso, não inicia contagem
                                                                       
    
    def set_reset(self, bool):
        """Assigns a state to the Reset.

        If the reset is set to false, a new counting will only start when there is a new rising edge on the input
        """
        if bool == True:                                        # Se o pedido for para reset então
            self._resetVal = True                                   # O timer fica em estado de reset
            self._triger = False                                    # Garante que quando o reset vier a Falso, não inicia contagem
        else:                                                   # Senão
           self._resetVal= False                                    # Desbloqueia apenas o reset, e o triger de contagem tem que vir de um pulso no IN
            
    
    def set_presetTime(self, preset_time):
        """Insert preset time (float) in seconds
           When the counting time is inputted, the output goes to zero
        """
        self._triger = False                                    # Garante que a saida vai a zero, só com novo pulso no in é que a saida vai a 1
        self._preset_timeVal = preset_time                      # Atribui o novo tempo de contagem




#           ================ CLOCK PULSE =========================
#               ****************************************
#
#              IMPLEMENTA A FUNÇÃO DE PLC DE CLOCK PULSE
#           ==================================================

class clockPulse:                                    
    def __init__(self):
        pass

        
        
        


