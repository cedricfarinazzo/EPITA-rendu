import os
import shutil
import zipfile

import config_epitarendu
import data_epitarendu


### configfile

def createconfigfile():
    data = data_epitarendu.defaultconfigfile
    with open(data_epitarendu.configfile, "w+") as file:
        file.write(data)


def readconfigfilr():
    with open(data_epitarendu.configfile, "r") as file:
        data = file.read()
    config = config_epitarendu.Config
    config.Parse(data)
    return config


def updateconfigfile(config):
    with open(data_epitarendu.configfile, "w+") as file:
        file.write(config.__repr__())


### init

def createdirectory(newpath):
    if os.path.exists(newpath):
        raise Exception("already exists")
    else:
        os.mkdir(newpath)

def createfile(newpath, data):
    if os.path.exists(newpath):
        raise Exception("already exists")
    else:
        with open(newpath, "w+") as file:
            file.write(data)

def init(id, config):
    try:
        createdirectory(config.workdirectory)
    except:
        pass
    path = config.workdirectory + "/" + data_epitarendu.directorynameprefix + str(id) + "/"
    createdirectory(path)
    createdirectory(path + data_epitarendu.workingdirectoryname)
    createdirectory(path + data_epitarendu.workingdirectoryname + "/" + config.login)
    createdirectory(path + data_epitarendu.releasedirectory)
    createdirectory(path + data_epitarendu.releasedirectory + "/" + data_epitarendu.oldreleasedirectory)
    createfile(path + data_epitarendu.workingdirectoryname + "/" + config.login + "/" + data_epitarendu.readmefilename, "TP" + str(id) +"\n\n" + data_epitarendu.readmetemplate)
    createfile(path + data_epitarendu.workingdirectoryname + "/" + config.login + "/" + data_epitarendu.authorsfilename, "* " + config.login + "\n")
    return path

def addzip(zippath, path, config):
    shutil.copy(zippath, path + (zippath.split("/")[-1]))
    with zipfile.ZipFile(zippath, path) as zip:
        zip.extractall()
    with zipfile.ZipFile(zippath, path + data_epitarendu.workingdirectoryname + "/" + config.login + "/" ) as zip:
        zip.extractall()

### release