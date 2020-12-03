# pygmres
Trabalho da disciplina de Programação Científica da UFF, período 2020.1.

### Instalação
Você deve possuir em seu ambiente:

* [Python](https://www.python.org/downloads/) >= [3.6](https://www.python.org/downloads/release/python-360/)
    * [pipenv](https://pypi.org/project/pipenv/) - pode ser instalado com ```pip3 install pipenv```. Se você tem Python >= 3.4, pip já vem pré-instalado. 
    Caso contrário, [aqui](https://pip.pypa.io/en/stable/installing/) existe um tutorial ensinando como instalá-lo.

### Configuração
Crie um environment do pipenv usando:
```pipenv shell```

A seguir instale as dependências:
```pipenv install```

Ao fim, você está livre para editar ou executar o projeto.

### Executando testes
Execute o comando a seguir para rodar os testes unitários:
```pytest```

### Links adicionais

* [Especificação do algoritmo GMRES](http://www.acme.byu.edu/wp-content/uploads/2014/09/Krylov2.pdf)
