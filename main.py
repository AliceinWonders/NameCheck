# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')
# //server/Users/user/ZA
#
# //server/Users/Прямые-контакты
#

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import os

path = '//server/Users'


filelist = []
for root, dirs, files in os.walk(path):
    for file in files:
        # filelist.append(os.path.join(file))
        filelist.append(os.path.join(root, file))


with open('filelist.txt', 'w', encoding='utf-8') as f:
    for name in filelist:
        incorrect_name = os.path.basename(name)
        if incorrect_name.__contains__(' '):
            f.seek(0, 2)
            f.write(str(name))
            f.write('\n')
