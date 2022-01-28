from typing import Optional


class Data_log:
    def __init__(self, log_num: Optional[int], list_name, list_password, list_cpf):
        self.log_num = log_num
        self.list_name = list_name
        self.list_password = list_password
        self.list_cpf = list_cpf

    def register(self):
        for i in range(0, self.log_num):
            print(f'\n{i + 1}° :')
            name = input('\nNome de usuário: ')
            password = input('\nSenha: ')
            cpf = str(input('\nCPF: '))
            self.list_name.append(name)
            self.list_password.append(password)
            self.list_cpf.append(cpf)

    def users(self):
        print('\nUSUÁRIOS REGISTRADOS')
        print('=' * 8)
        for i in range(0, self.log_num):
            print(f'\nUsername - {self.list_name[i]}')
            print(f'Password - {self.list_password[i]}')
            print(f'CPF - {self.list_cpf[i]}\n')

    def add_user(self):
        log_num_sum = int(input('Quantos novos serão registrados? '))
        for i in range(0, log_num_sum):
            print(f'\n{self.log_num + i + 1}° :')
            name = input('\nNome de usuário: ')
            password = input('\nSenha: ')
            cpf = input('\nCPF: ')
            print('\n')
            self.list_name.append(name)
            self.list_password.append(password)
            self.list_cpf.append(cpf)
        self.log_num += log_num_sum

    def del_user(self):
        num = int(input('Quantos usuários serão deletados? '))
        for i in range(0, num):
            opt = int(input('[1] Excluir por CPF / [2] Excluir por nome\n'))
            if opt == 1:
                cpf_del = str(input('\nCPF do usuário a ser deletado: '))
                log_position = self.list_cpf.index(cpf_del)
                self.list_name.pop(log_position)
                self.list_password.pop(log_position)
                self.list_cpf.pop(log_position)
                self.log_num -= 1
            elif opt == 2:
                name_del = input('\nNome do usuário a ser deletado: ')
                log_position = self.list_name.index(name_del)
                self.list_name.pop(log_position)
                self.list_password.pop(log_position)
                self.list_cpf.pop(log_position)
                self.log_num -= 1