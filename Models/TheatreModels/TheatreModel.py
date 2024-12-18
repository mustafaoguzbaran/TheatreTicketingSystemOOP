class Theatre:
    def __init__(self):
        self.__id = None
        self.__category = None

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category



