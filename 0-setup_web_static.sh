#!/usr/bin/env bash
<<<<<<< HEAD
# A Script that sets up your web servers for the deployment of web_static
# Installing Nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# Create the folders
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

sudo echo "<html>
<head>
<title>
AirBnb Clone
</title>
</head>
<body>
Welcome to AirBnb Clone
</body>
</html>" | sudo tee '/data/web_static/releases/test/index.html'

# Create a symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Ownership of the folder
sudo chown -R ubuntu:ubuntu /data/

# Nginx Config to serve content
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart Nginx
=======
# sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "38i\ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
>>>>>>> 244ccc095292cc5f12263e314aee254ad13614cd
sudo service nginx restart
