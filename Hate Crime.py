#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("NYPD_Hate_Crimes.csv")
df.head(2)


# In[3]:


df.County.value_counts()


# In[4]:


df["Bias Motive Description"].value_counts()


# In[5]:


df['Offense Description'].value_counts()


# In[6]:


df[df.County == 'KINGS']["Bias Motive Description"].value_counts(ascending = True).plot(kind='barh',figsize = (30, 30),fontsize =30 )


# In[7]:


df[df["Offense Description"] == "MURDER & NON-NEGL. MANSLAUGHTE"]['Bias Motive Description'].value_counts()


# In[8]:


df[df['Bias Motive Description'] == 'ANTI-ASIAN']['Law Code Category Description'].value_counts()


# In[9]:


df[df['Bias Motive Description'] == 'ANTI-JEWISH']["Offense Description"].value_counts()


# In[59]:


df[df['Bias Motive Description'] == 'ANTI-ASIAN']["Offense Description"].value_counts()


# In[11]:


df[df['Bias Motive Description'] == 'ANTI-ASIAN']["Offense Description"].value_counts().plot(kind='barh',figsize = (30, 30),fontsize =30 )


# Anti-gay and Anti-asian hate crime types are similar.

# In[58]:


df[df['Bias Motive Description'] == 'ANTI-MALE HOMOSEXUAL (GAY)']["Offense Description"].value_counts()


# In[12]:


df[df['Bias Motive Description'] == 'ANTI-MALE HOMOSEXUAL (GAY)']["Offense Description"].value_counts().plot(kind='barh',figsize = (30, 30),fontsize =30 )


# In[61]:


df[df['Bias Motive Description'] == 'ANTI-MALE HOMOSEXUAL (GAY)']['Law Code Category Description'].value_counts()


# In[56]:


df[df['Bias Motive Description'] == 'ANTI-BLACK']["Offense Description"].value_counts()


# In[62]:


df[df['Bias Motive Description'] == 'ANTI-BLACK']['Law Code Category Description'].value_counts()


# In[63]:


df[df['Bias Motive Description'] == 'ANTI-JEWISH']['Law Code Category Description'].value_counts()


# In[33]:


df[df.County == 'BRONX']["Bias Motive Description"].value_counts()


# In[34]:


df[df.County == 'NEW YORK']["Bias Motive Description"].value_counts()


# In[35]:


df[df.County == 'QUEENS']["Bias Motive Description"].value_counts()


# In[36]:


df[df.County == 'RICHMOND']["Bias Motive Description"].value_counts()


# In[65]:


df[df["Offense Description"] == 'GRAND LARCENY']["Bias Motive Description"].value_counts()


# In[67]:


df[df["Offense Description"] == 'ROBBERY']["Bias Motive Description"].value_counts()


# In[68]:


df[df["Offense Description"] == 'FELONY ASSAULT']["Bias Motive Description"].value_counts()


# In[ ]:




