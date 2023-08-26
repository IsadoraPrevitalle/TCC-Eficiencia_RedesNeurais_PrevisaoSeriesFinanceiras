Este projeto tem por finalidade analisar a eficácia de alguns algoritmos de previsão.

# Bibliotecas e métodos utilizados
Utilizou-se das bibliotecas numpy, pandas, seaborn e matplotlib.pyplot para realizar uma análise e visualização da base de dados retida do Censo, que traz informações sobre imóveis, seus cômodos, quartos e valores por quarteirão.

A biblioteca numpy é muito utilizada para fornecer funções matemáticas e estatísticas no uso de arrays.

A biblioteca pandas é muito utilizada para fornecer estruturas e ferramentas para manipulação, limpeza, análise e visualização dos dados.

A biblioteca Seaborn é principalmente utilizada na visualização de dados através de gráficos estatísticos.

E a biblioteca Matplotlib.pyplot é utilizada para criação de visualizações criativas ao fornecer uma grande flexibilidade para criação de gráficos personalizados.

Para realizar a análise inicial da base de dados, utilizou-se do método 'describe(include='all')' para obter um resumo estatístico com a contagem, média, desvio padrão, quartis e valores máximo e mínimo da base.

Além disso, utilizou-se a biblioteca sweetviz para gerar um relatório automático, a fim de auxiliar no entendimento e visualização da distribuição dos dados e possíveis padrões.

Aproveitou-se também nesse processo inicial de um gráfico de calor para identificar a correlação das variáveis, que variam de -1 a 1.

# Algoritmos utilizados
Foi verificado o processo de predição utilizando-se os algoritmos do Scikit-learn, que é uma biblioteca para aprendizado de máquina, juntamente com a classe KNR, que tem como base a regressão para prever um valor com base em exemplos de treino. Também utilizou-se o train_test_split, que é uma função do módulo sklearn.model_selection, que tem como base dividir os dados em um conjunto de testes e validação para treinamento do modelo de teste e predição do de validação.

A Árvore de Decisão (DecisionTreeRegressor) tem como funcionamento básico dividir repetidamente os dados buscando a melhor maneira de separar as observações de acordo com os valores das características.

E o modelo de florestas aleatórias (Random Forests) tem como base em seu funcionamento ser composto por várias árvores de decisões individuais construídas a partir de uma amostra aleatória do conjunto de dados original, onde durante sua construção são consideradas apenas um subconjunto aleatório das características disponíveis.

Para verificar a média de erros absolutos dos algoritmos de previsão, foi utilizada a função mean_absolute_error.

A linha de teste foi baseada na escolha do modelo, seguindo o treinamento, a realização da predição e, então, a validação.

No final desse breve projeto, conseguimos avaliar como os diferentes modelos de previsão podem se comportar ao analisar uma base de dados. Fica claro que seus parâmetros são um grande diferencial ao executar esses modelos, afinal são eles que definem as bases.
