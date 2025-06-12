# Previsao_Preço_de_Imoveis

# Projeto de Previsão de Valores de Imóveis na Califórnia 🏡💰

Este projeto demonstra a aplicação de técnicas de Machine Learning para prever o valor mediano de imóveis (`median_house_value`) em diferentes distritos da Califórnia, utilizando um dataset abrangente de características geográficas e demográficas.

## Problema Abordado: Regressão

O objetivo central é resolver um problema de **regressão**, onde o modelo aprende a prever um valor contínuo (o preço da casa) com base nas características de entrada.

## Principais Etapas e Conquistas:

1.  **Análise Exploratória de Dados (EDA):**
    * Visualização de distribuições das características.
    * Análise de correlações entre variáveis, identificando `median_income` como um forte preditor.
    * Visualização da distribuição geográfica dos valores dos imóveis.
2.  **Pré-processamento e Feature Engineering:**
    * Tratamento de dados ausentes (remoção de linhas com NaNs).
    * Aplicação de transformações logarítmicas em variáveis com distribuições assimétricas para normalização.
    * Criação de novas features (`bedroom_ratio`, `household_rooms`) para capturar relações mais complexas.
    * Codificação One-Hot de variáveis categóricas (`ocean_proximity`).
3.  **Modelagem e Avaliação:**
    * **Modelos Utilizados:**
        * **Regressão Linear:** Um modelo baseline para estabelecer a performance inicial.
        * **Random Forest Regressor:** Um modelo de ensemble robusto, conhecido por sua alta performance em problemas de regressão.
    * **Otimização:** Aplicação de `GridSearchCV` para tunar os hiperparâmetros do Random Forest, buscando a melhor performance do modelo.
    * **Performance:** O modelo de Random Forest otimizado demonstrou uma capacidade preditiva significativamente maior (R² de ~0.80) em comparação com o modelo linear.

## Demonstração de Habilidades:

* Manipulação e limpeza de dados com `pandas`.
* Técnicas de EDA e visualização (`matplotlib`, `seaborn`).
* Engenharia de features para melhorar o desempenho do modelo.
* Construção e avaliação de modelos de regressão.
* Otimização de modelos com `GridSearchCV`.

