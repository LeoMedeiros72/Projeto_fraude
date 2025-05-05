# Projeto de Detecção de Fraude com Machine Learning

Este repositório contém uma solução completa de detecção de fraudes em transações financeiras utilizando técnicas de Machine Learning. A solução foi desenvolvida com foco em escalabilidade e monitoramento, e é composta por:

- **Modelagem supervisionada com Random Forest**
- **Balanceamento de dados com SMOTE**
- **API com FastAPI** para inferência
- **Deploy com Docker**
- **Monitoramento com MLflow e Evidently**

---

##  Estrutura do Projeto
```
projeto_fraude/
├── app/                  
│   ├── main.py
│   ├── model.joblib
│   └── requirements.txt
├── colab /
│   └── projeto_fraude.ipynb
|   └── projeto_fraude.py
├── data/                 
│   └── creditcard.csv    # Não incluído no repositório (para download acesse: 'https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud'
├── docker/
│   └── Dockerfile
├── mlflow_tracking/
│   └── experimento.py
├── monitoring/
│   └── drift_report.py
├── notebooks/
│   └── 01_modelagem.ipynb
├── .gitignore
├── README.md
```

---

## Modelagem

Este projeto utiliza a técnica de Random Forest para modelar a detecção de fraudes nas transações financeiras. O fluxo do projeto de modelagem inclui:

1. **Análise Exploratória dos Dados (EDA)**: Compreensão dos dados e análise estatística, incluindo a verificação de variáveis e a distribuição das classes.
2. **Balanceamento dos Dados com SMOTE**: A técnica SMOTE (Synthetic Minority Over-sampling Technique) é aplicada para balancear as classes desiguais (fraude vs não-fraude), gerando amostras sintéticas para a classe minoritária.
3. **Treinamento do Modelo**: O modelo Random Forest é treinado utilizando os dados balanceados.
4. **Avaliação do Modelo**: O desempenho do modelo é avaliado por meio da matriz de confusão e do classification report, que fornecem métricas como precisão, recall, F1-score, etc.

---

## API com FastAPI

A API foi construída utilizando **FastAPI** para servir o modelo treinado e permitir inferências em tempo real.

### Para rodar a API localmente, execute:

```bash
uvicorn app.main:app --reload
```

Ou modifique o `data_path` no notebook para apontar corretamente para o arquivo.

Você pode baixar o dataset neste link:  
👉 https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

---

## Requisitos
Instale as dependências com:
```bash
pip install -r app/requirements.txt
```

---
## Deploy com Docker

Para facilitar o deploy da aplicação, ela foi containerizada utilizando Docker. Execute os seguintes comandos para construir e rodar a imagem Docker:

Para construir a imagem Docker:
```bash
docker build -t projeto-fraude
```

Para rodar a aplicação em um container:
```bash
docker run -d -p 8000:8000 projeto-fraude
```
A aplicação estará acessível em http://localhost:8000.

---
## Monitoramento

O monitoramento da solução é realizado utilizando as seguintes ferramentas:

**MLflow**: Usado para rastrear experimentos e salvar o histórico dos modelos treinados.

**Evidently**: Utilizado para monitorar o drift do modelo em produção, garantindo que a performance do modelo seja mantida ao longo do tempo.

---
## Dataset

Para rodar o projeto, coloque o dataset no caminho:
```bash
/content/drive/MyDrive/Projeto_Fraude/creditcard.csv
```

## Contato
Leonardo – Cientista de Dados, Analista de Dados

[LinkedIn](https://www.linkedin.com/in/leonardo-santos-medeiros/) 
