class Empleado:

    @property
    def SSN(self):
        return self.__SSN

    @property
    def name(self):
        return self.__name
    @property
    def lastname(self):
        return self.__lastname

    @property
    def department(self):
        return self.__department

    def __init__(self, SSN, name, lastname, department):
        self.__SSN = SSN
        self.__name = name
        self.__lastname = lastname
        self.__department = department
    pass

    def __str__(self):
        return f"{self.__SSN}\t{self.__department}\t {self.__name} {self.__lastname}"