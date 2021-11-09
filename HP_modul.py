class Doctors:
    def __init__(self,id=0,name=None,spec=None,duty=0,salary=0):
        self.D_id= id
        self.D_name= name
        self.D_specail = spec
        self.D_duty = duty
        self.D_salary = salary

    def __repr__(self):
        return f'{self.D_id,[self.D_name],[self.D_specail],[self.D_duty],[self.D_salary]}'

class Staff:
    def __init__(self,id=0,name=None,duty=0,salary=0,Job_roll=None):
        self.S_id = id
        self.S_name = name
        self.S_duty = duty
        self.S_salary = salary
        self.S_job= Job_roll

    def __repr__(self):
        return f'{self.S_id,[self.S_name],[self.S_duty],[self.S_salary],[self.S_job]}'
