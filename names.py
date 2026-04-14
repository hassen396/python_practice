with open('./names.txt', 'a+')as file:
    while True:
        name = input('please enter your name!, or q to quit\n')
        if name == 'q':
            break
        file.write(f"{name}\n")
    file.seek(0)
    lines = file.readlines()
    print('the content:', lines)