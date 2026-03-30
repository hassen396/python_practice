from pathlib import Path
path = Path('user.txt')
from name_fromating import get_formated_name
while True:
    first = input('please enter your first name: ')
    if not first or len(first.split()) > 1:
        print("please enter properly!\nlet's try again")
        continue
    elif first == 'q':
        break
    last = input('please enter your last name: ')
    if not last or len(last.split()) > 1 :
        print("please enter properly!\nlet's try again")
        continue
    elif last == 'q' :
        break
    formated_name = get_formated_name(first.strip(), last.strip())
    existing_names = path.read_text()
    if formated_name.lower() in existing_names.lower():
        print(f'you already registered {first.title()}')
        continue
    with path.open(mode='+a') as f:
        new_line = '\n' if existing_names else ''
        f.write(f"{new_line}{formated_name}")
    print(f'you have registered successfully! {first}')