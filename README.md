# Projeto de Detecção de Fraudes Financeiras

Este projeto apresenta uma solução de machine learning para detecção de fraudes em transações de cartão de crédito. Foi desenvolvido com o objetivo de identificar o maior número possível de fraudes verdadeiras (minimizando falsos negativos), mesmo que isso implique aceitar alguns falsos positivos.

## Problema

Uma instituição financeira busca identificar fraudes em tempo real em sua base de clientes de cartão de crédito. A prioridade do modelo é **não deixar nenhuma fraude passar despercebida**, mesmo que isso implique classificar algumas transações legítimas como suspeitas. O foco, portanto, está em maximizar a **recall** (sensibilidade) para fraudes.

## Solução

O projeto utiliza algoritmos supervisionados para treinar e comparar modelos preditivos sobre um conjunto de dados real do Kaggle. Foram avaliados 3 modelos:

- Random Forest
- Regressão Logística
- XGBoost

O modelo final atingiu **87% de detecção de fraudes com 100% de acurácia geral**, com destaque para a capacidade de generalização em dados desequilibrados.

## Tecnologias Utilizadas

- Python 3.10+
- Scikit-learn
- XGBoost
- Pandas / NumPy
- FastAPI (para exposição do modelo via API REST)
- Matplotlib / Seaborn

## Métricas Avaliadas

- **Recall (Fraude):** > 0.85  
- **Precisão:** > 0.90  
- **AUC-ROC:** utilizado para comparar performance dos classificadores  
- **Matriz de Confusão**  
- **Curva Precision-Recall**

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/LeoMedeiros72/Projeto_fraude.git
cd Projeto_fraude
```

2. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```

3. Execute a API:

```bash
uvicorn main:app --reload
```

4. Acesse o endpoint:

[http://localhost:8000/docs](http://localhost:8000/docs)

## Exemplos de Entrada/Saída

Exemplo de entrada (via JSON):

```json
{
  "amount": 120.50,
  "transaction_type": "compra",
  "location": "SP",
  "time": "15:32:00",
  ...
}
```

Saída esperada:

```json
{
  "fraude": true,
  "probabilidade": 0.92
}
```

## Capturas de Tela

![cc2c87c7-a6d1-4f65-a6a8-d137dc8cab45](https://github.com/user-attachments/assets/93c0d7a5-b287-4f6e-b654-c7b560bf74fa)

## Estrutura

Projeto_fraude/

├── data/

├── models/

├── notebooks/

├── src/

│   ├── pipeline.py

│   └── train_model.py

├── main.py

├── requirements.txt

└── README.md

## Considerações 

Este projeto é um exemplo realista de aplicação de modelos de classificação com dados desbalanceados, reforçando a importância de priorizar métricas de sensibilidade em cenários críticos como detecção de fraude.

## Licença

MIT

## Contato

Projeto desenvolvido por [Leonardo Medeiros](https://www.linkedin.com/in/leonardo-santos-medeiros/).  
Entre em contato para sugestões, contribuições ou oportunidades!

