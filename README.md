# data_analysis_nyc_parking
Data analysis of NYC parking tickets<br />

#setup:<br />
#1<br />
#.gitignore includes data folder<br />
#csv-files have to be downloaded and placed in the following subfolder 'data\nyc_parking_tickets'<br />
<br />
#2<br />
#initialize the jupyter notebook on localhost:8888 and attach the git-repository as root directory<br />
docker run --rm -p 8888:8888 -v C:/[path to git repository]:/home/jovyan/work jupyter/datascience-notebook<br />
<br />
<br />
#docker image used:<br />
juypter/datascience-notebook<br />
<br />
<br />
#commands:<br />
<br />
#show docker container<br />
docker container ls [--all]<br />
<br />
#show docker images<br />
docker image ls [--all]<br />
<br />
#access bash of the jupyter-notebook<br />
docker exec -it [container_id]  /bin/bash<br />
<br />
#stop and remove all docker containers<br />
docker stop $(docker ps -a -q)<br />
docker rm $(docker ps -a -q)<br />
<br />
