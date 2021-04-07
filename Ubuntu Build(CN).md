~~~shell
sudo apt update
sudo apt upgrade
sudo apt install vim-gtk // 安装 vim
cd ~ // 到达Home目录
vi .bashrc // 把 "alias vi=vim" 加进 bashrc
source .bashrc // 刷新生效bashrc
sudo apt install git // 安装 git
sudo git clone https://github.com/Singosgu/GreaterWMS.git // 下载 GreaterWMS 从 github
sudo apt install nodejs // 安装 nodejs
sudo apt install npm // 安装 npm
sudo npm install n -g // 安装 n
n stable // 下载 nodejs 的稳定版本
// 你需要确定你的nodejs是12或者14版本，Quasar只支持12或者14版本
// 这步完成以后，你需要重新启动你的Terminal，要不然升级不生效
sudo npm install npm -g // 升级 NPM 到最新版本
sudo npm install yarn -g // 安装 yarn
sudo npm install -g @quasar/cli // 安装 quasar/cli
quasar -v // 检查 Quasar 版本
python3 // 确定你的python版本是3.8以上版本，原则上3.6也是可以的，但是安装库会有些问题
pip3 list // 确定你是否安装有 pip3
sudo apt install python3-pip // 如果你没有pip3 ，就安装一下
pip3 list // 检查下是否安装成功
sudo chmod -R 755 GreaterWMS // 提权 GreaterWMS 文件夹
cd GreaterWMS // 进入GreaterWMS文件夹
sudo pip3 install -r requirements.txt
//  有些时候，你安装这些库会出问题，是因为python3版本的问题，不用担心，sudo pip3 install 出错的库就可以了.
sudo daphne -p 8008 greaterwms.asgi:application
// 现在打开浏览器，输入"127.0.0.1:8008"，你会看到500错误，恭喜你，你已经可以正常部署接下来的事情了
Ctrl + C // 回到GreaterWMS文件夹
sudo python3 manage.py makemigrations // 数据库生成
sudo python3 manage.py migrate // 数据库迁移
sudo daphne -p 8008 greaterwms.asgi:application
// 现在打开浏览器，输入"127.0.0.1:8008"，你会看到项目已经运行了
// 输入 "127.0.0.1:8008/myip", 你会得到你的内网IP，一定记住它 
Ctrl + C // 回到GreaterWMS文件夹
cd templates //进入 templates 文件夹
sudo yarn install // 等待Yarn安装完成，其实你也可以sudo npm install ，就是会慢一点
sudo quasar d // 使用quasar命令启动前端页面
// 前端会向 "127.0.0.1:8008"发请求, 在这里我们只是看下项目是不是可以运行
Ctrl + C // 退回到templates文件夹
cd src/boot // 进入在src/boot文件夹
sudo vim axios_requests.js // 我们开始更改请求地址
// 更改 "127.0.0.1" 成你的内网IP, baseurl 是http请求地址 , ws 是 websocket请求地址
按下 Esc 然后输入 ":wq" 去保存修改
// 现在，你已经知道怎么部署和修改请求地址了
sudo quasar build // 需要对修改进行重新打包
cd .. // 回到GreaterWMS文件夹
sudo daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application
// 现在，打开浏览器，输入 "你的内网IP:8008"，你可以看到项目已经运行了

谢天谢地!!!

顺便说一句
1. 你知道了怎么修改请求地址
2. 你也可以按你的喜好，去更改Port
3. 你更可以使用Nginx或者Apache，把项目发布到互联网上
~~~

