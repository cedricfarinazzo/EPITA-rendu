# -*- coding: utf-8 -*-

import os

class Config:

    def __init__(self, login = None, workdirectory = None):
        self.login = login
        self.workdirectory = workdirectory
        if self.workdirectory != None:
            self.workdirectory = self.workdirectory.replace("~", os.getenv("HOME"))

    def __repr__(self):
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
            self.workdirectory = self.workdirectory.replace("~", os.getenv("HOME"))
        except:
            raise Exception("failed to parse configuration file")
