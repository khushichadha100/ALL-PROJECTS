import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


movie= pd.read_csv('D:\\RESUME_INTERNSHIPS_CERTIFICATES\\CODSOFT INTERNSHIP\\Movie.csv')
mg= pd.read_csv('D:\\RESUME_INTERNSHIPS_CERTIFICATES\\CODSOFT INTERNSHIP\\Movie Genres.csv')
genres= pd.read_csv('D:\\RESUME_INTERNSHIPS_CERTIFICATES\\CODSOFT INTERNSHIP\\Genres.csv')
movie_columns =['mov_id','mov_title','mov_year','mov_lang']
columns_to_drop = [col for col in movie.columns if col not in  movie_columns]
movie.drop(columns=columns_to_drop, inplace=True)
print(movie.head(10))

print(mg.head())
print(genres.head())

df=genres.merge(mg , on="gen_id")
print(df.head())
 
movie=movie.merge(df , on="mov_id")
print(movie.head())


 
movie_columns =['mov_id','mov_title','mov_year','mov_lang','gen_title']
columns_to_drop = [col for col in movie.columns if col not in  movie_columns]
movie.drop(columns=columns_to_drop, inplace=True)
print(movie.head())


ratings=pd.read_csv('D:\\RESUME_INTERNSHIPS_CERTIFICATES\\CODSOFT INTERNSHIP\\Rating.csv')
print(ratings.head())


movie=movie.merge(ratings, on="mov_id")
print(movie.head())


del movie["rev_id"]
print(movie.head(10))


rstars_avg=movie["rev_stars"].mean()
print(rstars_avg)

movie['rev_stars'] = movie['rev_stars'].fillna(rstars_avg)
print(movie.head(10))


norat_avg=movie["num_o_ratings"].mean()
print(norat_avg)


movie["num_o_ratings"]=movie["num_o_ratings"].fillna(norat_avg)
print(movie.head(10))


C = movie['rev_stars'].mean()
m = movie['num_o_ratings'].quantile(0.75)
def points(x, m=m, C=C):
    v = x['num_o_ratings']
    R = x['rev_stars']
    return (v / (v + m)) * R + (m / (v + m)) * C
movie['score'] = movie.apply(points, axis=1)
movie = movie.sort_values('score', ascending=False)
print(movie.head(10))


movie= movie.sort_values('score', ascending=False)
plt.figure(figsize=(5,2)) 
plt.barh(movie['mov_title'].head(8),movie['score'].head(8), align='center',color='darkblue')
plt.gca().invert_yaxis()
plt.xlabel("Popularity")
plt.ylabel("Popular Movies")
plt.title("trending movies")
plt.show()

 
tfidf = TfidfVectorizer(stop_words='english')
movie['gen_title'] = movie['gen_title'].fillna('')
tfidf_matrix = tfidf.fit_transform(movie['gen_title'])
print(tfidf_matrix.shape)

for i in tfidf_matrix:
    print(i)


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
print(cosine_sim)


indices = pd.Series(movie.index, index=movie['gen_title']).drop_duplicates()
print(indices)


def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = movie[movie['mov_title'] == title].index[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 5 most similar movies
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return movie['mov_title'].iloc[movie_indices]

 


recommendations = get_recommendations('Trainspotting')
print("Recommendations in relation to 'Trainspotting':")
print(recommendations)


recommendations = get_recommendations('The Innocents')
print("Recommendations in relation to 'Trainspotting':")
print(recommendations)


 




