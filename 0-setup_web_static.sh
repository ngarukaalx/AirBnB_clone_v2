#!/usr/bin/env bash
# Prepare your web servers

# install Nginx if it not already installed
sudo apt-get update
sudo apt-get update
sudo apt-get install -y nginx

# create the folder /data/ if it doest exit
sudo mkdir -p /data/web_static/releases/test /data/web_static

# create fake HTML file /data/web_static/releases/test/index.html
echo "Hello hiram!" | tee -a /data/web_static/releases/test/index.html

# Create a symbolic link
release_folder="/data/web_static/releases/"
current_link="/data/web_static/current"
# create a new symbolick link
sudo ln -sf "$release_folder/test" "$current_link"

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
nginx_config="/etc/nginx/sites-enabled/default"
sudo sed -i '41i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $nginx_config

sudo nginx -t
sudo service nginx restart
