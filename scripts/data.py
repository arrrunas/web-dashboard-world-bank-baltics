import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.colors
from collections import OrderedDict
import requests

country_list = OrderedDict([('Lithuania', 'LTU'), ('Estonia', 'EST'), ('Latvia', 'LVA'), 
  ('Euro Area', 'XC'), ('Central Europe and the Baltics', 'B8')])

def return_figures(countries=country_list):
    if not bool(countries):
        countries = country_list

    country_filter = list(countries.values())
    country_filter = [x.lower() for x in country_filter]
    country_filter = ';'.join(country_filter)

    indicators = ['NY.GDP.PCAP.CD', 'FP.CPI.TOTL.ZG', 'GC.XPN.TOTL.GD.ZS', 'BX.KLT.DINV.CD.WD']

    data_frames = []
    urls = []

    for indicator in indicators:
        url = 'http://api.worldbank.org/v2/countries/' + country_filter + \
        '/indicators/' + indicator + '?date=1993:2018&per_page=1000&format=json'
        urls.append(url)

        try:
            r = requests.get(url)
            data = r.json()[1]
        except:
            print('could not load data ', indicator)

        for i, value in enumerate(data):
            value['indicator'] = value['indicator']['value']
            value['country'] = value['country']['value']

        data_frames.append(data)

### GRAPH 1: GDP PER CAPITA

    graph_one = []
    df_one = pd.DataFrame(data_frames[0])

    df_one.sort_values('date', ascending=False, inplace=True)

    countryList = df_one.country.unique().tolist()

    for country in countryList:
        x_val = df_one[df_one['country'] == country].date.tolist()
        y_val = df_one[df_one['country'] == country].value.tolist()
        graph_one.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = country
            )
        )

    layout_one = dict(title = 'GDP per capita',
                    xaxis = dict(title = 'Year'),
                    yaxis = dict(title = 'current US$')
                    )

### GRAPH 2: INFLATION

    graph_two = []
    df_two = pd.DataFrame(data_frames[1])

    df_two = df_two[df_two['date'] >= '2000']
    df_two.sort_values('date', ascending=False, inplace=True)

    countryList = df_two.country.unique().tolist()

    for country in countryList:
        x_val = df_two[df_two['country'] == country].date.tolist()
        y_val = df_two[df_two['country'] == country].value.tolist()
        graph_two.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = country
            )
        )

    layout_two = dict(title = 'Inflation, consumer prices (annual %)',
                    xaxis = dict(title = 'Year'),
                    yaxis = dict(title = '%')
                    )

    # append all charts
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    #figures.append(dict(data=graph_three, layout=layout_three))
    #figures.append(dict(data=graph_four, layout=layout_four))

    return figures