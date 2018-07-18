# -*- coding: utf-8 -*-

import os
import shutil
import zipfile
from distutils.dir_util import copy_tree

import config_epitarendu
import data_epitarendu


### configfile

def createconfigfile():
    open(data_epitarendu.configfile, "a").close()
    print("Init config file : " + data_epitarendu.configfile)
    data = data_epitarendu.defaultconfigfile
    with open(data_epitarendu.configfile, "w") as file:
        file.write(data)


def readconfig():
    if not os.path.exists(data_epitarendu.configfile):
        createconfigfile()
    with open(data_epitarendu.configfile, "r") as file:
        data = file.read()
    config = config_epitarendu.Config()
    config.Parse(data)
    return config


def updateconfigfile(config):
    print("Writing on config file : " + data_epitarendu.configfile)
    with open(data_epitarendu.configfile, "w") as file:
        file.write(config.__repr__())


### new

def createdirectory(newpath):
    if os.path.exists(newpath):
        print("Directory : " + newpath + " already exists")
    else:
        print("Create directory: " + newpath)
        os.mkdir(newpath)

def createfile(newpath, data):
    print("Create file: " + newpath)
    with open(newpath, "w+") as file:
        file.write(data)

def init(id, config):
    try:
        createdirectory(config.workdirectory)
    except:
        pass
    path = config.workdirectory + "/" + data_epitarendu.directorynameprefix + str(id) + "/"
    print("Init TP" + str(id) + " on " + path)
    createdirectory(path)
    createdirectory(path + data_epitarendu.workingdirectoryname)
    createdirectory(path + data_epitarendu.workingdirectoryname + "/" + config.login)
    createdirectory(path + data_epitarendu.releasedirectory)
    createdirectory(path + data_epitarendu.releasedirectory + "/" + data_epitarendu.oldreleasedirectory)
    createfile(path + data_epitarendu.workingdirectoryname + "/" + config.login + "/" + data_epitarendu.readmefilename, "TP" + str(id) +"\n" + data_epitarendu.readmetemplate)
    createfile(path + data_epitarendu.workingdirectoryname + "/" + config.login + "/" + data_epitarendu.authorsfilename, "* " + config.login + "\n")
    return path

def addzip(zippath, path, config):
    print("Copying zip on tp directory")
    shutil.copy(zippath, path + (zippath.split("/")[-1]))
    print("Extract zip on tp directory")
    with zipfile.ZipFile(zippath, "r") as zip:
        zip.extractall(path + "/")
    print("Extract zip on working directory")
    with zipfile.ZipFile(zippath, "r") as zip:
        zip.extractall(path + "/" + data_epitarendu.workingdirectoryname + "/" + config.login + "/" )

### release

def removeitem(workdir):
    os.chdir(workdir)
    files = os.listdir('.')
    for f in files:
        if f in data_epitarendu.toremovelist:
            try:
                print("Remove " + f + "before compression")
                if os.path.isdir(workdir + "/" + f):
                    os.rmdir(workdir + "/" + f)
                else:
                    os.remove(workdir + "/" + f)
            except:
                pass
        else:
            if os.path.isdir(workdir + "/" + f):
                removeitem(workdir + "/" + f)


def zip(workpath, to):
    shutil.make_archive(to, 'zip', workpath, verbose=True)

def moveold(dir, path,config):
    os.chdir(dir + "/" + data_epitarendu.oldreleasedirectory)
    nbold = len(os.listdir())
    newname = data_epitarendu.archivenameprefix + config.login + "_" + str(nbold) + ".zip"
    os.rename(path,dir + "/" + data_epitarendu.oldreleasedirectory + "/" + newname)


def copydir(fro, to):
    copy_tree(fro, to)


def makerelease(path, config):
    print("Copying work directory to /tmp/BuildTP/")
    copy_tree(path + "/" + data_epitarendu.workingdirectoryname, "/tmp/BuildTP/")
    removeitem("/tmp/BuildTP/" + config.login)
    os.chdir(path + "/" + data_epitarendu.releasedirectory)
    files = os.listdir()
    for e in files:
        if data_epitarendu.archivenameprefix in e:
            print("Moving old archive on release/old/")
            moveold(path + "/" + data_epitarendu.releasedirectory + "/", path + "/" + data_epitarendu.releasedirectory + "/" + e, config)
    print("Compress from /tmp/BuildTP/ to " + data_epitarendu.releasedirectory + "/" + data_epitarendu.archivenameprefix + config.login + ".zip")
    zip("/tmp/BuildTP/", path + "/" + data_epitarendu.releasedirectory + "/" + data_epitarendu.archivenameprefix + config.login)
