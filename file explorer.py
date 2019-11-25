import os
from os import path as p
k=56#每行字符个数
l=os.listdir
def depth(path):
    return path.count('/')-1
def he():
    print('Help'.center(56,'-'))
    print('Entering:Input the path or input \'/\' and the serial number of the listed dir.')
    print('Jump:Add an additional \'/\' before an absolute path.')
    print('Command:\n  /help:Show help.\n  /back(/b):Return to the parent path.')
    print('  /exit:Exit this program.\n  /refresh(/r):Reload current path.')
    print('End Help'.center(56,'-'))
def pr():
    global temp,path
    print('-'*56)
    try:
        print(temp)
        if l(temp)==[]:print('//Nothing there.//')
        else:
            for i in l(temp):
                print(' '*depth(temp)+i)
    except PermissionError:print('//Permission denied.//');temp=path
    except Exception as e:print('//Not found.//');print(e);temp=path
    else:path=temp
#/help instructions
print('-'*56+'\nInput the path you want to view,and then press \'enter\'.\nCommands:/back--Back to the parent directory.\nType \'/help\'for more help.\n'+56*'-')
path=input('Path:')
temp=path
pr()#start
while True:#loop
    a=input('-->')
    if a=='':pass
    elif '//' in a:
        temp=a[1::]
        pr()
    elif a[0]=='/':
        if a=='/back' or a=='/b':
            temp=p.split(path)[0]#get parent path
            pr()
        elif a=='/exit':break
        elif a=='/help':he()
        elif a=='/refresh' or a=='/r':pr()
        else:
            try:
                n=int(a[1::])
                temp+='/'+l(temp)[n-1]
                pr()
            except ValueError:
                print('Command not found.')
    else:temp+='/'+a;pr()
