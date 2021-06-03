#!/usr/bin/env python
# coding: utf-8

# In[44]:


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[27]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[30]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[46]:


html = browser.html
newsoup = BeautifulSoup(html,'html.parser')


# In[52]:


title = newsoup.find_all('div', class_='content_title')[0].text
paragraph = newsoup.find_all('div', class_='article_teaser_body')[0].text
print(title)
print(paragraph)


# In[54]:


imagehtml = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(imagehtml)


# In[71]:


imagehtml = browser.html
imgagesoup = BeautifulSoup(html,'html.parser')


# In[72]:


imageurl = imgagesoup.find('img', class_='fancybox-image').get('src')
imageurl


# In[74]:


fact_url = 'https://space-facts.com/mars/'
datatable = pd.read_html(fact_url)
print(datatable)


# In[82]:


datatable_html = datatable.to_html()
print(datatable_html)


# In[84]:


mission_dictionary={
    "title":title,
    "paragraph": paragraph,
    "datatable": datatable
}
mission_dictionary





