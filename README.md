# Projeto: Detecção de Fraudes

Este projeto simula um pipeline completo de detecção de fraudes bancárias:
- Análise exploratória e modelagem com scikit-learn e XGBoost
- Deploy de modelo com FastAPI e Docker
- Rastreio de experimentos com MLFlow
- Monitoramento com Evidently

## Como rodar a API localmente
```bash
cd app
uvicorn main:app --reload
```

## Como testar a API
Use o Postman ou curl:
```json
{
  "V1": -1.359807,
  "V2": -0.072781,
  ...
  "Amount": 149.62
}
```

## Docker
```bash
docker build -t fraude-api .
docker run -p 8000:8000 fraude-api
```

## Dataset

O arquivo `creditcard.csv` não está no repositório por questões de tamanho.

Para usar o projeto, coloque o arquivo em:
