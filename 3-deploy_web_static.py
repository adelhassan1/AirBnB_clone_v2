#!/usr/bin/python3
# Fabric script that creates and distributes an archive to your web servers

from fabric.api import env, local, put, run
from datetime import datetime
import os.path
env.hosts = ["54.165.117.227", "54.87.213.18"]

def deploy():
    """
     creates and distributes an archive to your web servers
     """
     try:
         data = datetime.now().strftime("%Y%m%d%H%M%S")
         if isdir("versions")is False:
             local ("mkdir versions")
        file_name = "versions/web_static_{}".format(date)
        local("tar -cvzf {} web_static".format(file_name)
        return file_name
    except:
    return None

do_deploy(archive_path):
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "data/web_static/releases"
        put(archive_patj, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{}{}{}'.format(file_n, path, no_ext))
