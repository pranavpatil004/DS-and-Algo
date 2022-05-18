from AbstractFacade import GetEmployeeFacade

class FacadeFactory:
    def get_employee_facade_factory(self, type):
        if type == "employee":
            return GetEmployeeFacade()