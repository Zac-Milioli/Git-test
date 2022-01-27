from funct import Data_log

print('- '*20)
print('\nSISTEMA SIMPLES REPRESENTATIVO DE REGISTRO DE USUÁRIOS\n')
print('- '*20)

log_num = int(input('Quantos usuários serão registrados? '))
list_name = []
list_password = []
obj_user = Data_log(log_num, list_name, list_password)

obj_user.register()

print('\n')
print('_'*10)
print()
print('[1] - Mostrar usuários registrados \n[2] - Adicionar novos usuários \n[3] - Excluir usuário registrado')
opt = int(input('Selecione a opção - '))
print('_'*10)

if opt == 1:
    obj_user.users()
elif opt == 2:
    obj_user.add_user()
    obj_user.users()
elif opt == 3:
    obj_user.del_user()
    obj_user.users()