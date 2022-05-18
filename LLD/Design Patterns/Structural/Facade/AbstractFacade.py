import abc

class AbstractGetEmployeeFacade(abc.ABC):
    @abc.abstractmethod
    def get_employee(self):
        pass

class GetEmployeeFacade(AbstractGetEmployeeFacade):
    def get_employee(self):
        # do pyodbc stuff
        # create connection
        # open connection
        # run the query
        # print and return the employees
        print("Employee 1 Employee 2 blah blah blah")
        # connection commit
        # connection close