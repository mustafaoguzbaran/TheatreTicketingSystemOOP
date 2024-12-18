from Libraries.TheatreService import TheatreService
from Libraries.UserService import UserService

class Main:
    def __init__(self):
        self.userService = UserService()
        self.theatreService = TheatreService()

    def HorrorTheatreProcess(self):
        self.theatreService.id = int(input("Lütfen ID Giriniz: "))
        self.theatreService.name = input("Lütfen Tiyatro Adı Giriniz: ")
        self.theatreService.location = input("Lütfen Tiyatro Lokasyonu Giriniz: ")
        self.theatreService.hours = input("Lütfen Tiyatro Saatleri Giriniz: ")
        self.theatreService.category = "Korku"

    def ComedyTheatreProcess(self):
        self.theatreService.id = int(input("Lütfen ID Giriniz: "))
        self.theatreService.name = input("Lütfen Tiyatro Adı Giriniz: ")
        self.theatreService.location = input("Lütfen Tiyatro Lokasyonu Giriniz: ")
        self.theatreService.hours = input("Lütfen Tiyatro Saatleri Giriniz: ")
        self.theatreService.category = "Komedi"

    @staticmethod
    def getAllTheatreCategories():
        return ("Korku \n"
                "Komedi")

    def UserProcess(self):
        self.userService.id = int(input("Lütfen ID Giriniz: "))
        self.userService.name = input("Lütfen İsim Giriniz: ")
        self.userService.surname = input("Lütfen Soyisim Giriniz: ")
        self.userService.username = input("Lütfen Kullanıcı Adı Giriniz: ")
        self.userService.password = input("Lütfen Şifre Giriniz: ")
        self.userService.address = input("Lütfen Adres Giriniz: ")

    def getUserInfos(self):
        print(self.userService.getUserInfos())

if __name__ == '__main__':
    main = Main()

    print("----------Tüm Tiyatro Kategorileri----------")
    print(Main.getAllTheatreCategories())

    print("----------Horror Tiyatro Kayıt Aşaması----------")
    main.HorrorTheatreProcess()

    print("----------Kayıt Edilen Horror Tiyatro Bilgileri----------")
    print(main.theatreService.getHorrorTheatre())

    print("----------Comedy Tiyatro Kayıt Aşaması----------")
    main.ComedyTheatreProcess()

    print("----------Kayıt Edilen Comedy Tiyatro Bilgileri----------")
    print(main.theatreService.getComedyTheatre())

    print("----------Biletleme İçin Kullanıcı Kayıt Aşaması----------")
    main.UserProcess()

    print("----------Kayıt Edilen Kullanıcı Bilgileri----------")
    main.getUserInfos()

