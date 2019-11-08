from brian2 import *
import matplotlib.pyplot as plt
import json
import webbrowser
from subprocess import call
from neuronCharacteristcs import *

start_scope()
##----------------------------------------------------SIMULACAO----------------------------------------------------##
runtime = 200*ms            ##Tempo total de simulacao

                     #Wsyn representa a Matriz do peso de coneccao entre neuronios

Wsyn = [[  0.1, 0, 0, 0.1, 0.2, 0.3, 0, 0, 0],
        [  0, 0.2, 0, 0.2, 0.2, 0.4, 0, 0, 0],
        [  0, 0, 0.3, 0.3, 0.4, 0.6, 0, 0, 0],
        [  0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.1],
        [  0, 0, 0, 0, 0, 0, 0.3, 0.3, 0.2],
        [  0, 0, 0, 0, 0, 0, 0.4, 0.5, 0.7],
        [  0, 0, 0, 0, 0, 0, 0, 0, 0],
        [  0, 0, 0, 0, 0, 0, 0, 0, 0],
        [  0, 0, 0, 0, 0, 0, 0, 0, 0]]

                    #Grupo de Neuronios
N = len(Wsyn)       ##Numero total de neuronios

G = NeuronGroup(N,eqs,threshold='v>Vthreash',reset='v = Vreset',method='euler')
            ##Os neuronios possuem uma tensao de threashold, tensao de reset e as caracteristicas descritas no modulo neuronCharacteristcs

                    #Condicoes iniciais
G.v = 0*volt
G.I = 25*uamp

                    #Sinapses
Syn = Synapses(G, G,model='w : 1',on_pre='Ps_post += w')    ##Modelo de Sinapse simples
Syn.connect(True)                                           ##Conecta todos os neuronios entre si
for i in range(N):                                          ##Aplica os pesos entre as sinapses de acordo com a matriz Wsyn
   for j in range(N):
       Syn.w[i,j] = Wsyn[i][j]


                    #Monitor
StM = StateMonitor(G,['v','Ps'],record=True)
SpM = SpikeMonitor(G)

                    #Rodar

print "Simulando..."
run(runtime)



##----------------------------------------------------VISUALIZACAO----------------------------------------------------##
##-----------------------------A VIZUALIZACAO EH FEITA EM JAVASCRIPT--------------------------------------------------##
data = {}           ##Salva a matrix de pesos em arquivo
data['pesos'] = []
for i in range(N):
    data['pesos'].append(Wsyn[:][i])

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
                    #Plotar graficos
spike_dictionary = SpM.spike_trains()

                    ##Salva os plots como imagens, para o visualizador
filepath = 'images/'
print "Salvando Simulacao ..."
for i in range(N):
    plt.figure("Neuron "+str(i+1))
    plot(StM.t/ms, StM.v[i])
    plot(StM.t/ms, StM.Ps[i])
    xlabel('Time (ms)')
    ylabel('Vmem');
    for t in spike_dictionary[i]:
        axvline(t/ms, ls='--', c='red', lw=3)
    plt.savefig(filepath+'n'+str(i+1)+'.png')
    
print "Simulacao salva! ..."

print "Abrindo Visualizador"

call(["python2.7","startServer.py"])                                        ##Inicia um servidor Web
webbrowser.open_new_tab('http://localhost:8080/networkVisualization.html')  ##Chama o visualizador de dados
