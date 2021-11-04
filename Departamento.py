class Departamento:

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name
    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, new_budget):
        self.__budget= new_budget

    def __init__(self, code, name, budget):
        self.__code = code
        self.__name = name
        self.__budget = budget
    pass

    def __str__(self):
        return f"{self.__code}\t{self.__budget}\t {self.__name}"