Previsão de Empréstimos Automatizados
==============================

A empresa procura automatizar em tempo real o processo de qualificação do crédito com base nas informações prestadas pelos clientes durante o preenchimento de um formulário de candidatura online. Espera-se com o desenvolvimento de modelos de ML que possam ajudar a empresa a prever a aprovação de empréstimos na aceleração do processo de tomada de decisão para determinar se um solicitante é elegível para um empréstimo ou não.

## Dataset
* [Loan Predication Dataset](https://www.kaggle.com/ninzaami/loan-predication)

## Index
* [Dataset](https://github.com/julianyraiol/ml-deploy/blob/main/data/raw/train_loan.csv)
* [Notebook](https://github.com/julianyraiol/ml-deploy/blob/main/Trab_Final_Previsão_emprestimo.ipynb)
* [Flask API](https://github.com/julianyraiol/ml-deploy/blob/main/src/app/api.py)

# Configuração de ambiente

É preciso instalar a virtualenv para configurar as dependências do projeto.

```bash
$ git clone https://github.com/julianyraiol/ml-deploy
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Executar API

```bash
$ cd ml-deploy/src/app
$ python api.py
```

Disponível em http://0.0.0.0:5000

## Executar Streamlit

```bash
$ cd ml-deploy
$ python api.py
```

Disponível em http://localhost:8501


# Deploy da API na GCP

O endereço da API está em http://34.72.103.113:5000