import argparse
import os
import subprocess
import sys
from rich import print

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(HERE, "main.py")

parser = argparse.ArgumentParser(prog="Area53")

parser.add_argument("--investigate", "-i", metavar="IMAGE", help="Investigate any image")
parser.add_argument("--version", action="store_true", help="Display your installed version of Area53")

argv = parser.parse_args()
if argv.investigate:
    subprocess.run([sys.executable, MAIN, argv.investigate])
    sys.exit()
elif argv.version:
    print("[bold yellow]Area53: [/bold yellow]\n[bold magenta]Investigative Investigations![/bold magenta]\n[bold green]v1.0[/bold green]")
else:
    parser.print_help()