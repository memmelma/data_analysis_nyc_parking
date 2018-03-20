# data_analysis_nyc_parking
Data analysis of NYC parking tickets

#setup:
#1.  
#.gitignore includes data folder
#csv-files have to be downloaded and placed in the following subfolder 'data\nyc_parking_tickets'

#2
#initialize the jupyter notebook on localhost:8888 and attach the git-repository as root directory
docker run --rm -p 8888:8888 -v C:/[path to git repository]:/home/jovyan/work jupyter/datascience-notebook

#docker image used: 
juypter/datascience-notebook

#commands:

#show docker container
docker container ls [--all]

#show docker images
docker image ls [--all]

#access bash of the jupyter-notebook
docker exec -it [container_id]  /bin/bash

#stop and remove all docker containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

