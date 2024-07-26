#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# importing clear data for analysis


# In[3]:


# establishing a new column calculating the percentage from the three available scores and grading using the average scores


# In[4]:


df = pd.read_csv(r"C:\Users\Sindhu reddy\Downloads\StudentsPerformance.csv")

print(df.to_string())


# In[5]:


df["Percentage"]=(df["math score"]+df["reading score"]+df["writing score"])/3
print(df["Percentage"])


# In[6]:


df['Percentage'] = (df['math score']+df['reading score']+df['writing score'])/3
print(df["Percentage"])


def Grade(Percentage):
    if (Percentage >= 95):return 'O'
    if (Percentage >= 81):return 'A'
    if (Percentage >= 71):return 'B'
    if (Percentage >= 61):return 'C'
    if (Percentage >= 51):return 'D'
    if (Percentage >= 41):return 'E'
    else: return 'F'
    
df["grade"] = df.apply(lambda x : Grade(x["Percentage"]),axis=1)


# In[7]:


print(df)


# In[8]:


# using Seaborn for analysis


# In[9]:


import seaborn as sns
import numpy as np


# In[34]:


sns.barplot(x ='gender', y ='Percentage', data = df,
            palette ='plasma', estimator = np.std)


# In[11]:


df['gender'].value_counts()


# In[12]:


import matplotlib.pyplot as plot


# In[17]:


lunchCount = df['lunch'].value_counts()
print(lunchCount)


# In[18]:


plot.figure(figsize=(4,4))
plot.pie(lunchCount, labels=lunchCount.index)
plot.title("Types of Lunch Distribution")
plot.savefig(r"C:\Users\Sindhu reddy\Downloads/lunchdistribution.png")
plot.show()


# In[ ]:


# Below countplot illustares the grade secured by female and male 


# In[19]:


plot.plot(df['reading score'], df['writing score'], marker='o')

# Add labels and title
plot.xlabel('Reading Score')
plot.ylabel('Writing Score')
plot.title('Reading VS Writing Scores')

# Save the plot as a PNG file
plot.savefig(r"C:\Users\Sindhu reddy\Downloads/readingvswriting.png")

# Display the plot
plot.show()


# In[29]:


plot.hist(df['writing score'], bins=25, color='blue',edgecolor='black')
plot.xlabel('Writing Score')
plot.ylabel('Numbers')
plot.title("Writing Score Numbers")
plot.savefig(r"C:\Users\Sindhu reddy\Downloads/writingscorenumbers.png")
plot.show()


# In[40]:


sns.boxplot(x='gender', y='writing score', data=df)
plot.xlabel('Gender')
plot.ylabel('Writing Score')
plot.title("Reading Score By Gender")
plot.savefig(r"C:\Users\Sindhu reddy\Downloads/writingscorebygender.png")
plot.show()


# In[44]:


ax=sns.distplot(df['Percentage'], kde = False, color ='red', bins = 20)
fig=ax.get_figure()
fig.savefig(r"C:\Users\Sindhu reddy\Downloads\Distribution_percentage.png")


# In[52]:


ax = sns.jointplot(x='Percentage', y='reading score', data=df, kind='hex', cmap='Blues')

# Save the plot as a PNG file
plot.savefig(r"C:\Users\Sindhu reddy\Downloads\Hexbin_Plot.png")

# Display the plot
plot.show()


# In[53]:


g = sns.FacetGrid(df, col='gender', col_wrap=3, height=4, aspect=1.2)

# Map a scatter plot onto the FacetGrid
g.map(sns.scatterplot, 'Percentage', 'reading score')

# Add titles and labels
g.set_axis_labels('Percentage', 'Reading Score')
g.set_titles(col_template='{col_name}')

