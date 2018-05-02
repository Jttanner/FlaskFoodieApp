from IUserDao import IUserDao

class UserDao(IUserDao):
    def __init__(self):
        self.dbURL = 'C:\\Users\Tanner Desktop\source\repos\FlaskTest\FlaskTest\db\test.db'
        self.connection = None

    def openConnection(self, dbURL):
        self.connection = create_connection(self.dbURL)

    def getConnection(self):
        return self.connection

    def closeConnection(self, dbURL):
        pass

    def insertUser(self, userInfo):
        pass

    def deleteUser(self, userInfo):
        pass

    def updateUser(self, userInfo):
        pass

    def getUser(self, userInfo):
        pass
    

