class Department:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
 
    class Manager:
        def __init__(self, name, position):
            self.name = name
            self.position = position
 
        def manage_employee(self, employee):
            print(f"{self.name} ({self.position}) управляет {employee.name} ({employee.position})")
 
# Создаем объекты Employee и Manager
employee = Department.Employee("Алексей", "разработчик")
manager = Department.Manager("Ольга", "руководитель проекта")
 
# Метод manage_employee используется для отображения информации о связи между менеджером и сотрудником
manager.manage_employee(employee)
