class Student:
    def __init__(self, name,gpa,age,email,phone,is_registered):
        self.name = name
        self.gpa = gpa
        self.age = age
        self.email = email
        self.phone = phone
        self.is_registered = is_registered
    def on_honor_roll(self):
        if self.gpa>= 4.3:
            return True
        else:
            return False

