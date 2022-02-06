#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
import numpy as np

fig = go.Figure(data=[go.Scatter3d(
   x =[1,2,3,4,5,6,7,8,9,10],
y =[5,6,2,3,13,4,1,2,4,8],
z =[2,3,3,3,5,7,9,11,9,10],
    mode='markers',
    marker=dict(
        size=[15,20,25, 30,15,20,25, 30,15,20],
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)', 'rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)', 'rgb(93, 164, 214)', 'rgb(255, 144, 14)'],  showscale = True
    )
)])
fig.update_layout(margin=dict(l=0, r=1, b=5, t=0))
fig.show()

