~~~shell
# 下载python3.9.2(版本以自己电脑系统为主，我们以64位为例)
https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe
# 右键，以管理员运行exe文件，安装python3.9.2
# 注意一定要勾选上Add Python3.9 To PATH,然后点选Install Now
# 下载sqlite3(版本以自己电脑系统为主，我们以64位为例)
https://www.sqlite.org/2021/sqlite-dll-win64-x64-3350500.zip
# 解压zip文件，将解压出来的文件，覆盖python路径dll中的文件，地址为
~ C:\Users\{你的用户名}\AppData\Local\Programs\Python\Python39\DLLs
# 下载Node.JS14.16.1(版本以自己电脑系统为主，我们以64位为例)
https://nodejs.org/dist/v14.16.1/node-v14.16.1-x64.msi
# 安装Node.JS的时候，一定不要勾选Automatically，一直下一步，知道安装完成
# 下载Git(版本以自己电脑系统为主，我们以64位为例，需要下载setup版本)
https://git-scm.com/download/win
# 右键，以管理员运行exe文件，然后一直下一步就可以了
# 选择好你要把GreaterWMS摆在哪个目录中，右键，选择Git Bash Here
# 下载 GreaterWMS 从 github,由于网络原因，会很慢，多试几次
git clone https://github.com/Singosgu/GreaterWMS.git
# 左下角搜索栏，输入cmd
# 右键，以管理员运行cmd
# 查看Python版本
python -V
# 查看pip有没有装好
pip list
# 升级pip到最新版本
pip install --upgrade pip
# 进入GreaterWMS摆放目录，演示时摆在downlowad里面的，所以我们进去目录
~  cd C:\Users\{你的用户名}\Downloads\GreaterWMS\
# pip安装python依赖库
pip install -r requirements.txt
# Twisted可能安装不上，需要下载下来手动安装
https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
# 下载自己适合的版本，比如：我的演示视频是Python3.9.2，Win10版本是64位的
# 所以我就要下载Twisted-20.3.0-cp39-cp39-win_amd64.whl
# 将下载下来的Twisted摆在GreaterWMS根目录，手动安装
pip install Twisted-20.3.0-cp39-cp39-win_amd64.whl
# 再次运行安装requirements.txt
pip install -r requirements.txt
# 启动GreaterWMS
daphne -p 8008 greaterwms.asgi:application
# 这时候打开浏览器，输入127.0.0.1:8008
# 如果看到500报错，就说明之前的Python依赖已经全部安装完成了
# 回到CMD界面，按住Ctrl+C来退出项目启动
# 生成数据库迁移文件
python manage.py makemigrations
# 生成数据库
python manage.py migrate
# 再次启动项目
daphne -p 8008 greaterwms.asgi:application
# 这时候打开浏览器，输入127.0.0.1:8008
# 查看局域网IP，浏览器输入127.0.0.1:8008/myip
# 保存或者记住这个IP地址
# 一定注意，windows每次启动获得的内网IP是不同的，要么你路由器设置固定内网IP给这台电脑，要么你就不要关电脑
# 回到CMD界面，按住Ctrl+C来退出项目启动
# 进入templates目录
cd templates

从2.0.19版本以后，优化了请求地址修改方式，直接修改templates/dist/spa/statics/baseurl.js，中的baseurl和wsurl，就可以成功更改前端请求地址，不再需要做下面的quasar build打包工作。

如果需要修改前端内容，则还需要修改templates/public/statics/baseurl.js中的baseurl和wsurl，然后重新使用quasar build进行打包

# 升级下npm
npm install -g npm
# 切换npm源为国内源
npm config set registry https://registry.npm.taobao.org
# 安装Yarn
npm install -g yarn
# 更改yarn为国内源
yarn config set registry https://registry.npm.taobao.org/
# 安装quasar环境
npm install -g @quasar/cli
# 安装windows构建工具
#注意：如果安装不上请下载 Visual Studio 安装C++环境
npm install -g windows-build-tools
# 安装core-js依赖
npm install -g core-js
# 查看全局依赖是否安装完成
npm list -g --depth=0
# 安装项目依赖
yarn install
# 这个过程会有点慢，有时候会很快，是因为网络原因
# 如果发生报错，那是因为网络原因无法安装，多试几次就可以了，直到没有报错
# 进入发请求的文件，修改请求地址
~ 记事本编辑 GreaterWMS/templates/src/boot/axios_request
# 将127.0.0.1更改为你刚才查看到的内网IP
const baseurl = 'http://127.0.0.1:8008/'
const wsurl = 'ws://127.0.0.1:8008/'
# 保存退出
# templates目录下重新编译前端
quasar build
# 回到GreaterWMS根目录
cd ..
# 启动项目加入-b 0.0.0.0参数
daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application
# 接下来就可以使用你的浏览器，访问{ http://内网IP:8008 }来查看该项目了
# 局域网上的电脑也可以通过这个IP来访问项目

谢天谢地!!!

顺便说一句
1. 你知道了怎么修改请求地址
2. 你也可以按你的喜好，去更改Port
3. 你更可以使用Nginx或者Apache，把项目发布到互联网上
~~~

