import os
import winreg
import ctypes
import subprocess
import time
import shutil
from pathlib import Path
from rich import print
from rich.progress import Progress
from transformers import BlipProcessor, BlipForConditionalGeneration
import threading

DONE = False

def thing():
    global DONE
    BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    DONE = True

threading.Thread(target=thing, daemon=True).start()

with Progress() as progress:
    task = progress.add_task("[bold orange]Installing model...[/bold orange]", total=100)
    while not DONE:
        time.sleep(0.05)
        progress.update(task, advance=1)

subprocess.run("cls", shell=True)

BASE = Path(__file__).parent.resolve()

def addToPath(new_path: str):
    new_path = os.path.abspath(new_path)

    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        "Environment",
        0,
        winreg.KEY_READ | winreg.KEY_WRITE
    ) as key:

        try:
            current_path, _ = winreg.QueryValueEx(key, "Path")
        except FileNotFoundError:
            current_path = ""

        paths = current_path.split(";") if current_path else []

        if any(
            os.path.normcase(os.path.normpath(p)) ==
            os.path.normcase(os.path.normpath(new_path))
            for p in paths
        ):
            print("[bold red]Already in PATH[/bold red]")
            return

        updated_path = (
            current_path + ";" + new_path
            if current_path else
            new_path
        )

        winreg.SetValueEx(
            key,
            "Path",
            0,
            winreg.REG_EXPAND_SZ,
            updated_path
        )

    HWND_BROADCAST = 0xFFFF
    WM_SETTINGCHANGE = 0x001A

    result = ctypes.c_ulong()

    ctypes.windll.user32.SendMessageTimeoutW(
        HWND_BROADCAST,
        WM_SETTINGCHANGE,
        0,
        "Environment",
        0,
        5000,
        ctypes.byref(result)
    )


print("[bold yellow]Press enter to continue...[/bold yellow]", end="")
input("")

new = Path.home() / "Area53"
THING = (BASE == new)

if os.path.exists(new) and not THING:
    shutil.copytree(BASE, new, dirs_exist_ok=True)
elif not THING:
    shutil.copytree(BASE, new)

if not THING:
    addToPath(str(new))

with Progress() as progress:
    task = progress.add_task("[bold orange]Installing folders...[/bold orange]", total=100)
    for i in range(100):
        time.sleep(0.05)
        progress.update(task, advance=1)

with Progress() as progress:
    task = progress.add_task("[bold orange]Adding to PATH...[/bold orange]", total=100)
    for i in range(100):
        time.sleep(0.05)
        progress.update(task, advance=1)

print(f"\n[bold green]Installation complete! Installed Area53 to: {new}[/bold green]")
print("[bold yellow]Restart your terminal before using the area53 command.[/bold yellow]")