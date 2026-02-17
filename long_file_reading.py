from pathlib import Path
path = Path("./text_files/pi_million_digits.txt")
content = path.read_text() # this is a string that contains all the data in the file
lines = content.splitlines() # this is array of lines in the file
for line in lines:
    print(line)