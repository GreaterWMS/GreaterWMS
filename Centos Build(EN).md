~~~shell
su - // Enter root
chmod u+w /etc/sudoers // up auth
vim /etc/sudoers // "{{ your username }} ALL=(ALL) ALL"  // add your username
chmod u-w /etc/sudoers // cancel auth
restart // 
sudo yum update
sudo yum upgrade
sudo yum -y install gcc-c++
sudo yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel libffi-devel gcc make
sudo yum install nodejs
sudo npm install n -g
sudo /usr/local/bin/n 14.18.3 // update nodejs
sudo npm install npm -g
sudo npm install yarn -g
sudo npm install @quasar/cli -g
sudo npm install cordova -g
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz // download python3.9.5
sudo tar -zxvf Python-3.9.5.tgz
cd Python-3.9.5/
sudo ./configure --enable-optimizations
sudo make altinstall
sudo mv /usr/bin/python3 /usr/bin/python3.bak // backup python3
sudo ln -s /usr/local/bin/python3.9 /usr/bin/python3
sudo mv /usr/bin/pip3 /usr/bin/pip3.bak // backup pip3
sudo ln -s /usr/local/bin/pip3.9 /usr/bin/pip3
sudo yum install git // install git
sudo git clone https://github.com/Singosgu/GreaterWMS.git // clone GreaterWMS from github
sudo chmod -R 755 GreaterWMS
cd GreaterWMS
sudo pip3 install -r requirements.txt
sudo python3 manage.py makemigrations
sudo python3 manage.py migrate
sudo /usr/local/bin/daphne -p 8008 greaterwms.asgi:application
// open Chrom "127.0.0.1:8008/myip", you will get your internal lan ip, remember it 
Ctrl + C // back GreaterWMS folder
cd templates // enter templates folder
sudo /usr/local/bin/yarn install 
sudo /usr/local/bin/quasar d // it will start web site
Ctrl + C // back templates folder
cd src/boot
sudo vim axios_request.js // change request baseurl
// change "127.0.0.1" to your internal IP, baseurl is for http, ws is for websocket
// save it 
sudo /usr/local/bin/quasar build // build your web site
cd .. // back to GreaterWMS folder
sudo /usr/local/bin/daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application
// now，you can use "internal IP:8008" to use greaterwms