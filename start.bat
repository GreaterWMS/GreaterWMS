echo "欢迎进入GreaterWMS"
echo "安装python"
python-3.9.2-amd64.exe /quiet InstallAllUers=1 PrependPath=1 Include_test=0
echo 验证python是否安装正确
python -V
echo "升级pip"
python -m pip install --upgrade pip
echo "安装Twisted库"
pip3 install Twisted-20.3.0-cp39-cp39-win_amd64.whl
echo "安装项目依赖"
pip3 install -r requirements.txt
echo "初始化"
python manage.py makemigrations
python manage.py migrate
pause

