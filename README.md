# Area53

## What Is This?
**Area53** is a program that converts any image into an *impossible* and *strange* theory.

#### Input:
<img src="assets/pigeon.jpg" border="10px" height="200px" width="300px">

#### Output:
<font color="#46cec3">
The seemingly <b>innocent bird</b> perched atop the lamppost in Central Park is, in fact, a time traveler from the future.
relaying messages to a rogue <b>AI</b> controlling the global stock market via synchronized flapping of wings. 
</font>

## How To Setup?
1. First, download the repo and find the folder named `raw`
2. Then, from that folder, run `installer.py` *(Wifi is required during installation)*
3. Then, close and re-open all instances of terminal, powershell, or command prompt *(This includes Visual Studio Code)*
2. You should now be able to use the **area53** command!

## Commands!
```bash
area53 --investigate <Image filename>
```
Investigate and generate a theory about a given image

```bash
area53 --version
```
Displays your installed version of **Area53**

```bash
area53 --help
```
Displays a help message providing information about the commands and their usage

## Dependencies
> currently **Area53** is **Windows** only
- **Rich**
```bash
pip install rich
```
- **Requests**
```bash
pip install requests
```
- **Pillow**
```bash
pip install Pillow
```
- **Transformers**
```bash
pip install transformers
```
- **PyTorch**
```bash
pip install torch
```
- **Ollama**
Download at [Ollama](https://ollama.com/)
- *Gemma2:2b*
After installing ollama, run
```bash
ollama pull gemma2:2b
```

## Credits
Pigeon image from [Wikimedia](https://commons.wikimedia.org/w/index.php?search=pigeon&title=Special%3AMediaSearch&type=image) by **Pinkietastic**