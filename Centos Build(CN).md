~~~shell
su - // 进入管理员账号
yum update
yum upgrade
yum -y install gcc-c++ // 安装依赖
yum install zlib-devel xz-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel libffi-devel gcc make // 安装python依赖
yum install nodejs // 安装nodejs
npm install n -g // 安装n
/usr/local/bin/n 14.18.3 // 升级nodejs
npm install npm -g // 升级npm
npm install yarn -g // 安装yarn
npm install @quasar/cli -g // 安装quasar
npm install cordova -g // 安装cordova
quasar -v // 检查 Quasar 版本
python3 // 查看python版本
cd /usr/src // 进入src
wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz // 下载python3.9.5
tar -zxvf Python-3.9.5.tgz // 解压
cd Python-3.9.5/ // 进入目录
./configure --enable-optimizations // 编译
make altinstall  // 安装
mv /usr/bin/python3 /usr/bin/python3.bak // 备份
ln -s /usr/local/bin/python3.9 /usr/bin/python3 // 建立软连接
mv /usr/bin/pip3 /usr/bin/pip3.bak // 备份
ln -s /usr/local/bin/pip3.9 /usr/bin/pip3  // 建立软连接
python3 // 查看python版本
pip3 list // 查看pip3 是否安装成功
yum install git // 安装git
git clone https://github.com/Singosgu/GreaterWMS.git // 下载 GreaterWMS 从 github
chmod -R 755 GreaterWMS // 提权 GreaterWMS 文件夹
cd GreaterWMS // 进入GreaterWMS文件夹
pip3 install -r requirements.txt
//  有些时候，你安装这些库会出问题，是因为python3版本的问题，不用担心，pip3 install 出错的库就可以了.
/usr/local/bin/daphne -p 8008 greaterwms.asgi:application
// 现在打开浏览器，输入"127.0.0.1:8008"，你会看到500错误，恭喜你，你已经可以正常部署接下来的事情了
Ctrl + C // 回到GreaterWMS文件夹
python3 manage.py makemigrations // 数据库生成
python3 manage.py migrate // 数据库迁移
/usr/local/bin/daphne -p 8008 greaterwms.asgi:application
// 现在打开浏览器，输入"127.0.0.1:8008"，你会看到项目已经运行了
// 输入 "127.0.0.1:8008/myip", 你会得到你的内网IP，一定记住它 
Ctrl + C // 回到GreaterWMS文件夹
cd templates //进入 templates 文件夹
/usr/local/bin/yarn install // 等待Yarn安装完成，其实你也可以npm install ，就是会慢一点
yarn config set registry https://registry.npmmirror.com/  //更改yarn为国内源
/usr/local/bin/quasar d // 使用quasar命令启动前端页面
// 前端会向 "127.0.0.1:8008"发请求, 在这里我们只是看下项目是不是可以运行
Ctrl + C // 退回到templates文件夹

从2.0.19版本以后，优化了请求地址修改方式，直接修改templates/dist/spa/statics/baseurl.js，中的baseurl和wsurl，就可以成功更改前端请求地址，不再需要做下面的quasar build打包工作。

如果需要修改前端内容，则还需要修改templates/public/statics/baseurl.js中的baseurl和wsurl，然后重新使用quasar build进行打包

cd src/boot // 进入在src/boot文件夹
vim axios_request.js // 我们开始更改请求地址
// 更改 "127.0.0.1" 成你的内网IP, baseurl 是http请求地址 , ws 是 websocket请求地址
按下 Esc 然后输入 ":wq" 去保存修改
// 现在，你已经知道怎么部署和修改请求地址了
/usr/local/bin/quasar build // 需要对修改进行重新打包
cd .. // 回到GreaterWMS文件夹
/usr/local/bin/daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application
// 现在，打开浏览器，输入 "你的内网IP:8008"，你可以看到项目已经运行了

谢天谢地!!!

顺便说一句
1. 你知道了怎么修改请求地址
2. 你也可以按你的喜好，去更改Port
3. 你更可以使用Nginx或者Apache，把项目发布到互联网上
~~~

