Deploy greaterwms under docker (this document is applicable to users with docker Foundation)

1. Install or Upgrade Docker Client

```
	curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
	//If you are prompted that there is no curl, execute sudo apt install curl or yum - y install curl
```

2. Install Docker Compose

   	sudo curl -L "https://get.daocloud.io/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   	sudo chmod +x /usr/local/bin/docker-compose

3. Use docker to directly test run the project (non secondary development, user trial, no need to clone the project from GitHub)

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

5. Applicable to long-term data storage (code needs to be stored on the user's machine)

```English
//glone code
git clone https://github.com/Singosgu/GreaterWMS.git
/enter the project directory and use docker compose up -d to run the project
#you need to modify the contents of baseurl.js before running the project
vim templates/public/static/baseurl.js #change 127.0.0.1 to the IP address of the server
docker-compose up -d
//view the mirror operation log
docker logs -f greaterwms:v2.0.25
```

