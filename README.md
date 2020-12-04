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

### Executando o projeto
Após a instalação e a configuração do projeto realizadas acima, você poderá executar o projeto usando o comando:
```python main.py --lsyst <nome do arquivo> --resid <residual minimo> --niter <num iteracoes> --debug <debug ativado>```, onde os argumentos são:

* ```<nome do arquivo>``` - obrigatório. Nome do arquivo representando o sistema linear a ser trabalhado. O arquivo deve possuir o sistema no formato a seguir. As 3 primeiras linhas são os elementos da matriz A e a última linha do arquivo sempre representará o vetor b.

```
2 4 5
6 2 9
1 0 8
1 8 7
```

* ```<residual minimo>``` - opcional. Valor de residual mínimo suficiente para considerar a solução encontrada como boa. Caso não seja passado, o valor padrão de 1e-8 será usado.
* ```<num iteracoes>``` - opcional. Número máximo de iterações do algoritmo GMRES. Caso não seja passado, o valor padrão de 50 será usado.
* ```<debug ativado>``` - opcional. Número (1 ou 0) indicando se deseja ver as saídas de debug ou não ao executar o algoritmo. Caso não seja passado, por padrão o debug está ativado.

### Executando testes unitários
Execute o comando a seguir para rodar os testes unitários:
```pytest```
