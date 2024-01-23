# This project involves the analysis of the Netflix dataset to gain insights into user preferences, content trends, and other relevant aspects.
#Pandas: Used for data manipulation, cleaning, and exploratory data analysis.
#NumPy: Employed for numerical operations on arrays and matrices.
#Matplotlib:Utilized for creating static visualizations, such as line charts and histograms.
#Seaborn: Applied for statistical data visualization, enhancing the aesthetics of the visualizations.

# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv(r"C:\Users\sunid\Downloads\8. Netflix Dataset.csv")


# In[39]:


data


# In[5]:


data.head()               #it is use to show top 5 recoreds of dataset


# In[7]:


data.tail()                                                           #it will show the bottom 5 records


# In[9]:


data.shape                                      # it will show the total number of rows and coloums


# In[10]:


data.size                        # it will show the total number of value(element) in the dataset


# In[12]:


data.columns                    # it will show the each columns names


# In[13]:


data.dtypes                      # it will show the data-types of each columns


# In[14]:


data.info()                         #to show the index, columns, data-types of each column, memory at once    


# Is there any Duplicate Record in this dataset? if yes, then remove the duplicate records.

# In[15]:


data.head()


# In[16]:


data.shape


# In[18]:


data[data.duplicated()]                 #to check the duplicate in the records


# In[20]:


data.drop_duplicates(inplace= True)                  #to remove the duplicates from the dataset


# In[21]:


data[data.duplicated()]                          # to check the duplicates are remove or not


# In[22]:


data.shape


# In[ ]:





#  IS THERE IS ANY NULL VALUE PRESENT IN ANY COLUMN? SHOW THE HEAT-MAP.
# 

# In[24]:


data.isnull()                                 #to check the null value in the data set


# In[25]:


data.isnull().sum()                 # to show the null value in the each columns


# In[40]:


import seaborn as sns                               #to import the seaborn library


# In[27]:


sns.heatmap(data.isnull())                        # using the heat-map to show the null values


#  Questions
# 
# 

# FOR "House Of Cards". WHAT IS THE SHOW ID AND WHO IS THE DIRECTOR OF THIS SHOW?

# In[30]:


data.head()


# In[34]:


data[data["Title"].isin(['House of Cards'])]             # to show the particular item in any columns


# In[8]:


data[data['Title'].str.contains('House of Cards')]               #to show the particular items in any columns with the help of str.contains 


# #IN WHICH YEAR HIGHEST NUMBER OF THE TV SHOWS AND MOVIES WERE RELEASED? SHOW WITH THE BAR GRAPH. 

# In[9]:


data.dtypes


# In[19]:


data['Data_N'] = pd.to_datetime(data['Release_Date'])


# In[6]:


data.head()


# In[7]:


data.dtypes


# In[79]:


del data['Data_N']

data['Data_N'] = pd.to_datetime(data['Release_Date'])
# In[61]:


data.dtypes


# In[62]:


data.head()


# In[63]:


data['Data_N'].dt.year.value_counts()


# In[13]:


data['Data_N'].dt.year.value_counts().plot(kind='bar')            #to creat a bar graph 


# How many movies and TV shows are in the dataset?Show with bar graph.

# In[15]:


data.head(2)


# In[17]:


data.groupby('Category').Category.count()


# In[49]:


sns.countplot(data['Category'])


# Show the movies that were released in year 2000.

# In[50]:


data.head()


# In[20]:


data['Year']= data['Data_N'].dt.year


# In[23]:


data.head()


# In[65]:


data[ (data['Category'] == 'Movie') & (data['Year']) ]


# Show only the Titles of all TV shows that were released in India only.

# In[26]:


data.head(2)


# In[70]:


data[(data['Category'] == 'TV Show') & (data['Country'] =='India')]  ['Title']


# In[ ]:





# Show Top 10 Diectors, who ave the highest number of TV shows & Movies to netflix?

# In[72]:


data['Director'].value_counts().head(10)


# In[ ]:





# Show all the records , where "Category is Movies and type is comedies" or " Country is united kingdom".

# In[73]:


data.head()


# In[77]:


data[(data['Category']=='Movie') & (data['Type']=='Comedies')]


# In[78]:


data[(data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country'] == 'United Kingdom')] 


# In how many movie/shows dose Tom Cruise was cast?

# In[80]:


data.head()


# In[84]:


data[(data['Cast'] == 'Tom Cruise')]


# In[1]:


data[data['Cast'].str.contains('Tom Cruise')]


# In[87]:


#as this data contain null value as shown in above syntax. there for we have to remove the null values.
#so we have to creat the new data frame


# In[88]:


data_new = data.dropna()                                     # it drops the rows that contains all or any missing values.


# In[89]:


data.head()


# In[92]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# What is the different ratings defined by Netflix

# In[94]:


data.head(2)


# In[95]:


data['Rating'].nunique()


# In[97]:


data.Rating.unique()


# How many movies got the 'TV-14' rating, in canada?

# In[99]:


data.head(2)


# In[102]:


data[(data['Category'] =='Movie')  & (data['Rating'] =='TV-14') ].shape


# In[107]:


data[(data['Category'] =='Movie')  & (data['Rating'] =='TV-14') & (data['Country'] == 'Canada') ].shape


# How many TV Shows got the 'R' rating, after year 2018?

# In[106]:


data.head(2)


# In[109]:


data[(data['Category'] =='TV Show') & (data['Rating'] == 'R')]


# In[110]:


data[(data['Category'] =='TV Show') & (data['Rating'] == 'R') & (data['Year'] >2018)]


# What is the maximum duration of a movie/show on netflix?

# In[111]:


data.head(2)


# In[112]:


data.Duration.unique()


# In[117]:


data.Duration.dtypes


# In[118]:


data.head(2)


# In[120]:


data[['Minutes' , 'Unit']] = data['Duration'].str.split(' ', expand = True)


# In[121]:


data.head()


# In[123]:


data['Minutes'].max()


# In[124]:


data.dtypes


# In[ ]:





# Which individual country has the Highest No. of TV Shows ?

# In[3]:


data.head(2)


# In[7]:


data_tvshow = data[data['Category'] == 'TV Show']


# In[8]:


data_tvshow.head(2)


# In[9]:


data_tvshow.Country.value_counts()


# In[13]:


data_tvshow.Country.value_counts().head(1)


# How can we sort the dataset by Year ?

# In[14]:


data.head(2)


# In[21]:


data.sort_values(by = 'Year')


# In[24]:


data.sort_values(by = 'Year' , ascending = False).head(5)


# Find all the instances where:
#   category is 'Movie' and Type is 'Dramas'
#                     or
#   category is 'TV show' & Type is 'kids' TV ?

# In[25]:


data.head(2)


# In[39]:


data[(data['Category'] =='Movie') & (data['Type']=='Dramas')].head(2)


# In[38]:


data[(data['Category'] == 'TV Show') & (data['Type'] == "Kids' TV")]


# In[41]:


data[(data['Category'] =='Movie') & (data['Type']=='Dramas') | (data['Category'] == 'TV Show') & (data['Type'] == "Kids' TV")]


# In[ ]:




