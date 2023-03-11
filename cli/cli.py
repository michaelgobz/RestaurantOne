"""CLI module."""
import sys
from model import CLI

cli = CLI()

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        cli.cli()
    elif(sys.argv[1] == 'migrate'):
        cli.migrate()
    elif(sys.argv[1] == 'loadData'):
        cli.load_data()
    