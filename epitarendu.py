import os
import sys

import data_epitarendu
import func_epitarendu

if "config" in sys.argv[1]:
    data = sys.argv[2]
    key, d = data.split("=")[0], data.split("=")[1]
    config = func_epitarendu.readconfig()
    if key == "login":
        config.login = d
    if key == "dir":
        config.workdirectory = d
    func_epitarendu.updateconfigfile(config)

if "new" in sys.argv[1]:
    id = sys.argv[2]
    zippath = sys.argv[3]
    config = func_epitarendu.readconfig()
    path = func_epitarendu.init(id, config)
    func_epitarendu.addzip(zippath, path, config)

if "makerelease" in sys.argv[1]:
    id = sys.argv[2]
    config = func_epitarendu.readconfig()
    if os.path.exists(config.workdirectory + "/" + data_epitarendu.directorynameprefix + str(id)):
        func_epitarendu.makerelease(config.workdirectory + "/" + data_epitarendu.directorynameprefix + str(id), func_epitarendu.readconfig())
    else:
        print("Not found!")
