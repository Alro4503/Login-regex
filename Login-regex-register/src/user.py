class User:

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def getInfo(self):
        print(self.name)
        print(self.surname)
        print(self.email)
        print(self.password)

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname


    def getEmail(self):
        return self.email


    def getPassword(self):
        return self.password