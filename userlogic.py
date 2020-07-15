from Logic import Logic
from userobj import UserObj


class UserLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = ["id", "user", "password", "role"]

    def getUserData(self, user):
        database = self.get_databaseXObj()
        sql = f"select * from cardexdb.user where user='{user}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            userObj = UserObj(
                data_dic["id"], data_dic["user"], data_dic["password"], data_dic["role"]
            )
            return userObj
        else:
            return None
