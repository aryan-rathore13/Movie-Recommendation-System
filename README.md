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

Step 2: Install Dependencies
Install all required dependencies listed in the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Step 3: Preprocess Data and Generate Files
Use the provided notebook to preprocess the dataset and generate required files:

Open the Generate_Cosine_Similarity.ipynb notebook.
Run the notebook to:
Load and preprocess the dataset.
Generate the tfidf_vectorizer.pkl and cosine_similarity_matrix.pkl files.
The generated files will be saved locally in the project directory.

Step 4: Upload Files to S3
Ensure your AWS credentials are configured.
Upload the preprocessed files to your S3 bucket:
bash
Copy code
aws s3 cp tfidf_vectorizer.pkl s3://<your-bucket-name>/model/tfidf_vectorizer.pkl
aws s3 cp cosine_similarity_matrix.pkl s3://<your-bucket-name>/model/cosine_similarity_matrix.pkl
Step 5: Run the Application
Update the following in application.py:

Replace <your-bucket-name> with your S3 bucket name.
Ensure correct file paths for tfidf_vectorizer.pkl and cosine_similarity_matrix.pkl.
Start the Flask application:

bash
Copy code
python application.py
Access the application using the public IP address of your server or http://0.0.0.0:80.

Deployment on EC2
Follow these additional steps for deploying the project on an AWS EC2 instance:

Launch an EC2 instance with a publicly accessible IP.
Configure the security group to allow HTTP (port 80) and HTTPS (port 443) traffic.
Transfer the repository files to the instance using SCP or git clone.
Follow the above setup steps on the EC2 instance to run the application.
Feel free to fork, contribute, or raise issues to improve this project.
