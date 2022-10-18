

from plotly.tools import mpl_to_plotly

import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dash.register_page(__name__)

df = pd.read_csv('../extracted_data_vis4.csv')
# DATA LOADING CELL
# data_path = "../Crimedata.csv"# change for now
data_path = '../extracted_data_vis4.csv'# change for now

col_dict = {
'V1263': 'Alcohol_ever',
'V1300' : 'Marijuana_ever',
'V1294' : 'Heroin_ever',
'V1301' : 'Cocaine_ever',
'V1267': 'Alcohol',
'V1266' : "Alcohol_12months",
 'V1327': 'Marijuana',
 'V1315' : 'Marijuana_30days',
 'V1339' : 'Marijuana_12months',
 'V1330': 'Heroin',
 'V1318' : 'Heroin_30days',
 'V1342' : 'Heroin_12months',
 'V1328': 'Cocaine',
 'V1316': 'Cocaine_30days',
 'V1340': 'Cocaine_12months',
 'RV0001': 'Age',
 'RV0003': 'Race',
 'RV0005': 'Sex',
 'V0772': 'State'}
data = pd.read_csv(data_path) 
data.rename(columns=col_dict,inplace=True)
total_count = 24848

m_12 = data.Marijuana_12months.value_counts()
m_now = data.Marijuana.value_counts()
m_ever = data.Marijuana_ever.value_counts()

h_12 = data.Heroin_12months.value_counts()
h_now = data.Heroin.value_counts()
h_ever = data.Heroin_ever.value_counts()

c_12 = data.Cocaine_12months.value_counts()
c_now = data.Cocaine.value_counts()
c_ever = data.Cocaine_ever.value_counts()

# now, 12 months ago, earlier than 12 months ago, never, don't know
print(m_ever[1])
marijuana_values = [
    m_now[0],
    len(df[(df['Marijuana'] != '(1) 1 = Yes') & (df['Marijuana_12months']=='(1) 1 = Yes')]),
    len(df[(df['Marijuana'] != '(1) 1 = Yes') & (df['Marijuana_12months']!='(1) 1 = Yes') & (df['Marijuana_ever'] == '(1) 1 = Yes')]),
    m_ever[1],
    total_count - m_ever[0] - m_ever[1]
]

cocaine_values = [
    c_now[1],
    len(df[(df['Cocaine'] != '(1) 1 = Yes') & (df['Cocaine_12months']=='(1) 1 = Yes')]),
    len(df[(df['Cocaine'] != '(1) 1 = Yes') & (df['Cocaine_12months']!='(1) 1 = Yes') & (df['Cocaine_ever'] == '(1) 1 = Yes')]),
    c_ever[1],
    total_count - c_ever[0] - c_ever[1]
]

print('gergegege', h_ever[1], h_now[1] +
    len(df[(df['Heroin'] != '(1) 1 = Yes') & (df['Heroin_12months']=='(1) 1 = Yes')])+
    len(df[(df['Heroin'] != '(1) 1 = Yes') & (df['Heroin_12months']!='(1) 1 = Yes') & (df['Heroin_ever'] == '(1) 1 = Yes')]),
    )

heroin_values = [
    h_now[1],
    len(df[(df['Heroin'] != '(1) 1 = Yes') & (df['Heroin_12months']=='(1) 1 = Yes')]),
    len(df[(df['Heroin'] != '(1) 1 = Yes') & (df['Heroin_12months']!='(1) 1 = Yes') & (df['Heroin_ever'] == '(1) 1 = Yes')]),
    h_ever[0],
    total_count - h_ever[0] - h_ever[1]
]

print(sum(marijuana_values), sum(heroin_values), sum(cocaine_values))

print(marijuana_values, heroin_values, cocaine_values)

category_names = ['When Imprisoned', '12 Months Prior', 'More Than 12 Months Prior', 'Never', "Unknown"]
results = {
    'Mairjuana': marijuana_values,
    'Cocaine': cocaine_values,
    'Heroin': heroin_values
}


def survey(results, category_names, title):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('magma')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_title('title')
    
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            ax.text(x, y, str(int(c)), ha='center', va='center',
                    color=text_color)
    fig.suptitle(title)  
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')
    return fig, ax
#https://stackoverflow.com/questions/7908636/how-to-add-hovering-annotations-to-a-plot
survey(results, category_names, 'Drug Usage Among All Prisoners')
#https://stackoverflow.com/questions/7908636/how-to-add-hovering-annotations-to-a-plot



fig, ax = survey(results, category_names, 'Drug Usage Among All Prisoners')

plotly_fig = mpl_to_plotly(fig)

layout= html.Div([
    dcc.Graph(id= 'matplotlib-graph', figure=plotly_fig)

])