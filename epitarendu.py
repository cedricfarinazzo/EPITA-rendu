# -*- coding: utf-8 -*-

__author__ = "Cedric Farinazzo"
__version__ = "1.0"
__status__ = "beta"

import os
import sys

import data_epitarendu
import func_epitarendu


def help():
    print("\n epitarendu : help usage")
    print()
    print("     config:  change the default config")
    print("        config login=firstname:name     to change your epita login")
    print("        config directory=/home/user/directory/     to change the directory where you want to work")
    print()
    print("     help: this page")
    print()
    print("     new: initialize a new tp")
    print("        new id zip_path")
    print("             id: an integer that will be the identifier of the tp")
    print("             zip_path: the path of the archive")
    print()
    print("     release: create a rendering archive of an existing tp")
    print("        release id")
    print("             id: the identifier of the tp")
    print()


def config():
    data = sys.argv[2]
    key, d = data.split("=")[0], data.split("=")[1]
    config = func_epitarendu.readconfig()
    up = False
    if key == "login":
        config.login = d
        print("Update login: " + d)
        up = True
    if key == "dir":
        config.workdirectory = d
        print("Update directory: " + d)
        up = True
    if up:
        func_epitarendu.updateconfigfile(config)
        print("success")
    else:
        help()


def new():
    config = func_epitarendu.readconfig()
    id = sys.argv[2]
    print("TP identifier : " + str(id))
    zippath = sys.argv[3]
    print("Zip path : " + zippath)
    path = func_epitarendu.init(id, config)
    func_epitarendu.addzip(zippath, path, config)
    print("success")


def release():
    id = sys.argv[2]
    config = func_epitarendu.readconfig()
    if os.path.exists(config.workdirectory + "/" + data_epitarendu.directorynameprefix + str(id)):
        print("TP" + str(id) + " found!")
        func_epitarendu.makerelease(config.workdirectory + "/" + data_epitarendu.directorynameprefix + str(id), func_epitarendu.readconfig())
        print("success")
    else:
        print("TP" + str(id) + ": Not found!")
        print("failed")


def main():
    try:
        if len(sys.argv) == 1:
            help()
        elif "config" == sys.argv[1]:
            config()
        elif "new" == sys.argv[1]:
            new()
        elif "release" == sys.argv[1]:
            release()
        elif "help" == sys.argv[1]:
            help()
        else:
            help()
    except:
        help()
        print("failed")


if __name__ == "__main__":
    main()
