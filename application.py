from flask import Flask, request, render_template
import joblib
import pandas as pd
import boto3
import os

application = Flask(__name__)

# S3 bucket and file keys for resources
bucket_name = 'movie-recommender-dataset'
vectorizer_key = 'model/tfidf_vectorizer.pkl'
cosine_sim_key = 'model/cosine_similarity_matrix.pkl'
file_key = 'data/movies_metadata.csv'

# Function to download a file from S3
def download_from_s3(bucket, key, local_path):
    s3 = boto3.client('s3')
    s3.download_file(bucket, key, local_path)

# Download and load the TF-IDF vectorizer and cosine similarity matrix
if not os.path.exists('tfidf_vectorizer.pkl'):
    download_from_s3(bucket_name, vectorizer_key, 'tfidf_vectorizer.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

if not os.path.exists('cosine_similarity_matrix.pkl'):
    download_from_s3(bucket_name, cosine_sim_key, 'cosine_similarity_matrix.pkl')
cosine_sim = joblib.load('cosine_similarity_matrix.pkl')

# Function to load movies metadata from S3
def load_movies_metadata_from_s3(bucket_name, file_key):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    return pd.read_csv(obj['Body'], low_memory=False)

# Load the sample DataFrame from S3 (global for app use)
sample_df = load_movies_metadata_from_s3(bucket_name, file_key)

# Define the function to get movie recommendations
def recommend_movies(title, sample_df, cosine_sim=cosine_sim):
    if title not in sample_df['title'].values:
        return [f"Movie titled '{title}' not found in the dataset."]
    
    idx = sample_df[sample_df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return sample_df.iloc[movie_indices]['title'].tolist()

@application.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        title = request.form.get('title')
        recommendations = recommend_movies(title, sample_df)
    return render_template('index.html', recommendations=recommendations)

if __name__ == "__main__":
    application.run(debug=True)
