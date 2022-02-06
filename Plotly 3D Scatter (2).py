#!/usr/bin/env python
# coding: utf-8

# In[3]:


import plotly.graph_objects as go
import numpy as np
t = np.linspace(0, 50, 100)
x, y, z = np.cos(t), np.sin(t), t
fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=12,
        color= z,               
        colorscale='rainbow',   
        opacity=0.8
    )
)])
fig.update_layout(margin=dict(l=0, r=1, b=5, t=0))
fig.show()

