#!/usr/bin/env python2
# -*- coding: utf8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

"""Example script which uses WebdavMirror."""

import subprocess
import sys
import fnmatch
import os
from WebdavMirror import WebdavMirror

mirrorDir = "./Dropbox" 
username = 'hans' 
password = 'wurst' 

webFolders = [
(279025, "Semester III", "Software Engineering"),
(279027, "Semester III", "Verteilte Systeme und Kommunikationsnetze"),
(279031, "Semester III", "Datenbanken"),
(279033, "Semester III", "Systemprogrammierung"),
(279023, "Semester III", "SW-Projektmanagement")
]

# Mirror
for webFolder in webFolders:
    mirrorPath = "%s/%s/%s" % (mirrorDir, webFolder[1], webFolder[2])
    if not os.path.exists(mirrorPath):
        os.makedirs(mirrorPath)
    WebdavMirror('https://nbl.fh-bielefeld.de/webdav.php/', '/FH-Bielefeld/ref_%d/' % webFolder[0], username, password, mirrorPath)
