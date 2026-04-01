import re

# This is what I normally would do
url = input('URL: ')
index = url.index('.com/')
username = (url[index + 4 + 1 : ])
print(username)

# using regex
re.sub()
