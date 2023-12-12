#!/usr/bin/python3
"""distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import *
from os.path import exists

env.hosts = ['107.23.64.175', '3.80.19.164']
env.user = 'ubuntu'
env.key = '/home/vagrant/.ssh/school'


def do_deploy(archive_path):
    """distributes an archive to your web servers
    args:
        archive_path - path to archive
    """

    if not exists(archive_path):
        return False
    try:
        # upload to folder /tmp/ in server
        put(archive_path, "/tmp/")

        # extract the archive file
        archive_file = archive_path.split('/')[-1]
        # remove .gtz extension
        new_file = archive_file.split('.')[0]

        # create path to server
        remote_path = f"/data/web_static/releases/{new_file}"
        run(f"mkdir -p {remote_path}")
        # decompress to remote_path
        run(f"tar -xzf /tmp/{archive_file} -C {remote_path}")
        # Delete archive from web server
        run(f"rm /tmp/{archive_file}")

        # create and delete old symbolic link
        old_link = '/data/web_static/current'
        run(f"rm -rf {old_link}")
        # create new link
        run(f"ln -s {remote_path} {old_link}")

        return True
    except Exception as e:
        print(e)
        return False
