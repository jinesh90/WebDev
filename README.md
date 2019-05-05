# Docker Commands

### Get docker information / to check docker is installed or not.
1) `docker info`

###  Get hello world docker image from repository and run
1)  - `docker run hello-world`


### Login to docker account from CLI.
1) - `docker login` 												 *this will login to docker account , need to apply username,password.*

### get alpine linux image and run shell
1) - `docker run -it alpine sh`
2) - `docker run -it ubuntu sh`

### build docker image help
1)  - `docker image --help` 
2)  - `docker image build -t <image_name>:<version>`                  *# -t for tag image, note here you must have a valid DockerFile in folder.*
3)  - `docker image ls   	`						                  *# to list all docker images.*
4)  - `docker image rm <image_name:tag>  `                            *# remove image*
5)  - `docker image tag <image1:latest> <image2:latest>`              *# creating image with tag.*
6)  - `docker image rm -f <image_name:tag> 		 `                 *# remove image forcefully.*
7)  - `docker image push <image_name:tag>  `		                  *# push image to repo.*
8)  - `docker image pull <image_name:tag>  		`                  *# pull image from repo.*


### docker container commands
1)  - `docker container ls `                                          *# list all running containers.*
2)  -`docker container ls  -a `                                      *# list all containers including stopped ones.*
3)  -`docker container run -it `                                     *# this flag for adding linux commands in container.*
    - `-e`                                        *# passing environmental variable to docker.*
	- `-p host:container`                         *# for bind port docker conatiner,host and container.*
	- `--name <name>`                             *# pass container name or docker will select random name.*
	- `-- rm` 			      *# remove container and recreated new one.*
	- `-d`                    *# detach container from cmd so terminal will be used(equivalent to running image to background & equivalent of linux.)*
	- `--restart on-failure`  *# restart docker on catastropic event automatically.*
	- `-v`                    *# attach volume like map directory to container -v $PWD:/app <- this will map /app to container and change reflects.*
	- `--net <network_name>`  *# attatch netwok with container.*

4)  - `docker container stop <container_id> or <container_name>`      *# stop running container.*
5)  - `docker container start <container_id> or <container_name> `    *# start container.*
6)  - `docker container rm  <container_id> or <container_name> `      *# remove docker container.*
7)  - `docker conatiner logs <container_id> or <container_name>`      *# see the logs of running container.*
    - `docker conatiner logs -f <container_id> or <container_name>`   *# see the logs of running container in real time in foreground.*
8)  - `docker container stats 		`								  *# see the container stats.*
9)  - `docker container prune     `                                   *# remove all stopped container.*
10) - `docker container pause <container_id> or <container_name>`     *# pause running container.*
11) - `docker container inspect <container_id> or <container_name>`   *# inspect container*


### docker netwroking commands
1)  - `docker network inspect <network_name>`                          *# get detail about docker network.*
2)  - `docker network create` 

### docker linux command execution
1) - `docker exec <container_name> <linux command>`                    *# example docker exec web ifconfig, docker exec web ls*

### docker volume mounting for database persistance.
1)  - `docker volume create <volume_name>      `                       *# create vloume on local instance that can save database for persistance.*
2)  - `docker volume ls       `                                        *# list all volumes.*
3)  - `docker volume inspect <volume_name>	`						   *# inspect docker voulme.*

### docker system commands
1)  - `docker system df`                                               *# check docker files volume.*
2)  - `docker system info`                                             *# create docker system information*
3)   -`docker system prune`                                            *# delete all dangling images,container and networks.*


### Docker Compose
1) - `docker-compose --help`                                           *# help command for docker compose.*


### DockerFile commands, Creating DockerFile File.

- `FROM python:latest` 												   *# get docker image from docker repo.*
- `RUN mkdir abc`      											       *# run command on OS, like Linux mkdir.*
- `WORKSDIR abc`      												 *# set working directory.*
- `COPY . /abc`       												 *# copy perticular file from source to destination*
- `CMD run.sh`        												 *# execute command after build.*
- `VOLUME ["app/public"]`                                            *# mount common volume for container access*


