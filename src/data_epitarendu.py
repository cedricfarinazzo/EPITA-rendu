# -*- coding: utf-8 -*-

import os

configfile = os.getenv("HOME") + "/.epitarendu.config"
configfilebundary = " = "
defaultconfigfile = "login = firstname.name\nworkdirectory = ~/epita_tp"


authorsfilename = "AUTHORS"
readmefilename = "README"
readmetemplate = "\nyour text\n"

workingdirectoryname = "WorkDir"
directorynameprefix = "TP"

toremovelist = ["bin", ".idea", ".vs", "obj"]
archivenameprefix = "rendu-tp-"

releasedirectory = "release"
oldreleasedirectory = "old"