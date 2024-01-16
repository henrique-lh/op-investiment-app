# Desafio Otimização

Manual de instalação e execução do desafio de investimento

## Instalação

Caso ainda não tenha o python instalado na sua máquina, instale por meio do link: [https://www.python.org/downloads/](https://www.python.org/downloads/) juntamente com seu gerenciador pacotes pip.

Após a instalação do python e do pip, execute as linhas de comando abaixo em seu terminal. A primeria é responsável por instalar pacotes python e a segunda executará o programa:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 main.py
```

## Do problema

Você pode encontrar informações do problema no arquivo "Desafio Bootcamp OTM ENACOM.pdf"

## Da resolução

A resolução se dá por meio de uma inspiração no problema clássico da computação, chamado "Problema da Mochila" que é um problema de otimização onde busca-se maximizar os itens dentro de uma mochila, sendo conhecidas as: capacidade da mochila, peso e valor dos itens.

A resolução foi adaptada para obedecer as seguintes restrições:

1. Você possui R$ 2.400.00,00 para comprar investimentos.
2. Você não pode ultrapassar o valor de R$ 1.200.000,00 em investimento de risco baixo, R$ 1.500.000,00 em investimentos de risco médio e R$ 900.000,00 em investimentos de risco alto.

Além do algoritmo para resolução do problema, o aplicativo conta com uma interface gráfica para usuário conseguir manipular mais facilmente.

## Tecnologias

As tecnologias utilizadas para resolução deste problema e interface de usuário:

* Python
* Pandas
* Numpy
* Tkinter

## To-do (Principal)
- [x] Criar apresentação
- [x] Utilizar numpy
- [x] Criar front para pegar dado de usuário
- [x] Fazer tratamento de erros e excessões
- [x] Validar respostas de usuários
- [x] Conectar back com front
- [x] Criar ambiente virtual e fazer instalações manualmente
- [x] Decidir o que visualizar
- [x] Criar possibilidade de adicionar dados
- [x] Salvar quais investimentos foram usados em um arquivo CSV
- [x] Implementar funções otimizadoras para 'Baixo' e 'Médio'
- [x] Criar algum tipo de front-end para aplicação (interface gráfica ou web)
- [x] Redução de dimensionalidade e redundância de código
- [x] Implementar primeiros otimizadores
- [x] Salvar dados em um CSV
- [x] Implementar condicionais (garantir restrições)
- [x] Colocar em OO

