~~~shell
su - // Enter root
yum update
yum upgrade
yum -y install gcc-c++
yum install zlib-devel xz-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel libffi-devel gcc make
yum install nodejs
npm install n -g
/usr/local/bin/n 14.18.3 // update nodejs
npm install npm -g
npm install yarn -g
npm install @quasar/cli -g
npm install cordova -g
cd /usr/src
wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz // download python3.9.5
tar -zxvf Python-3.9.5.tgz
cd Python-3.9.5/
./configure --enable-optimizations
make altinstall
mv /usr/bin/python3 /usr/bin/python3.bak // backup python3
ln -s /usr/local/bin/python3.9 /usr/bin/python3
mv /usr/bin/pip3 /usr/bin/pip3.bak // backup pip3
ln -s /usr/local/bin/pip3.9 /usr/bin/pip3
yum install git // install git
git clone https://github.com/Singosgu/GreaterWMS.git // clone GreaterWMS from github
chmod -R 755 GreaterWMS
cd GreaterWMS
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
/usr/local/bin/daphne -p 8008 greaterwms.asgi:application
// open Chrom "127.0.0.1:8008/myip", you will get your internal lan ip, remember it 
Ctrl + C // back GreaterWMS folder
cd templates // enter templates folder
/usr/local/bin/yarn install 
/usr/local/bin/quasar d // it will start web site
Ctrl + C // back templates folder
cd src/boot
vim axios_request.js // change request baseurl
// change "127.0.0.1" to your internal IP, baseurl is for http, ws is for websocket
// save it 
/usr/local/bin/quasar build // build your web site
cd .. // back to GreaterWMS folder
/usr/local/bin/daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application
// now，you can use "internal IP:8008" to use greaterwms