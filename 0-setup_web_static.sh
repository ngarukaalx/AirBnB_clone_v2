#!/usr/bin/env bash
# Prepare your web servers

# install Nginx if it not already installed
if [ ! -x "$(command -v nginx)" ]; then
	apt-get update
	apt-get install -y nginx
fi

# create the folder /data/ if it doest exit
data_folder="/data"
if [ ! -d "$data_folder" ]; then
	mkdir "$data_folder"
fi

# create folder /web_static/ if it does not exit
web_folder="/data/web_static/"
if [ ! -d "$web_folder" ]; then
	mkdir "$web_folder"
fi

# create the folder /data/web_static/releases/ if doest already exist
web_folder="/data/web_static/releases/"
if [ ! -d "$web_folder" ]; then
	mkdir "$web_folder"
fi

# create the folder /data/web_static/shared/ if doest already exist
shared_folder="/data/web_static/shared/"
if [ ! -d "$shared_folder" ]; then
	mkdir "$shared_folder"
fi

# create /data/web_static/releases/test/ if it doesn’t already exist
test_folder="/data/web_static/releases/test/"
if [ ! -d "$test_folder" ]; then
	mkdir "$test_folder"
fi

# create fake HTML file /data/web_static/releases/test/index.html
fake_content="<html><head></head><body>Hiram genius</body></html>"
echo "$fake_content" | tee -a /data/web_static/releases/test/index.html

# Create a symbolic link
release_folder="/data/web_static/releases/"
current_link="/data/web_static/current"
# Remove current link if it exists
rm -f "$current_link"
# create a new symbolick link
ln -s "$release_folder/test" "$current_link"

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
nginx_config="/etc/nginx/sites-enabled/default"
sudo sed -i "/server_name _;/a \
	\
	\tlocation /hbnb_static/ {\
	\t\talias /data/web_static/current/;\
	\t}" $nginx_config

nginx -t
service nginx restart
