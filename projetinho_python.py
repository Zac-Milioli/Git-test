from funct import Data_log

print('- '*20)
print('\nSISTEMA SIMPLES REPRESENTATIVO DE REGISTRO DE USUÁRIOS\n')
print('- '*20)

log_num = int(input('Quantos usuários serão registrados? '))
list_name = []
list_password = []
list_cpf = []
obj_user = Data_log(log_num, list_name, list_password, list_cpf)

obj_user.register()

def menu():
    print('\n')
    print('_'*10)
    print()
    print('[1] - Mostrar usuários registrados')
    print('[2] - Registrar novos usuários')
    print('[3] - Remover usuário registrado')
    print('[4] - Encerrar')
    print('_'*10)

while True:

    menu()
    opt = int(input('Selecione a opção - '))

    if opt == 1:
        obj_user.users()
    elif opt == 2:
        obj_user.add_user()
    elif opt == 3:
        obj_user.del_user()
    elif opt == 4:
        break