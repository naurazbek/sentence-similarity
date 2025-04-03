# Sentence Similarity Project

This project demonstrates the use of pre-trained Sentence Transformers to compute sentence embeddings and evaluate the similarity of question pairs using the Quora Question Pairs dataset. The goal is to predict whether two questions are duplicates based on their semantic similarity.

## Features
- Uses the `sentence-transformers` library with a pre-trained model (`all-MiniLM-L6-v2`).
- Computes cosine similarity between sentence embeddings.
- Evaluates the accuracy of predictions using a threshold for similarity.

## Dataset
The project uses the [Quora Question Pairs](https://www.kaggle.com/competitions/quora-question-pairs) dataset, which contains pairs of questions and a label (`is_duplicate`) indicating whether the questions are duplicates.

### Example Dataset Format
The dataset should be in CSV format with the following columns:
- `question1`: The first question in the pair.
- `question2`: The second question in the pair.
- `is_duplicate`: A binary label (1 for duplicate, 0 for not duplicate).

## Setup Instructions

### Prerequisites
- Python 3.9 or later (tested with Python 3.9, 3.10, and 3.11).
- GitHub account (`naurazbek`).
- PyCharm IDE (optional, for development).

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/naurazbek/sentence-similarity.git
   cd sentence-similarity
Install the required Python packages:

bash


pip install -r requirements.txt
Download the Quora Question Pairs dataset from Kaggle and place it in the project directory. Rename the file to quora_question_pairs.csv.

Run the script:

bash


python main.py
Docker Setup
Build the Docker image:

bash


docker build -t sentence-transformers-app .
Run the Docker container:

bash


docker run -it --rm sentence-transformers-app
