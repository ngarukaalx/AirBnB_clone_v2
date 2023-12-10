#!/usr/bin/python3
"""Compress before sending
generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a .tgz archive from the contents of
    the web_static folder
    """
    # creates the folder versions if it doesn;t exist
    local("mkdir -p versions")

    # Get current timestamp
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    # Create archive name
    archine_name = f"web_static_{timestamp}.tgz"
    # compress web_static into the archive
    result = local(f"tar -cvzf versions/{archine_name} web_static")
    # return the archive path if the archive has been correctly generated
    if result.return_code == 0:
        return f"versions/{archine_name}"
    else:
        return None
