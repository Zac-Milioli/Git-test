from funct import Data_log
import os
import getch

print('- '*20)
print('\nSISTEMA SIMPLES REPRESENTATIVO DE REGISTRO DE USUÁRIOS\n')
print('- '*20)

log_num = int(input('Quantos usuários serão registrados? '))
list_name = []
list_password = []
list_cpf = []
obj_user = Data_log(log_num, list_name, list_password, list_cpf)

obj_user.register()
os.system('clear')


def menu():
    print('\n')
    print('_'*10)
    print()
    print('[1] - Mostrar usuários registrados')
    print('[2] - Registrar novos usuários')
    print('[3] - Remover usuário registrado')
    print('[4] - Modificar dados de um usuário')
    print('[5] - Encerrar')
    print('_'*10)

while True:

    menu()
    opt = int(input('Selecione a opção - '))

    if opt == 1:
        obj_user.users()
        char = getch.getch()
        os.system('clear')
    elif opt == 2:
        obj_user.add_user()
        char = getch.getch()
        os.system('clear')
    elif opt == 3:
        obj_user.del_user()
        os.system('clear')
    elif opt == 4:
        obj_user.modify()
        os.system('clear')
    elif opt == 5:
        break