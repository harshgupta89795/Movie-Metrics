import numpy as np
import pandas as pd

import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('IMDB-Movie-Data.csv')
# sns.heatmap(data.isnull())
plt.show()
print(data.columns)
# Movies from the "Drama" Genre Released Before 2000 with a Rating Above 7
top_year_genre = data[data['Year'] > 2000]
top_year_genre1 = top_year_genre[top_year_genre['Genre'].str.contains("Drama")]
top_year_genre2 = top_year_genre1[top_year_genre['Rating'] > 7]
print(top_year_genre2)

# MOVIES DIRECTED BY CHRISTOPHER NOLAN AND RATING GREATER THAN 8
nolan = data[data['Director'] == 'Christopher Nolan']
nolan1 = nolan[nolan['Rating'] > 8]
print(nolan1)

# TOP 5 MOVIES(HIGHEST REVENUE) IN THE GENRE COMEDY
high_genre = data[(data['Genre'] == 'Comedy')]
high_henre1 = high_genre.sort_values(by='Revenue (Millions)', ascending=False).head(5)
print(high_henre1)

# DIRECTORS WITH MOST NUMBER OF FILMS THEY DIRECTED
top_directors = data['Director'].value_counts().head(10)
print(top_directors)

# SCATTER GRAPH THAT SHOWS THE REVENUE EARNED BY MOVIES CORRESPONDING TO THE RATING'S
sns.scatterplot(x='Rating', y='Revenue (Millions)', data=data)
plt.title('Rating vs Revenue')
plt.show()

# BAR GRAPH THAT SHOWS THE REVENUE EARNED BY MOVIES CORRESPONDING TO THEIR GENRE
sns.barplot(x='Genre', y='Revenue (Millions)', data=data)
plt.title('Revenue by Genre')
plt.show()

# MOVIES WITH RATING GREATER THAN 8
high_rated_movies = data[data['Rating'] > 8]
print(high_rated_movies[['Title', 'Rating']])

# MOVIES WHICH WERE RELEASED AFTER 2010 AND EARNED MORE THAN 100 MILLION
successful_movies = data[(data['Year'] > 2010) & (data['Revenue (Millions)'] > 100)]
print(successful_movies[['Title', 'Year', 'Revenue (Millions)']])

# TOP 5 RATED MOVIES
top_rated = data.sort_values('Rating', ascending=False).head(5)
print(top_rated)

# TOP 10 RATED MOVIE IN THE COMEDY GENRE
top_genre = data[data['Genre'].str.contains('Comedy')]
top_ = top_genre.sort_values(by="Rating", ascending=False)
print(top_.head(10))

# TOP 10 DIRECTORS
top_director = data.sort_values('Rating', ascending=False).head(10)
print(top_director[['Title', 'Rating', 'Director']])

# Display the Top 15 Movie in the Dataset
print(data.head(15))

# Display the Last 15Movie in the Dataset
print(data.tail(15))

# Shape of the Dataset
print("Shape {}".format(data.shape))

# Information
print(data.info())
print(data.isnull())

if (data.duplicated().any()):
    print("Are there any duplicated data present in the Datase? {}".format(data.duplicated().any()))
else:
    print("Are there any duplicated data present in the Dataset? {}".format(data.duplicated().any()))

print(data.describe())

# MOVIES WITH RUNTIME GREATER THAN 180 MINUTES
print(data[data['Runtime (Minutes)'] >= 180]['Title'])

# MOVIES WHICH COLLECTED MORE THAN 900 MILLIONS AS REVENUE
print(data[data['Revenue (Millions)'] >= 900]['Title'])

# BAR PLOT THAT SHOW THE NUMBER OF VOTES CASTED EACH YEAR
sns.barplot(x='Year', y='Votes', data=data)
plt.title("Votes by Year")
plt.show()

# PLOT THAT SHOW THE REVENUE COLLECTED IN EACH YEAR
sns.barplot(x='Year', y='Revenue (Millions)', data=data)
plt.title("Revenue by Year")
plt.show()

# AVGERAGE RATING OF THE DIRECTORS
print(data.groupby('Director')['Rating'].mean().sort_values(ascending=False))

# TOP 5 MOVIES WITH THE LARGEST RUNTIME
le = data.nlargest(10, 'Runtime (Minutes)')[['Title', 'Runtime (Minutes)']]. \
    set_index('Title')
sns.barplot(x='Runtime (Minutes)', y=le.index, data=le)
plt.title('Top 5 Lengtly Movies')
plt.show()

# PLOT THAT SHOWS HOW MANY NUMBER OF MOVIES ARE BEING DIRECTED IN A YEAR
sns.countplot(x='Year', data=data)
plt.title("Number of movies per year")
plt.show()

# TOP 10 MOVIES WHO EARNED THE MAXIMUM REVENUE
top_rev = data.sort_values('Revenue (Millions)', ascending=False).head(10)
print(top_rev)





