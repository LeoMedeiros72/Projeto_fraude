#  Projeto de Detecção de Fraude com Machine Learning

Este repositório contém uma solução completa de detecção de fraudes com:
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
├── data/                 
│   └── creditcard.csv    # Não incluído no repositório
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

## 🧠 Modelagem
- Análise exploratória e balanceamento dos dados com SMOTE
- Treinamento com Random Forest
- Avaliação com matriz de confusão e classification report

---

## 🚀 API com FastAPI
```bash
uvicorn app.main:app --reload
```
Acesse a documentação automática em: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Deploy com Docker
```bash
docker build -t projeto-fraude .
docker run -d -p 8000:8000 projeto-fraude
```

---

## 🔍 Monitoramento
- **MLflow** para rastrear experimentos
- **Evidently** para detectar drift em produção

---

## 📂 Dataset
O arquivo `creditcard.csv` **não está incluído no repositório** por questões de tamanho.

Para usar o projeto, coloque o dataset no caminho:
```bash
/content/drive/MyDrive/Projeto_Fraude/creditcard.csv
```

Ou modifique o `data_path` no notebook para apontar corretamente para o arquivo.

Você pode baixar o dataset neste link:  
👉 https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

---

## ✅ Requisitos
Instale as dependências com:
```bash
pip install -r app/requirements.txt
```

---

## 📬 Contato
Leonardo – Cientista de Dados
[LinkedIn](https://www.linkedin.com/) 
