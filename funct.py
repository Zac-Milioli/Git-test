class Data_log:
    def __init__(self, log_num, list_name, list_password):
        self.log_num = log_num
        self.list_name = list_name
        self.list_password = list_password

    def register(self):
        for i in range(0, self.log_num):
            print(f'\n{i + 1}° :')
            name = input('\nNome de usuário: ')
            password = input('\nSenha: ')
            self.list_name.append(name)
            self.list_password.append(password)

    def users(self):
        print('\nUSUÁRIOS REGISTRADOS')
        print('=' * 8)
        for i in range(0, self.log_num):
            print(f'\nUsername - {self.list_name[i]}')
            print(f'Password - {self.list_password[i]}\n')

    def add_user(self):
        log_num_sum = int(input('Quantos novos serão registrados? '))
        for i in range(0, log_num_sum):
            print(f'\n{self.log_num + i + 1}° :')
            name = input('\nNome de usuário: ')
            password = input('\nSenha: ')
            print('\n')
            self.list_name.append(name)
            self.list_password.append(password)
        self.log_num += log_num_sum

    def del_user(self):
        num = int(input('Quantos usuários serão deletados? '))
        for i in range(0, num):
            name_del = str(input('\nNome do usuário a ser deletado: '))
            log_position = self.list_name.index(name_del)
            self.list_name.pop(log_position)
            self.list_password.pop(log_position)
            self.log_num -= 1

