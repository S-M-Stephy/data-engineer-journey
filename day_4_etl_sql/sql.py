movies = '''
movie_id,title,genre,year
1,The Matrix,Sci-Fi,1999
2,The Godfather,Crime,1972
3,Toy Story,Animation,1995
4,Inception,Sci-Fi,2010
5,The Dark Knight,Action,2008
6,Forrest Gump,Drama,1994
7,Finding Nemo,Animation,2003
'''

ratings = '''
movie_id,user_id,rating
1,101,5
1,102,4
1,103,5
2,101,5
2,104,5
3,101,4
3,105,3
3,106,5
4,102,5
4,103,4
5,101,4
5,106,5
5,107,5
6,101,5
6,108,3
7,103,4
7,104,5
'''
with open('movies.csv', 'w') as file:
    file.write(movies)
with open('ratings.csv', 'w') as file:
    file.write(ratings)

import pandas as pd
import sqlite3

# Load data from CSV files into pandas DataFrames
movie_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')

# Display the first few rows of each DataFrame
print(movie_df.head())
print(ratings_df.head())

# Create a SQLite database and save the DataFrames to it
conn = sqlite3.connect("movie.db")
movie_df.to_sql('movies',conn,if_exists='replace')
ratings_df.to_sql('ratings',conn,if_exists='replace')

# Top 5 movies by average rating
query = 'SELECT title, avg(rating) FROM movies JOIN ratings ON movies.movie_id = ratings.movie_id GROUP BY title order by avg(rating) desc limit 5'
output_df = pd.read_sql_query(query,conn)
print(output_df)

conn.close()