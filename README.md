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
Uma vez que o modelo de Hodgkin-Huxley, composto por equações diferenciais não-lineares, são computacionalmente complexas, é  interessante buscarmos uma simpĺificação das mesmas de modo que,a partir da análise do comportamento das mesmas, possa encontrar um modelo computacionalmente mais simples e que mantenha as características principais descritas pelo modelo original.

É seguindo esse mesmo pensamento que é proposto o modelo _Leak, Integrate and Fire_ (LIF), descrito pelas seguintes equações

<p align="center">
  <img src="https://github.com/ma-ath/SNN-Simulation/blob/master/CodeCogsEqn.gif" title="Equação LIF">
  <br>
  <img src="https://github.com/ma-ath/SNN-Simulation/blob/master/photo_2019-11-12_22-40-02.jpg" width="300" title="Imagem retirada de [2]">
</p>

# Bibliografia & Links Externos
[1] DAYAN,P.;ABBOTT,L.F;Theoretical Neuroscience - Computational and Mathematical Modeling of Neural Systems. Cambridge, 2001

[2] AAMIR, S. A. Mixed-Signal Circuit Implementation of Spiking Neuron Models. Orientador: Prof. Dr. Marc Weber. 2018. Dissertação (Doktors der Ingenieurwissenschaften) - Fakultät für Elektrotechnik und Informationstechnik des Karlsruher Instituts für Technologie (KIT), Karlsruher Instituts für Technologie, 2018.

[3] SAKEMI, Y; MORINO, K. スパイキングニューラルネットワークにおける深層学習: Deep Learning for Spiking Neural Networks. 生産研究, J-STAGE, ano 2019, v. 71, n. 2, p. 159-167, 30 mar. 2019.

[4] https://pt.wikipedia.org/wiki/Modelo_de_Hodgkin-Huxley

[5] https://demonstrations.wolfram.com/MinimalHodgkinHuxleyModelDCStimulus/
