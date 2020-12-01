import argparse
from src.files import read_system_of_lineq_from_file
from src.gmres import gmres

parser = argparse.ArgumentParser(
    description="PyGMRES - Implementacao de GMRES em Python")
parser.add_argument("--lsyst", type=str,
                    help="arquivo com o sistema a ser resolvido, formato: Ax=b. O arquivo deve conter A e b", required=True)
parser.add_argument("--resid", type=float,
                    help="residuo minimo para parar as iteracoes", required=False, default=1e-8)
parser.add_argument("--niter", type=int,
                    help="maximo de iteracoes", required=False, default=50)
parser.add_argument("--debug", type=int,
                    help="debug ativado ou nao", required=False, default=1)
args = parser.parse_args()

debug_activated = bool(args.debug)

A, b = read_system_of_lineq_from_file(args.lsyst)
if debug_activated:
    print(f'A={A}')
    print(f'b={b}')

x = gmres(A, b, args.niter, args.resid)
print(f'x={x}')
