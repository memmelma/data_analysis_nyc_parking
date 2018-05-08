# data_analysis_nyc_parking
Data analysis of NYC parking tickets

## setup:
### UPDATE!
- Feather format for faster reading-ops
### 1.
- download the dockerimage jupyter/datascience-notebook
- run the start.bat
### If the batch is NOT working
- initialize the jupyter notebook on localhost:8888 and attach the git-repository as root directory
- `docker run -it --rm -p 8888:8888 -v C:/[path to git repository]:/home/jovyan/work jupyter/datascience-notebook`
### 2.
- download the datasets from Kaggle into the following directory: "data/"
- rename the file of the fiscal year 2014 to "Parking_Violations_Issued_-_Fiscal_Year_2014.csv"
### 3.
- open and run the following script to install the dependencies 'scripts/install_modules'
### 4.
- Scripts are stored in the scripts-folder
- Data is stored in the data-folder
## data source:
- https://www.kaggle.com/new-york-city/nyc-parking-tickets
## installed modules:
- Gmaps:	https://github.com/pbugnion/gmaps
- GoogleMapsAPI: googlemaps
- Folium: https://folium.readthedocs.io/en/latest/
- Feather: https://pypi.python.org/pypi/feather-format
- plotly: https://plot.ly/
- cufflinks: https://plot.ly/ipython-notebooks/cufflinks/
## docker image used:
- juypter/datascience-notebook
- https://hub.docker.com/r/jupyter/datascience-notebook/
