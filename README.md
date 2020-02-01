## Link to hosted [dashboard](https://wb-baltics-dashboard-prototype.herokuapp.com)

# World Bank API Data Dashboard - Baltics
Web dashboard prototype that visualises data from the world bank API. Data is pulled directly from the API, wrangled using pandas and then visualised using Plotly. The web app is hosted on Heroku.

The dashboard shows sample economic indicators for the Baltic countries.

# Contents
* `wb_web_dasdhboard` - folder containing Anaconda virtualenv with prerequisites
* `wb-baltics-dashboard-prototype` - folder containing the web dashboard

# Prerequisites
To install the flask app, you need:

* python3
* python packages in the requirements.txt file

Install the packages with

`pip install -r requirements.txt`

# Installing

On macOS/linux system, go to the `wb-baltics-dashboard-prototype` folder, open `worldbank.py`, uncomment the commented line, then run python worldbank.py in the terminal. 
