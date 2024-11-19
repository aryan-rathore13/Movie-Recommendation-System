# Movie-Recommendation-System
A content-based movie recommendation system that suggests movies based on textual similarities of features like titles, overviews, and genres. This project leverages data from a movie dataset stored on AWS S3, processes it using Python, and employs machine learning techniques to compute recommendations.
This repository contains a Flask-based web application that provides movie recommendations using a precomputed cosine similarity matrix and TF-IDF features.

## Dataset Credit  
The dataset used in this project is sourced from Kaggle: [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset).  
All rights and acknowledgments go to the original dataset creators.

---

## Project Setup Instructions  

### Prerequisites  
- Python 3.8 or above  
- AWS account with S3 bucket set up  
- Dependencies listed in `requirements.txt`  

### Step 1: Clone the Repository  
```bash  
git clone https://github.com/your-username/movie-recommendation-system.git  
cd movie-recommendation-system  
