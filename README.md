# SNN-Simulation

Redes Neurais Pulsadas - SNN (do ingles Spiking Neural Networks) são uma arquitetura de redes neurais artificiais baseadas nos sistemas neuronal-biológicos, e que visam assim, imitar o funcionamento das redes neurais biológicas. Esse grupo de redes neurais incorpora em sua estrutura a ideia da codificação da informação no domínio do tempo, através dos chamados "Códigos de Pulsos", e do uso de um conjunto de equações de estado que governam o funcionamento individual de cada célula da rede.
 
# Funcionamento Neuronal: O Modelo de Hodgkin-Huxley
 
O entendimento das características básicas de um neurônio pode ser remetido à 1952, quando a dupla de cientistas britânicos _Alan Hodgkin_ e _Andrew Huxley_ descreveram pela primeira vez um grupo de equações diferenciais que governavam as características fisico-químicas dos neurônios de uma lula, em seu famoso paper _"A quantitative description of membrane current and its application to conduction and excitation in nerve"_, o que lhes rendeu o Prêmio Nobel de 1963 _"por suas descobertas sobre os mecanismos iônicos envolvidos na excitação e inibição nas porções periférica e central da membrana das células nervosas"_. Nesse mesmo estudo, Hodgkin e Huxley ao descrever o conjunto de equações, nos introduz a um modelo eletrônico com os quais é possível simular o comportamento do neurônio, o qual ficou conhecido por **Modelo de Hodgkin-Huxley**.
 
 O modelo eletrônico de Hodgking-Huxley é descrito a seguir:
 
 <p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Hodgkin-Huxley_-_PT.svg" title="Modelo Eletrônico de Hodgkin-Huxley">
  <br>
  <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/8fde652312d9692d346ee7150c362c7679bb7e3f">
  <br>
  <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/057155f00703e829696e069d0c66131e2c02e453">
  <br>
  <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/e721bc5c172643c1ea4c02507e593f3950561b6b">
  <br>
  <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/e2d6115fcbd65351edd5b8176fc192cddd4a49f4">
  <br>
</p>

Esse conjunto de equações têm por variável principal a _"Tensão de membrana"_ (Vm) do neurônio, que é a variável de estado básica do sistema. As soluções para as equações descrevem um **comportamento pulsado** do sistema, ou seja: Os sinais de comunicação (_sinapses_) entre os neurônios são também sinais pulsados.


# Uma simplificação: O modelo "Leak, Integrate and Fire"
Uma vez que o modelo de Hodgkin-Huxley, composto por equações diferenciais não-lineares, é computacionalmente bastante complexo, é  interessante buscarmos uma simpĺificação das mesmas de modo que, a partir do comportamento ddo modelo completo, seja possivel extrair um modelo computacionalmente mais simples e que mantenha as principais características descritas pelo modelo original.

Seguindo esse pensamento, nos é proposto o modelo _Leak, Integrate and Fire_ (LIF), descrito pelas seguintes equações

<p align="center">
  <img src="https://github.com/ma-ath/SNN-Simulation/blob/master/Readme/CodeCogsEqn.gif" title="Equação LIF">
  <br>
  <img src="https://github.com/ma-ath/SNN-Simulation/blob/master/photo_2019-11-12_22-40-02.jpg" width="300" title="Imagem retirada de [2]">
</p>

Nesse modelo, passa a existir uma chamada **"Tensão de Limiar"**: Quando a variável interna do sistema (Tensão de Membrana) atinge esse valor, ocorre instantaneamente um pulso, o que é descrito pelos seguites passos:
* A tensão de membrana _"salta"_ instantaneamente para uma tensão de disparo
* Logo em seguida, a tensão de membrana retorna instantaneamente a um valor mais baixo, chamado _"Tensão de Reset"_
* O neurônio pode ou não entrar em um período "refratorio", onde a tensão de membrana permanecerá inalterada

<p align="center">
  <img src="https://github.com/ma-ath/SNN-Simulation/blob/master/Readme/Simulation-of-LIF-Model-of-SNN.png" title="Equação LIF - Retirada de [4]">
</p>

Uma vez que a tensão de membrana salta "instantâneamente" ao atingir sua "Tensão de Limiar", podemos imaginá-la como um _impulso de Dirac_, e é através de tais impulsos que o neurônio irá enviar informações para os demais neurônios.  

# Sinapses

_Sinapse_ é o nome dado às regiões de contato entre um neurônio e o meio exterior (outro neurônio, uma célula muscular, etc), e é aonde ocorre a propagação da informação entre neurônios através de processos bioquímicos. Os principais contatos sinápticos são do tipo axo-somático, axo-dendrítico, neuroefetor e neuromuscular [6]. Do ponto de vista computacional, é por meio de sinapses que o as sinais processados em um neurônio são transmitidos para outras células.

Físicamente, o efeito que as sinápses geram no comportamento celular é o de aumentar ou diminuir o _potencial da membrana pós-sináptico_: Uma **resposta excitatória** despolariza o interior da célula, o que gera o aumento do potencial da membrana local. Já uma **resposta inibitória** hiperpolariza o interior celular, o que diminui o potencial de membrana local. [5]

No modelo RC do LIF apresentado anteriormente, podemos modelar o efeito de uma sinápse no potencial de membrana _Vmem_ através da adição de uma _condutância sináptica_ controlada _gs_, conectada entre o potencial Vmem e um potencial sináptico _Vs_.

Essa condutânia _gs_ é igual a multiplicação de três termos [5][1, Pág. 169,180]:

<p align="center">
  <img src="https://github.com/ma-ath/SNN-Simulation/blob/master/Readme/gs_code.gif" title="Equação de Resposta Sináptica - Retirada de [5]">
</p>

* _gsmax_: máxima condutância assumida por _gs_
* _Prel_:  Probabilidade de haver uma resposta (liberação de neurotransmissores) dada uma resposta recebida
* _Ps_:    Probabilidade de haver a abertura de canais pós-sinapticos (= fração de canais abertos)

Por simplicidade, podemos assumir que _Prel = 1_, ou seja, há a liberação de neurotransmissores todas as vezes que uma resposta é recebida.

Podemos modelar os efeitos de _Ps_ a partir de um modelo cinético, onde os canais os canais fecham e abrem, respectivamente, à taxas _α_s_ e _β_s_:

<p align="center">
  <img src="https://github.com/ma-ath/SNN-Simulation/blob/master/Readme/ps_code.gif" title="Equação do Comportamento do Canal - Retirada de [5]">
</p>

A solução desse sistema para um _Impulso de Dirac_ descreve _Ps(t)_ como uma função exponencial. Podemos dessa forma, imaginarmos esta equação como um filtro sináptico: Cada sinal sinaptico recebido será filtrado por ele, ou, em outras palavras, um _trem de impulsos_ sinápticos na entrada do sistema descreverá uma resposta sináptica no sistema (através da condutância sináptica _gs_) dada por uma **Integral de convolução** do trem de impulsos com a resposta ao impulso do sistema, representada por:

<p align="center">
  <img src="https://github.com/ma-ath/SNN-Simulation/blob/master/Readme/gbt_code.gif" title="Filtro Sinaptico (Tempo) - Retirada de [5]">
 <br>
  <img src="https://github.com/ma-ath/SNN-Simulation/blob/master/Readme/rhob_code.gif" title="Trem de Pulso Sinaptico - Retirada de [5]">
</p>

Na equação:
* _K(t)_:   É a resposta ao impulso do filtro (uma resposta exponencial decrescente)
* _ρb(t)_:  Trem de impulsos sinápticos, representa uma resposta sináptica recebida de outro neurônio
* _gb,max_: É a máxima condutância assumida por _gb(t)_
* _gb(t)_:  É a condutância sinaptica do modelo eletrônico LIF


# Bibliotecas e Dependências

Principais Dependências:
* Python (3.5.2)
* Brian2 - https://brian2.readthedocs.io/en/stable/

Outras bibliotecas utilizadas:
* Jquery-3.5.1 - https://jquery.com
* Vis.JS - https://visjs.org
* Json
* matplotlib
* webbrowser
* subprocess
* SimpleHTTPServer
* SocketServer

(As bibliotecas Jquery e Vis.JS já estão incluidas na pasta /js)

# Bibliografia & Links Externos
[1] DAYAN,P.;ABBOTT,L.F;Theoretical Neuroscience - Computational and Mathematical Modeling of Neural Systems. Cambridge, 2001

[2] AAMIR, S. A. Mixed-Signal Circuit Implementation of Spiking Neuron Models. Orientador: Prof. Dr. Marc Weber. 2018. Dissertação (Doktors der Ingenieurwissenschaften) - Fakultät für Elektrotechnik und Informationstechnik des Karlsruher Instituts für Technologie (KIT), Karlsruher Instituts für Technologie, 2018.

[3] SAKEMI, Y; MORINO, K. スパイキングニューラルネットワークにおける深層学習: Deep Learning for Spiking Neural Networks. 生産研究, J-STAGE, ano 2019, v. 71, n. 2, p. 159-167, 30 mar. 2019.

[4] https://www.researchgate.net/figure/Simulation-of-LIF-Model-of-SNN_fig1_316284143

[5] Aulas de Neurociência Computacional - https://www.coursera.org/learn/computational-neuroscience/

[6] Marcus Lira Brandão (2008). As bases biológicas do comportamento. Introdução à neurociência. São Paulo: E.P.U. 244 páginas. ISBN 8512406305

[7] https://pt.wikipedia.org/wiki/Modelo_de_Hodgkin-Huxley

[8] https://demonstrations.wolfram.com/MinimalHodgkinHuxleyModelDCStimulus/
