import os

'''with open('hello.txt') as f:
    print(f.readline())
    print(f.readline())


with open('hello.txt',"a") as f:
    f.write("not like that tho")

with open('hello.txt') as f:
    print(f.read())

f=open('anewfile.txt','x')


os.remove('anewfile.txt')
'''
if os.path.exists('demofile.txt'):
    os.remove('demofile.txt')
else:
    print('nah')