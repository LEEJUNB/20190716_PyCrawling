class User():
    species = "영장류"
    
    def __init__ (self, name, gender, city):
        self.name = name
        self.gender = gender
        self.city = city
    
    def get_user_info(self):
        return "이름은 : "+ self.name + "\n 성별 : " + self.gender + "\n 사는 곳 : " + self.city

    
    def get_species(self):
        return "사람은 모두" + User.species + "입니다."

user = User("문성재", "남성", "수원")
print(user.get_user_info())
print(user.get_species())