from pathlib import Path
path = Path('./usernames.json')
content = path.read_text()
print(content)