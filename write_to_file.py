from pathlib import Path
path = Path("./text_files/written_file.txt")
content = ''
while True:
    name =input('welcome guest!\nwrite your name here: ')
    if name == 'q':
        break

    content += name + '\n'
path.write_text(content)