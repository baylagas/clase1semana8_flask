from Logic import Logic


class UserLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = ["id", "user", "password"]

    def getUserData(self, user):
        database = self.get_databaseXObj()
        sql = f"select * from cardexdb.user where user='{user}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        return data[0]
