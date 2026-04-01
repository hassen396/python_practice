from pathlib import Path

username = input('what is your name? '.capitalize())
path = Path('./usernames.json')
path.write_text(username)