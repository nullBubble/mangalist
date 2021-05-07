# mangalist

This is an example project where a Django web application gets automatically tested and deployed with a CICD pipeline.  

This project uses Django, Python, MongoDB and Docker and includes several other files such as an Ansible playbook for configuring and two simple Kubernetes files for the container management.
It can either be run by configuring a server or running a couple containers with the given files.

**Django**

The Django project was written by myself to show some basic understanding Python. 

The website looks like this 

![](Pictures/Home.png)
![](Pictures/Add.png)
![](Pictures/Delete.png)

and can execute the usual CRUD functions, e.g:

1. Add an entry
2. Read an entry
3. Update an entry
4. Delete an entry

The main files lie in mysite/list/.

**Docker**

The Django application can be run as a container in conjunction with a MongoDB instance. Such a MongoDB can be run as a container or locally. A network has to be created for the Docker images to communicate with each other and it can be created with the following command: 

`docker create network mynet`

The following command runs a MongoDB instance as a container:

`docker run -d -p 27017:27017 -v ~/data:/data/db --name mongo --network mynet mongo`

This runs the database in the background on port 27017 with a local volume called at `~/data` and the process is called `mongo`. 

The Django application image is available under https://hub.docker.com/repository/docker/nullbubble/mangalist and can be started with the following Docker command:

`docker run -d --network mynet nullbubble/mangalist:latest` 

which should automatically download the image if it is not locally available.

The Dockerfile is available in the parent directory and is built on an Ubuntu base with a _very_ simple multi stage build to reduce the size. 

To build the image by yourself you have create a network and start a MongoDB container as described above and then execute the following command:

`docker build -t mangalist --network mynet .`

The Django image can only be built if a working database is available at the building process because the database has to be initialized at the building process. The network is needed for the communication between the containers.

**Ansible**

This project also includes an example playbook which configures a server with all the necessary files and technologies to run the Django application by itself, meaning that the server also runs the database locally.

**Kubernetes**

A couple of very basic Kubernetes deployment and service files are available in this project which can be used to start and manage both containers.

**CICD**

A gitlab-ci.yml file is provided in the root folder which tests the Django application by utilizing the built-in test suit with self written tests. If the tests pass successfully the Django image gets uploaded into the Gitlab image repository and and afterwards it logs into a remote server and downloads the recently uploaded image to deploy it to the remote server.
