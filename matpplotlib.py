#!/usr/bin/env python
# coding: utf-8

# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')


# In[18]:


fig = plt.figure()
plt.plot([1,2,3,4], label='blue_line')
plt.ylabel('some numbers')
plt.legend(loc='best')
plt.title('title');
plt.savefig('blue_line.png')


# In[16]:


x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)
kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins=40)
plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)
plt.savefig('hist.png')


# In[17]:


data = [500, 200, 250]
labels = ["Agriculture", "Aide", "News"]
plt.pie(data, labels=labels,autopct='%1.1f%%') 
plt.show()


# In[19]:


from IPython.display import Image
Image('blue_line.png')


# In[20]:


x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x - 0), color='blue') # specify color by name
plt.plot(x, np.sin(x - 1), color='g') # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75') # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44') # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 and 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported


# In[22]:


plt.plot(x, x + 0, linestyle='solid')


# In[23]:


plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');
# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle='-') # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':'); # dotted


# In[26]:


x = np.linspace(0, 10, 1000)
plt.figure() # create a plot figure
# create the first of two panels and set current axis
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))
# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x));


# In[ ]:




