<div align="justify">

# Misbehaviour Prediction for Autonomous Driving Systems

Andrea Stocco, Michael Weiss, Marco Calzana, and Paolo Tonella. 2020. Misbehaviour prediction for autonomous driving systems. In Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering (ICSE '20). Association for Computing Machinery, New York, NY, USA, 359–371. doi: [10.1145/3377811.3380353](https://doi.org/10.1145/3377811.3380353)

## 1. Fichamento de Conteúdo

O crescimento e desenvolvimento de *self-driving cars* promulgou a rápida ascenção evolutiva de Sistemas de Direção Autônomos (ADSs, do inglês *Autonomous Driving Systems*), no que tange o relacionamento entre esses, o segundo através da coleta de dados e do uso de redes neurais determina padrões de atuação. Ademais, esses sistemas complexos de *software* necessitam ser testados de maneira dispendiosa no intuito de obter-se o maior nível de cenários possíveis relacionados a falhas que possam ocorrer durante sua utilização, porém tais testes são custosos quando executados ou não abarcam todo o limitar de ocorrência relacional. O problema ocorre na não previsão de comportamentos possíveis, consequentemente o monitoramento do nível de confiança das redes neurais também é comprometido. O artigo então propõe a criação de uma ferramenta denominada *SelfOracle* que a partir da observância de categorias como *confidence estimation*, *probability of distribution-fitting* e *time series analysis* verifica a confiança em execução e prevê se o sistema se encontra dentro de uma zona de baixa confiabilidade. Como resultado obtém-se a efetividade da ferramenta proposta em antecipar comportamentos críticos com o intuito de validar maior segurança, seja em relação a limites de velocidade ou colisões.


## 2. Fichamento Bibliográfico 

* _Autoencoders_ (Auto-codificadores) composto por um codificador e um decodificador, tem a função de reconstruir seu próprio *input* (página 360).
* _Safety-critical misbehaviours_ (comportamentos críticos de segurança) comportamentos relacionados a possíveis colisões e velocidades limite que se tornam críticas em relação ao fator de segurança (página 361).
* _Unexpected Context Generator_ (gerador de contexto inesperado) responsável por gerar uma lista de cenários de possíveis ocorrências inesperadas quando um veículo se encontra em modo autônomo (página 364).

## 3. Fichamento de Citações 

* _"We evaluate our framework on three existing DNN-based SDCs: Nvidia’s DAVE-2 [9], Epoch [41], and Chauffeur [40]. We choose these models because they are robust SDC models and they are publicly available, thus they can be trained and evaluated on the simulator."_
* _"First, we developed a method to gradually inject unseen conditions during autonomous mode (i.e., conditions diverse from the training mode’s defaults). The first condition deals with illumination. Our extension of the simulator can gradually change the lightning condition of the track, simu- lating the passage between day and night (day/night cycle)."_
* _"We use the input validation technique of Deep- Road [55] as baseline for SelfOracle. Due to the unavailability of an open-source version of such technique, we implemented of our own version based on the authors’ description, which is pub- licly available in our replication package [45]."_
* _"Overall, LSTM and VAE are the best performing reconstructors on the AUC-PRC and AUC-ROC metrics. Columns 12 and 21 (Nomi- nal/FPR) show FPR under conditions similar to those of the training set. Values are almost always near to zero and occasionally even equal to zero (this is indicated by omitting the decimals) across the variants of SelfOracle."_
* _"We used a limited number of self-driving sys- tems in our evaluation, as well as tracks, which pose a threat in terms of generalizability of our results. We tried to mitigate this threat by choosing popular real-world SDC models which achieved competitive scores in the Udacity challenge."_
* _"Our tool SelfOracle was able to anticipate by several seconds many potentially safety-critical misbehaviours, such as out-of-bound episodes or collisions, with a low false alarm rate, outperforming the input validator of DeepRoad."_

<div>