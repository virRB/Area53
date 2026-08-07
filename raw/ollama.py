import requests

def askAI(prompt: str, model: str="phi3:latest") -> str:
    try:
        r = requests.post("http://localhost:11434/api/generate",
            json={"model": model,
                "prompt": prompt,
                "stream": False,
                "keep_alive": "30m",
                "options": {
                    "temperature": 1.2
                }}, timeout=60)
        r.raise_for_status()
        return r.json()["response"]
    except Exception as e:
        return f"Error: {e}"