#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# importing clean data for analysis


# In[3]:


data = pd.read_csv(r"C:\Users\Sindhu reddy\Downloads\Frailty Analysis Data.csv")

print(data)


# In[4]:


data.info()


# In[5]:


import matplotlib.pyplot as plot
import numpy as np
import seaborn as sns


# In[6]:


sns.lineplot(x='Age', y='Grip Strength', data=data)
plot.title('Age Vs Grip Strength')
plot.xlabel('Age')
plot.ylabel('Grip Strength')
plot.savefig(r"C:\Users\Sindhu reddy\Downloads/agevsgrip.png")
plot.show()


# In[8]:


sns.scatterplot(x='Height', y='Grip Strength', data=data)
plot.title('Height Vs Grip Strength')
plot.xlabel('Height')
plot.ylabel('Grip Strength')

# Save the plot as a PNG file
plot.savefig(r"C:\Users\Sindhu reddy\Downloads\heightvsgrip.png")

# Display the plot
plot.show()


# In[17]:


sns.distplot(data['Age'], kde = False, color ='green', bins = 50)
fig = plot.gcf()
fig.savefig(r"C:\Users\Sindhu reddy\Downloads\Age_Distribution.png")


# In[22]:


ax = data.plot.scatter(x='Weight',y='Grip Strength')
fig=ax.get_figure()
fig.savefig(r"C:\Users\Sindhu reddy\Downloads\/GripStrength_Weight_Relation.png")

