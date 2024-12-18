from Models.UserModel import Users

class UserService(Users):
    def getUserInfos(self):
        return (f"ID: {self.id} \n"
                f"İsim: {self.name} \n"
                f"Soyisim: {self.surname} \n"
                f"Kullanıcı Adı: {self.username} \n"
                f"Şifre: {self.password} \n"
                f"Adres: {self.address} \n")

    def addUserByUserModel(self, userModel: Users):
        self.id = userModel.id
        self.name = userModel.name
        self.surname = userModel.surname
        self.username = userModel.username
        self.password = userModel.password
        self.address = userModel.address
        return self
