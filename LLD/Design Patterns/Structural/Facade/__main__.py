from facade_factory import FacadeFactory


if __name__ == "__main__":
    facade = FacadeFactory().get_employee_facade_factory("employee")
    facade.get_employee()
