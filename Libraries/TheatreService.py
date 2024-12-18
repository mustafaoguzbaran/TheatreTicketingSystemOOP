from Models.TheatreModels.TheatreModel import Theatre


class TheatreService(Theatre):
    def comedyTheatreBuilder(self, id: int, name: str, location: str, hours: str, category: str):
        self.id = id
        self.name = name
        self.location = location
        self.hours = hours
        self.category = category
        return self

    def horrorTheatreBuilder(self, id: int, name: str, location: str, hours: str, category: str):
        self.id = id
        self.name = name
        self.location = location
        self.hours = hours
        self.category = category
        return self

    def getComedyTheatre(self):
        return (f"ID: {self.id}\n"
                f"İsim: {self.name}\n"
                f"Konum: {self.location}\n"
                f"Saat: {self.hours}\n"
                f"Kategori: {self.category}\n")

    def getHorrorTheatre(self):
        return (f"ID: {self.id}\n"
                f"İsim: {self.name}\n"
                f"Konum: {self.location}\n"
                f"Saat: {self.hours}\n"
                f"Kategori: {self.category}\n")

    def getAllTheatre(self):
        return self.getComedyTheatre() + self.getHorrorTheatre()

