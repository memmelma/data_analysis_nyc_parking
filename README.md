# data_analysis_nyc_parking
Data analysis of NYC parking tickets

## setup:
### UPDATE!
- Feather format for faster reading-ops
### 1.
- .gitignore includes data folder
- csv-files have to be downloaded and placed in the following subfolder 'data\nyc_parking_tickets'
### 2.
- initialize the jupyter notebook on localhost:8888 and attach the git-repository as root directory
- `docker run -it --rm -p 8888:8888 -v C:/[path to git repository]:/home/jovyan/work jupyter/datascience-notebook`
- maybe make a .bat out of it? ;)
### 3.
- open and run the following script to install the dependencies 'scripts/install_modules'
- sick of installing modules every time you start the notebook?
#### 3.1
- open fresh notebook
#### 3.2
- `docker commit [container id] jupyter/datascience-notebook`
## data source:
- https://www.kaggle.com/new-york-city/nyc-parking-tickets
## installed modules:
- Gmaps:	https://github.com/pbugnion/gmaps
- GoogleMapsAPI: googlemaps
- Folium: https://folium.readthedocs.io/en/latest/
- Feather: https://pypi.python.org/pypi/feather-format
## docker image used:
- juypter/datascience-notebook
- https://hub.docker.com/r/jupyter/datascience-notebook/
## commands:
### show docker container
- `docker container ls [--all]`
### show docker images
- `docker image ls [--all]`
### access bash of the jupyter-notebook
- `docker exec -it [container_id]  /bin/bash`
### stop and remove all docker containers
- `docker stop $(docker ps -a -q)`
- `docker rm $(docker ps -a -q)`


