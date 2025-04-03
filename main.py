import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the Quora Question Pairs dataset (download from Kaggle)
# Ensure the dataset is in the same directory as this script
data_path = "data/questions.csv"
df = pd.read_csv(data_path)

# Preprocess the dataset (take a small subset for demonstration)
df = df[['question1', 'question2', 'is_duplicate']].dropna().head(100)

# Compute embeddings for question pairs
embeddings1 = model.encode(df['question1'].tolist(), convert_to_tensor=True)
embeddings2 = model.encode(df['question2'].tolist(), convert_to_tensor=True)

# Compute cosine similarity
cosine_scores = util.cos_sim(embeddings1, embeddings2)

# Evaluate the similarity
threshold = 0.7  # Define a threshold for similarity
predictions = [1 if score >= threshold else 0 for score in cosine_scores.diagonal()]

# Calculate accuracy
accuracy = sum([pred == actual for pred, actual in zip(predictions, df['is_duplicate'].tolist())]) / len(predictions)
print(f"Accuracy: {accuracy:.2f}")
