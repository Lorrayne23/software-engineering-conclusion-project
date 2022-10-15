<div align="justify">

# An Are Code Smell Co-occurrences Harmful to Internal Quality Attributes? A Mixed-Method Study

Júlio Martins, Carla Bezerra, Anderson Uchôa, and Alessandro Garcia. 2020. Are Code Smell Co-occurrences Harmful to Internal Quality Attributes? A Mixed-Method Study. In Proceedings of the XXXIV Brazilian Symposium on Software Engineering (SBES '20). Association for Computing Machinery, New York, NY, USA, 52–61.  doi: [10.1145/3422392.3422419](https://doi.org/10.1145/3422392.3422419)



## 1. Fichamento de Conteúdo

 Linhas de Produtos de Software (*SPL*, do inglês *Software Product Line*) consistem em sistemas de *software* que possuem determinado conjunto de funcionalidades em comum na observância a um segmento, logo os componentes de LPS devem ser fácil de serem mantidos. Porém, é indubitável a presença de *code smells* e suas co-ocorrências diante da dimensão de tais *softwares*. Assim, o artigo visa a investigação das relações entre *code smells* denominadas *inter-smells* em relação ao impacto que essas podem gerar a despeito  da qualidade e manutenibilidade. Por meio da seleção de dois LPSs nomeados *MobileMedia* e *Health Watcher*, foram examinados cinco tipos de *code smells* e foram posteriormente realizadas a definação das relações *inter-smells*. Concomitantemente, a refatoração de *code smells* e a comparação de *releases* antes e depois para varificar o impacto em relação a manutenibilidade utilizando métricas.Por fim, obtiveram como resultados, em primeira instância, o estabelecimento do relacionamento direto existente entre a ocorrência de  *Duplicated Code*  e *Long Method*, uma vez o aumento da primeira está condicionado ao aumento da medida da segunda. Ademais, a inspeção de que não ocorreram impactos negativos a manutebnilidade e qualidade dos códigos com a presença de *inter-smells*, além da prorrogação que a métrica  *Lack of Cohesion of Methods* (*LCOM*) deve ser definida como uma das principais métricas no que tange fornecimento  informacional para a manutenibilidade de um sistema.


## 2. Fichamento Bibliográfico 

* _Software Product Line_ (Linha de Produtos de Software) Estratégia utilizada para o desenvolvimento de software que pertençam ao mesmo domínio a partir de reutilização(página 1).
* _Aglomerações de anomalias_ Grupos de elementos de códigos atípicos que podem estar relacionados diretamente ou indiretamente  (página 2).
* _Move Method_ (Método de movimentação) Tipo de refatoração utilizada para mover um método entre classes para remover dependências excessivas (página 2).
* _Relações Inter-smell_ Relação de dependência entre *code smells* (página 2).


## 3. Fichamento de Citações 

* _"descobertas apontam que os engenheiros de aplicação devem se preocupar mais com a coesão das classes na implementação da aplicação, preservando assim a manutenibilidade dos produtos e beneficiando de forma direta a reusabilidade"_
* _"as descobertas deste trabalho sugerem que a métrica LCOM, que mede a coesão de uma classe, é fundamental para qualidade do código e o índice de manutenibilidade nos produtos de uma LPS."_
* _"As coocorrências de code smells conhecidas como Inter-smell não tiveram impacto negativo para a manutenibilidade ou a qualidade do código em releases das LPSs MobileMedia e Health Watcher."_
* _"O número de ocorrências de Duplicated Code aumenta à medida que o número de ocorrências de Long Method também aumenta."_
* _" as operações de refatoração foram feitas de forma automá-tica utilizando a ferramenta JDeodorant [30]. A escolha do code smell a ser removido foi feita de forma aleatória. "_
* _"As LPSs MobileMedia e Health Watcher são medidas com seus respectivos códigos originais, i.e, antes do processo de remoção dos Inter-smell, para que após o processo de remoção dessas coo- corrências, seja medida novamente a qualidade do código dessas LPSs com o objetivo de comparar o código original com o código refatorado para que assim, seja avaliado o impacto dos Inter-smell para a manutenibilidade.."_

<div>
