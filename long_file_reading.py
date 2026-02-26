from pathlib import Path
path = Path("text_files/pi_million_digitS.txT")
content = ""
try:
    content = path.read_text() # this is a string that contains all the data in the file
except FileNotFoundError:
    print(f"file {path} doesn't exist")
    exit()
lines = content.splitlines() # this is array of lines in the file
for line in lines[:10]:
    print(line)