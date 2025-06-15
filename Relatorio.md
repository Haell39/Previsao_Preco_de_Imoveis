
## Relatório de Projeto: Previsão de Valores de Imóveis na Califórnia

Este projeto demonstra minhas habilidades em **análise de dados, engenharia de features e machine learning** aplicadas à construção de um modelo preditivo para **estimar o valor mediano de casas na Califórnia**.

 **1. Processamento e Exploração de Dados:**

O trabalho começou com a importação de dados imobiliários da Califórnia. Identifiquei e tratei valores ausentes na coluna `total_bedrooms` através da remoção das linhas afetadas. Para garantir a robustez do modelo, apliquei **transformações logarítmicas** em variáveis com distribuições assimétricas, como `total_rooms` e `population`, tornando-as mais adequadas para algoritmos preditivos. A natureza geográfica dos dados foi visualizada através de um mapa de dispersão, confirmando a **influência da localização (proximidade ao oceano)** nos valores dos imóveis.

---

**2. Engenharia de Features e Análise de Correlação:**

Para aprimorar a capacidade preditiva do modelo, criei novas características (`bedroom_ratio` e `household_rooms`) que refletem proporções importantes sobre o imóvel. A variável categórica `ocean_proximity` foi convertida em um formato numérico usando **One-Hot Encoding**, permitindo sua integração ao modelo. Uma **matriz de correlação** detalhada foi gerada e analisada, revelando que a **`median_income` (renda mediana)** é o preditor mais forte do `median_house_value`, com uma correlação positiva significativa.

---

**3. Modelagem Preditiva e Otimização:**

Iniciei a fase de modelagem com um modelo de **Regressão Linear**, obtendo um R-squared de 66%. Buscando maior precisão, implementei um **Random Forest Regressor**, que, inicialmente, elevou o R-squared para aproximadamente 80%. Para otimizar ainda mais este modelo e garantir a melhor performance, utilizei **GridSearchCV com validação cruzada**, ajustando cuidadosamente hiperparâmetros como `n_estimators`, `max_features` e `min_samples_split`.

---

**4. Resultados e Demonstração de Valor:**

O modelo **Random Forest otimizado** alcançou um **R-squared de 80.37%** no conjunto de teste. Este resultado demonstra que o modelo consegue explicar mais de 80% da variância nos valores dos imóveis, indicando uma alta capacidade preditiva. Finalizei o projeto com uma **aplicação prática**: usando as características de um imóvel hipotético, o modelo previu com sucesso um valor de **$489.029,80**, validando sua aplicabilidade real em cenários de estimativa de valor de mercado.

Este projeto destaca minha proficiência em construir soluções de Machine Learning do início ao fim, desde a manipulação de dados até a entrega de previsões precisas e acionáveis.

---