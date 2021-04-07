~~~shell
sudo apt update
sudo apt upgrade
sudo apt install vim-gtk // install vim
cd ~ // Go to home follder
vi .bashrc // add "alias vi=vim" in bashrc
source .bashrc // refresh bashrc
sudo apt install git // install git
sudo git clone https://github.com/Singosgu/GreaterWMS.git // Download GreaterWMS from github
sudo apt install nodejs // install nodejs
sudo apt install npm // install npm
sudo npm install n -g // update n
n stable // Download nodejs to stable version
// You must confirm your nodejs version is 14 or 12 , cause Quasar just support 12 or 14
// after this step , you should re-open your terminal
sudo npm install npm -g // update npm to latestest
sudo npm install yarn -g // install yarn
sudo npm install -g @quasar/cli // install quasar/cli
quasar -v // check quasar version
python3 // To check your python version is 3.8 above
pip3 list // To check whether you have pip3
sudo apt install python3-pip // if you don't have pip3 , install it
pip3 list // check again
sudo chmod -R 755 GreaterWMS // approve GreaterWMS chmod
cd GreaterWMS
sudo pip3 install -r requirements.txt
//  Some times , you can not install some lib . Cause your python3 version . Don't worry, sudo pip3 install it is ok.
sudo daphne -p 8008 greaterwms.asgi:application
// Now, Open the brower and enter "127.0.0.1:8008", If you see 500 error . Congratuation, you success.
Ctrl + C // out to terminal
sudo python3 manage.py makemigrations // database create
sudo python3 manage.py migrate // database create
sudo daphne -p 8008 greaterwms.asgi:application
// Now, Open the brower and enter "127.0.0.1:8008". You can see our project run
// Now , Enter "127.0.0.1:8008/myip", you will get Intranet ip, recorde it 
Ctrl + C // out to terminal
cd templates // Go to templates follder
sudo yarn install // Waiting for yarn install
sudo quasar d // run quasar web
// quasar web will send request to "127.0.0.1:8008", this step just to check whether it can be run
Ctrl + C // out to terminal
cd src/boot // go to boot follder
sudo vim axios_requests.js // go to this file to change the request link
// change "127.0.0.1" to your Intranet ip , baseurl is for http , ws is for websocket
Esc then enter ":wq" to save the change
// till now you know how to build it and change the request
sudo quasar build // Re-Build the Quasar Web
cd .. // back to greaterwms follder
sudo daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application
// Now, Open the brower and enter "your Intranet ip:8008". You can see our project run

Congratuation!!!

By The Way
1. You Know how to change the request
2. You also can change the port which you like
3. You can use Nginx or Apache to run the project on internet
~~~

