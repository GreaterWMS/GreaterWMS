Deploy greaterwms under docker (this document is applicable to users with docker Foundation)

1. Install or Upgrade Docker Client

```
	curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
	//If you are prompted that there is no curl, execute sudo apt install curl or yum - y install curl
```

2. Install Docker Compose

   	sudo curl -L "https://get.daocloud.io/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   	sudo chmod +x /usr/local/bin/docker-compose

3. Verify that docker is installed successfully

   //view docker version
   
   ```
   docker -v 
   Docker version 20.10.8, build 3967b7d //You can see this, which indicates that the docker installation is successful
   ```
   
   //查看docker-compose版本
   
   ```
   docker-compose -v docker-compose version 1.16.1, build 6d1ac21 //This indicates that the docker compose installation is successful
   ```
   
   //Verify that the docker service is started
   
   sudo systemctl status docker
   
   //If docker service is stop or failed, please try to start docker first
   
   sudo systemctl start docker
   
4. Use docker to directly test run the project (non secondary development, user trial, no need to clone the project from GitHub)

   ```
   docker run -itd --name greaterwms_v2.0.25 -p 8008:8008 -d silence2022/greaterwms:v2.0.25
   ```


4. Install git

```
//Install git under Ubuntu
apt-get install git
//Install git under CentOS
yum install git
```

5. It is suitable for long-term data storage (code needs to be stored on the user server) and secondary development

```English
//glone code
git clone https://github.com/Singosgu/GreaterWMS.git
//you need to modify the contents of baseurl.js before running the project
vim templates/public/static/baseurl.js //change 127.0.0.1 to the IP address of the server
docker-compose up -d
//view the mirror operation log
docker logs -f greaterwms:v2.0.25
//view the back-end mirror operation log
docker logs -f greaterwms_backend_v2.0.25
//Special note: after executing docker compose up - D, the front-end dependencies will be automatically downloaded. Sometimes the download fails, resulting in the front-end unable to start. At this time, first execute docker-compose down and then docker-compose up -d to download again until it succeeds.
```

6. compile front-end code

```English
//glone code
git clone https://github.com/Singosgu/GreaterWMS.git
//you need to modify the contents of baseurl.js before running the project
vim templates/public/static/baseurl.js //change 127.0.0.1 to the IP address of the server
docker-compose up -d
//view the mirror operation log
docker logs -f greaterwms:v2.0.25
//view the back-end mirror operation log
docker logs -f greaterwms_backend_v2.0.25
```

6. Access portal

```English
//Front end access portal
http://服务器IP:8008
//Back end access portal
http://服务器IP:8080

```
