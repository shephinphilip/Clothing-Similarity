import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Data_clean import clean_text

# Load the preprocessed CSV file
df = pd.read_csv('cleaned_dataset.csv')

# Step 2: Measure Similarity

# Extract features using TF-IDF
vectorizer = TfidfVectorizer()
features = vectorizer.fit_transform(df['Description'])  # Assuming 'Description' is the column name with preprocessed text

# Step 3: Return Ranked Results

def get_similar_items(input_text, top_n=5):
    # Preprocess the input text
    cleaned_input = clean_text(input_text)  # Implement your own clean_text function

    # Extract features for the input text
    input_feature = vectorizer.transform([cleaned_input])

    # Compute similarity between the input text and all items in the dataset
    similarity_scores = cosine_similarity(input_feature, features)

    # Get the indices of top-N similar items
    top_indices = similarity_scores.argsort()[0][-top_n:][::-1]

    # Get the relevant columns for the output
    output_columns = [ 'ProductName', 'ProductBrand', 'Description', 'product_url_website1','product_url_website2','product_url_website3']

    print("Top-N similar items:")
    for idx, index in enumerate(top_indices, start=1):
        row = df.loc[index, output_columns]
        print("Serial Number:", idx)
        print("Product Name:", row['ProductName'])
        print("Product Brand:", row['ProductBrand'])
        print("Description:", row['Description'])
        print("Website :", row['product_url_website1'])
        print("Website :", row['product_url_website2'])
        print("Website :", row['product_url_website3'])
        print()

# Example usage
input_text = input("Enter a description: ")
top_n = 10
get_similar_items(input_text, top_n)
