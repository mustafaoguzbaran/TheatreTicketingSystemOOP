class Users:
    #ilişkiler gösterilecek
    def __init__(self):
        self._id = None
        self._username = None
        self._password = None
        self._name = None
        self._surname = None
        self._address = None

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self,  userID: int):
        if userID == 0:
            raise ValueError("User ID 0 Olamaz!")
        self._id = userID

    @property
    def username(self) -> int:
        return self._username

    @username.setter
    def username(self, username: str):
        self._username = username

    @property
    def password(self) -> int:
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        self._surname = surname

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address: str):
        self._address = address
