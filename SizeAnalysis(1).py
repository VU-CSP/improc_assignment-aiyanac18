#!/usr/bin/env python
# coding: utf-8

# # Analysis of the particle sizes from segmentation output
# You should have an output file named `Results.csv` from FIJI/ImageJ segmentation. If you are using Google Colab to run this code, you will need to upload the file manually to Google using the `File` menu to the left.  

# In[7]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


get_ipython().system('pip install pandas')


# Write code below to read the `Results.csv` file as a pandas DataFrame and store it in the object named `measurements`. Show the head of the DataFrame.

# In[4]:


get_ipython().system('pip install numpy')


# In[6]:


get_ipython().system('pip install seaborn')


# In[18]:


# Code to read Results and show head
measurements = pd.read_csv('Results.csv')
measurements.head()


# In[22]:


# Code to plot a histogram of the Area
sns.histplot(measurements, x="Area")


# Calculate the mean and the standard deviation of the distribution and show them below. (HINT: pandas can do this easily)

# In[27]:


# Calculate mean
measurements['Area'].mean()


# In[29]:


# Calculate standard deviation
measurements['Area'].std()


# #### Describe your interpretation of the distribution of the measurements of nuclear area below. 
# Based on what you see, would you choose different value ranges of particle sizes for counting? Explain why.
# 

# The current mean has a very high standard deviation (65.5), which should not really be the case for nuclei areas. The range of particle sizes should be set to lower to segment nuclei close together seperately. 

# In[ ]:




