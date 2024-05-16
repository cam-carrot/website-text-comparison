from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer
import requests
import nltk

# Make sure stopwords are downloaded
nltk.download('stopwords')

# Function to get cleaned text from a webpage
def get_cleaned_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract text from the webpage
    text = soup.get_text()
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    cleaned_text = " ".join([word for word in words if word not in stop_words])
    
    return cleaned_text

# Semantic comparison function
def semantic_comparison(url1, url2):
    # Get the cleaned text
    text1 = get_cleaned_text(url1)
    text2 = get_cleaned_text(url2)

    # Use BERT model for semantic similarity
    model = SentenceTransformer('all-MiniLM-L6-v2')  # or any other model
    embeddings1 = model.encode([text1], convert_to_tensor=True)
    embeddings2 = model.encode([text2], convert_to_tensor=True)

    # Semantic similarity
    semantic_similarity = cosine_similarity(embeddings1, embeddings2)
    
    return semantic_similarity[0][0]

# N-gram comparison function
def ngram_comparison(url1, url2):
    # Get the cleaned text
    text1 = get_cleaned_text(url1)
    text2 = get_cleaned_text(url2)

    # TF-IDF Vectorizer with n-gram
    vectorizer = TfidfVectorizer(ngram_range=(1,2))  # Unigrams and bigrams

    # Transform the text into TF-IDF vectors
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

    # N-gram similarity
    ngram_similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    return ngram_similarity[0][0]

# Overall comparison function
def compare(url1, url2):
    semantic_similarity = semantic_comparison(url1, url2)
    ngram_similarity = ngram_comparison(url1, url2)

    return semantic_similarity, ngram_similarity
