~~~shell
su - // 进入管理员账号
chmod u+w /etc/sudoers // 提权更改
vim /etc/sudoers // 把 "{{ your username }} ALL=(ALL) ALL" 这个加进去，保存
chmod u-w /etc/sudoers // 取消提权
restart // 重启
sudo yum update
sudo yum upgrade
sudo yum -y install gcc-c++ // 安装依赖
sudo yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel libffi-devel gcc make // 安装python依赖
sudo yum install nodejs // 安装nodejs
sudo npm install n -g // 安装n
sudo /usr/local/bin/n stable // 升级nodejs
sudo npm install npm -g // 升级npm
sudo npm install yarn -g // 安装yarn
sudo npm install @quasar/cli -g // 安装quasar
quasar -v // 检查 Quasar 版本
python3 // 查看python版本
cd /usr/src // 进入src
sudo wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz // 下载python3.9.2
sudo tar -zxvf Python-3.9.2.tgz // 解压
cd Python-3.9.2/ // 进入目录
sudo ./configure --enable-optimizations // 编译
sudo make altinstall  // 安装
mv /usr/bin/python3 /usr/bin/python3.bak // 备份
ln -s /usr/local/bin/python3.9 /usr/bin/python3 // 建立软连接
mv /usr/bin/pip3 /usr/bin/pip3.bak // 备份
ln -s /usr/local/bin/pip3.9 /usr/bin/pip3  // 建立软连接
python3 // 查看python版本
pip3 list // 查看pip3 是否安装成功
sudo yum install git // 安装git
sudo git clone https://github.com/Singosgu/GreaterWMS.git // 下载 GreaterWMS 从 github
sudo chmod -R 755 GreaterWMS // 提权 GreaterWMS 文件夹
cd GreaterWMS // 进入GreaterWMS文件夹
sudo pip3 install -r requirements.txt
//  有些时候，你安装这些库会出问题，是因为python3版本的问题，不用担心，sudo pip3 install 出错的库就可以了.
sudo /usr/local/bin/daphne -p 8008 greaterwms.asgi:application
// 现在打开浏览器，输入"127.0.0.1:8008"，你会看到500错误，恭喜你，你已经可以正常部署接下来的事情了
Ctrl + C // 回到GreaterWMS文件夹
sudo python3 manage.py makemigrations // 数据库生成
sudo python3 manage.py migrate // 数据库迁移
sudo /usr/local/bin/daphne -p 8008 greaterwms.asgi:application
// 现在打开浏览器，输入"127.0.0.1:8008"，你会看到项目已经运行了
// 输入 "127.0.0.1:8008/myip", 你会得到你的内网IP，一定记住它 
Ctrl + C // 回到GreaterWMS文件夹
cd templates //进入 templates 文件夹
sudo yarn install // 等待Yarn安装完成，其实你也可以sudo npm install ，就是会慢一点
sudo /usr/local/bin/quasar d // 使用quasar命令启动前端页面
// 前端会向 "127.0.0.1:8008"发请求, 在这里我们只是看下项目是不是可以运行
Ctrl + C // 退回到templates文件夹
cd src/boot // 进入在src/boot文件夹
sudo vim axios_request.js // 我们开始更改请求地址
// 更改 "127.0.0.1" 成你的内网IP, baseurl 是http请求地址 , ws 是 websocket请求地址
按下 Esc 然后输入 ":wq" 去保存修改
// 现在，你已经知道怎么部署和修改请求地址了
sudo /usr/local/bin/quasar build // 需要对修改进行重新打包
cd .. // 回到GreaterWMS文件夹
sudo /usr/local/bin/daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application
// 现在，打开浏览器，输入 "你的内网IP:8008"，你可以看到项目已经运行了

谢天谢地!!!

顺便说一句
1. 你知道了怎么修改请求地址
2. 你也可以按你的喜好，去更改Port
3. 你更可以使用Nginx或者Apache，把项目发布到互联网上
~~~

