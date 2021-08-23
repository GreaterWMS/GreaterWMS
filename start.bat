echo "欢迎进入GreaterWMS！！"
echo "开始安装Python-3.9"
cd ../
python-3.9.2-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
echo "Python-3.9安装完成"
echo "验证python是否安装正确"
python -V
echo "升级pip版本"
python -m pip install --upgrade pip
echo "安装Twisted"
pip3 install Twisted-20.3.0-cp39-cp39-win_amd64.whl
echo "进入项目"
cd GreaterWMS
echo "安装依赖"
pip3 install -r requirements.txt
echo "初始化"
python manage.py makemigrations
python manage.py migrate
echo "安装完成"
pause