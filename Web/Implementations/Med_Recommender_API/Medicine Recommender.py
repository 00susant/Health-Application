#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from jupyter_dash import JupyterDash
import plotly.express as px


# In[2]:


df = pd.read_csv('final_test.csv')


# In[3]:


#df.head()


# In[4]:


df = df.loc[1:]


# In[5]:


df = df.reset_index(drop=True)


# In[6]:


#df.head()


# In[7]:



df['total_pred'] = df['total_pred'].astype(float)
df['total_pred'] = np.around(df['total_pred'],decimals=3)


# In[11]:


# Create a dash application
app = JupyterDash(__name__)
JupyterDash.infer_jupyter_proxy_config()
#JupyterDash.infer_jupyter_proxy_config()

app.layout = html.Div(children = [
    # Title
    html.H1('Medicine Recommendation System',
            style = {'textAlign': 'center','color' : '#503D36','font-size': '40px'}),
    
    
    html.Div(['Medical Condition: ', dcc.Input(id = 'condition-text', value = 'ADHD', type ='text', style = {'height':'35px', 'font-size': 25})], style={'font-size': 30}),
    
    html.Br(),
    html.Div(dcc.Graph(id = 'med-importance'), style={'width':'65%'})
])

@app.callback(
    Output(component_id = 'med-importance', component_property = 'figure'),
    Input(component_id = 'condition-text', component_property = 'value')
)

def get_graph(test):
    print(test)
    #img = medication(test)
    
    medicines = df[df['condition']==test].sort_values('total_pred', ascending=False)[:10]
    medicines = medicines.reset_index()
    #print(medicines)
    img = px.bar(medicines, x = 'drugName', y = 'total_pred', width=1500, height=600)
    
    return img




if __name__ == '__main__':
    app.run_server(mode="external", host="localhost", port=7647, debug=True)


# In[ ]:




