#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup


# In[3]:


import requests


# In[4]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'


# In[7]:


pagge = requests.get(url)


# In[8]:


soup = BeautifulSoup(page.text, 'html')


# In[9]:


print(soup)


# In[21]:


table = soup.find_all('table')[1]


# In[22]:


world_title = table.find_all('th')


# In[23]:


print(world_title)


# In[24]:


list_world_titles = [title.text.strip() for title in world_title]


# In[25]:


print(list_world_titles)


# In[27]:


import pandas as pd


# In[29]:


df = pd.DataFrame(columns = list_world_titles)
df


# In[30]:


table.find_all('tr')


# In[31]:


column_data = table.find_all('tr')


# In[36]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    data_ind = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = data_ind


# In[37]:


df


# In[38]:


df.to_csv(r'C:\Users\Mario Alberto\Documents\Proyecto\Portafolio_Project\CompaniasGrandes.csv', index = False)


# In[ ]:




