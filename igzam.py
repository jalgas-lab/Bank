git 
while True:
    print('1) 1+1=')
    print('2) 2+2=')
    print('3) 3+3=')
    print('4) 4+4=')
    print('5) 5+5=')
    a = int(input('qaysi sorawga juwap bertininizdi tanlan: (1,5): '))
    if a == 1:
        waziypa_qosiw()
    elif a == 2:
        waziypalardi_koriw()
    elif a == 3:
        waziypani_janalaw()
    elif a == 4:
        waziypalardi_oshiriw()
    elif a==5:
        waziypani_aliw()
        break
    else:
        print('Qate tanlaw')


while True:
    b = int(input('1+1? Juwabin jazin: '))
    if b == 2:
        print('Duris')
    else:
        print('Qate')
    with open('todo.txt','a')as file:
    
        v = int(input('3+3? Juwabin jazin: '))

    if v== 6:
        print('Duris')
    else:
        print('Qate')
    with open('todo.txt','a')as file:

        c = int(input('2+2? Juwabin jazin: '))

    if c == 4:
        print('Duris')
    else:
        print('Qate')
    with open('todo.txt','a')as file:
        

        f = int(input('4+4? Juwabin jazin: '))

    if f == 8:
        print('Duris')
        break
    else:
        print('Qate')
    with open('todo.txt','a')as file:
        print('siz barligina juwap berdiniz')