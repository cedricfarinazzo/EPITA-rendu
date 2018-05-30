class Config:

    def __init__(self, login = None, workdirectory = None):
        self.login = login
        self.workdirectory = workdirectory

    def __repr__(self):
        """

        :rtype: object
        """
        return "login = " + self.login + "\nworkdirectory = " + self.workdirectory

    def Parse(self, data):
        try:
            data = data.split("\n")
            for e in data:
                key, d = e.split(" = ")
                if key == "login":
                    self.login = d
                if key == "workdirectory":
                    self.workdirectory = d
        except:
            raise Exception("failed to parse configuration file")
