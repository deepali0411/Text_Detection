#!/usr/bin/env python
# coding: utf-8

# # THE SPARKS FOUNDATION
# # GRIPFEB21¶
# # NAME: DEEPALI RAJE RATHORE
# # DOMAIN : IOT AND COMPUTER VISION
# # TASK1 : TEXT DETECTION

# In[1]:


import matplotlib.pyplot as plt
import cv2
import pytesseract


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


img = cv2.imread('img.jpeg')


# In[4]:


plt.imshow(img)


# In[5]:


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# In[6]:


img = cv2.imread('img.jpeg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# In[7]:


print(pytesseract.image_to_string(img))


# In[8]:


#  ###detection characters
# hImg,wImg,_ = img.shape
# boxes = pytesseract.image_to_boxes(img)


# In[9]:


# for b in boxes.splitlines():
#     b = b.split(' ')
#     print(b)
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,225),2)
#     cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
# cv2.imshow('Result',img)
# cv2.waitKey(0)


# In[10]:


###detecting words
hImg,wImg,_ = img.shape


# In[11]:


boxes = pytesseract.image_to_data(img)


# In[12]:


for x, b in enumerate(boxes.splitlines()):
    if x!=0:
        b= b.split()
        print(b)
        if len(b)==12:
           x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9]) 
           cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,225),2) 
           cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(50,50,225),1)


# In[13]:


cv2.imshow('Result',img)
cv2.waitKey(0)


# In[ ]:




