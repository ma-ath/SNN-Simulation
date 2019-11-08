from brian2 import *

##----------------------------------------------------SIMULACAO----------------------------------------------------##
##Nesse arquivo estao definidas todas as caracteristicas que um neuronio possue, tanto as constantes quanto sua ---##
##---Equacao caracteristica----------------------------------------------------------------------------------------##
    #--Definicao de Constantes

C = 20*ufarad               ##Capacitancia 
vleak = -70*mvolt           ##Tensao de Leak
gleak = 0.001*siemens       ##Condutancia de Leak
vsyn = 0*mvolt              ##Tensao de Sinapse
gsmax = 0.001*siemens       ##Maxima Condutancia de Sinapse
Prel = 1                    ##Probabilidade de liberacao de Neurotransmissores ao receber uma sinapse(Assumido 100%)
alpha = 0.5                 ##Probabilidade de Abertura de canais ao receber uma sinapse
beta = 1-alpha              ##Probabilidade do fechamento de canais ao receber uma sinapse
tausym = 10*msecond         ##Constante de tempo de sinapse

Vthreash = -54*mvolt        ##Tensao de threashold, na qual e enviada uma sinapse
Vreset = -80*mvolt          ##Tensao de reset, setada apos uma sinapse

    #--Equacao carateristica dos neuronios
#####################################################################
#   Equacao 1: Lei de Kirchoff para a tensao de membrana v          #
#   Equacao 2: Equacao que descreve a condutancia de sinapse gsyn   #
#   Equacao 3: Equacao que descreve o comportamento de Ps           #
#              (Probabilidade de abertura de canais pos-sinapticos) #
#              (= fracao dos canais abertos)                        #
#   Equacao 4: Wsyn: Peso da conexao                                #
#   Equacao 5: I = corrente de estimulacao                          #
#####################################################################

eqs = '''
dv/dt = -(gleak*(v - vleak))/C -(gsyn*(v - vsyn))/C+ I/C : volt
gsyn = gsmax*Prel*Ps : siemens
dPs/dt = (alpha*(1-Ps)-beta*Ps)/tausym : 1
I : amp
'''
