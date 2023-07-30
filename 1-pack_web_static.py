#!/usr/bin/python3
<<<<<<< HEAD
""" a module to package web_static files """
import datetime
import os
from fabric.api import local


def do_pack():
    """ package function """
    if not os.path.isdir("./versions"):
        os.makedirs("./versions")
    ntime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -czzf versions/web_static_{}.tgz web_static/*".format(ntime))
    return ("{}/versions/web_static_{}.tgz".format(os.path.dirname(
        os.path.abspath(__file__)), ntime))
=======
"""Fabric script that generates a .tgz archive"""


from fabric.api import *
from os import path
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(now)
    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(file_path))
    if result.failed:
        return None
    return file_path
>>>>>>> 244ccc095292cc5f12263e314aee254ad13614cd
