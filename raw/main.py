import ollama
import os
from rich import print
from rich.console import Console
import sys
import threading
import time
import importlib

if len(sys.argv) != 2:
    print("[bold red]What?[/bold red]")
    sys.exit(1)

HERE = os.getcwd()
path = sys.argv[1]

IMAGE = os.path.join(HERE, path)
if not os.path.exists(IMAGE):
    print(f"[bold red]Cannot find {IMAGE}[/bold red]")
    sys.exit(1)

DONE = False
recognise = None
def add_recongition() -> None:
    global DONE, recognise
    recognise = importlib.import_module("recognise")
    DONE = True

threading.Thread(target=add_recongition, daemon=True).start()

console = Console()

with console.status("[bold yellow]Loading Image Recognition...[/bold yellow]", spinner="squareCorners", spinner_style="magenta"):
    while not DONE:
        time.sleep(0.05)

MODEL = "gemma2:2b"
what = recognise.identify(IMAGE)
print(f"[bold cyan]Identified:[/bold cyan]\n   [bold green]{what}[/bold green]")

def generate_prompt(topic: str) -> str:
    return f"""
You are an AI agent inside Area53, a fictional investigation agency.
Create a completely fictional and absurd conspiracy theory based on:
{topic}
Rules:
- Output only one sentence.
- Do not explain it.
- Make it sound like a serious conspiracy.
- The theory must be humorous and impossible.
Example:
Pigeons are actually government-operated hard drives.
"""

def create_theory(topic: str) -> str:
    prompt = generate_prompt(topic)
    answer = ollama.askAI(prompt, model=MODEL)
    return answer

response = ""
RESPONDED = False
def generate_response() -> None:
    global response, RESPONDED
    response = create_theory(what)
    RESPONDED = True

threading.Thread(target=generate_response, daemon=True).start()
with console.status("[bold yellow]Creating Theory...[/bold yellow]", spinner="squareCorners", spinner_style="magenta"):
    while not RESPONDED:
        time.sleep(0.05)

print(f"[bold yellow]Classified:[/bold yellow]\n   [bold magenta]{response}[/bold magenta]")
#space monkeys exist