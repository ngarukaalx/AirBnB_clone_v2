#!/usr/bin/env bash
# Prepare your web servers

# install Nginx if it not already installed
if [ ! -x "$(command -v nginx)" ]; then
	apt-get update
	apt-get install -y nginx
fi

# create the folder /data/ if it doest exit
sudo mkdir -p /data/web_static/releases/test /data/web_static

# create fake HTML file /data/web_static/releases/test/index.html
echo "Hello hiram!" | tee -a /data/web_static/releases/test/index.html

# Create a symbolic link
release_folder="/data/web_static/releases/"
current_link="/data/web_static/current"
# create a new symbolick link
ln -sf "$release_folder/test" "$current_link"

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
nginx_config="/etc/nginx/sites-enabled/default"
sudo sed -i '41i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $nginx_config

nginx -t
service nginx restart
