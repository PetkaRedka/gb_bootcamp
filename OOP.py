class User():
    
    count = 0

    def __init__(self, name, login, password):

        self.__name = name
        self.__login = login
        self.__password = password
        User.count += 1
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def login(self):
        return self.__login
    
    
    def set_password(self, password):
        self.__password = password

    password = property(fset=set_password)

    def show_info(self):
        print(f"Имя: {self.__name}   Логин: {self.__login}")
    

class SuperUser(User):

    count = 0

    def __init__(self, name, login, password, role):

        super().__init__(name, login, password)
        self.__role = role
        SuperUser.count += 1
    
    @property
    def role(self):
        return self.__role
    
    @role.setter
    def name(self, role):
        self.__role = role
    
    def show_info(self):
        print(f"Имя: {self.__name}   Логин: {self.__login}   Роль: {self.__role}")

user1 = User('Paul Mccarty', 'Paul', '1234')
user2 = User('George Harrison', 'George', '5678')
user3 = User('Ringo Star', 'Ringo', '3423')
user4 = SuperUser('John Lenon', 'John', '3674', 'admin')

print(f'Users count {User.count}')
print(f'Superusers count {SuperUser.count}')

print(user1.name)
user2.name = 'Ringo Star'
print(user2.name)

print(user4.role)