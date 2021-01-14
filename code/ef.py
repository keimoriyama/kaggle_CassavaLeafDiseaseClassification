#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In[2]:


import timm


# In[7]:


timm.list_models("tf_efficient*")


# In[8]:


ef_model = timm.create_model("tf_efficientnet_b8", pretrained = True)


# In[10]:


import torch


# In[11]:


torch.save(ef_model.state_dict(), "/")


# In[ ]:




