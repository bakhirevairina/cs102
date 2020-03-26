class Enity:

    def __init__(self, age:int, name:int):
        self.age = age
        self.name = name

    @staticmethod
    def getNameClass():
        print("Enity")
    
    def getInfo(self):
        print("Info Name: ", self.name)
    
class People(Enity):
    
    def __init__(self, is_alive: bool):
        self.is_alive = is_alive

    def getInfo(self):
        print("Info Is_alive: ", self.is_alive)

if __name__ == "__main__":
    student = Enity(18, "Irina")
    student_2 = People(True)
    student_2.name = "Arina"
    student_2.age = 25
    student.getInfo()
    student_2.getInfo()