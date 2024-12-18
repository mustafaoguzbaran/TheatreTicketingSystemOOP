from Models.TheatreModels.TheatreModel import Theatre


class ComedyTheatreModel(Theatre):
    def __init__(self):
        super().__init__()
        self._name = None
        self._location = None
        self._hours = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location: str):
        self._location = location

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours: str):
        self._hours = hours
