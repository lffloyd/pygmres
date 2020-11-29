import argparse
from src.files import read_system_of_lineq_from_file
from src.gmres import gmres

parser = argparse.ArgumentParser(description="PyGMRES - Implementacao de GMRES em Python")
parser.add_argument('--lsyst', type=str, help='arquivo com o sistema a ser resolvido, formato: Ax=b. O arquivo deve conter A e b', required=True)
parser.add_argument('--debug', type=int, help='debug ativado ou nao', required=False, default=1)
args = parser.parse_args()

A, b = read_system_of_lineq_from_file(args.lsyst)
print(f'A={A}')
print(f'b={b}')

x = gmres(A, b)
print(f'x={x}')
