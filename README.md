# website-text-comparison
This script is used to measure the semantic and n-gram similiarity of two URLs or a list of URLs.

# Requirements
- flask==2.3.2
- pandas==2.0.0
- beautifulsoup4==4.12.2
- requests==2.28.2
- nltk==3.8.1
- scikit-learn==1.2.2
- sentence-transformers==2.2.2

# Installation
1. Clone the repo
2. Install dependencies

   ` pip install flask` and so on

3. Run the main.py script

    ` python main.py`

# How This Works
When you run the main.py code, you will launch a local app accessible in your browser. Your console will provide you with the address (ie, http://127.0.0.1:5000)

On the html that loads, you can either input two URLs to compare in the fields or upload a list of URLS.  Your upload should be a CSV file with two columns: the first column with a header = "url1" and the second column with a header = "url2".  The script will compare the two paired URLS on each row and provide scores.

If you input two URLS in the browser fields and click submit, the job will process and the scores will appear on the following screen.

If you upload a CSV and click submit, the job will process and you will receive a results.csv file.

# About The Results
This script provides two different similarity scores: semantic similarity and n-gram similarity. Each is on a scale from 0 to 1.  These scores provide meaningful insights about how similar two webpages are along two differnt lines.

## n-gram Similarity
N-gram similarity scores measure the similarity between two texts based on the number of shared sequences of n consecutive characters or words. An n-gram is simply a contiguous sequence of n items from a given sample of text. For example, in the text "hello world" with n=2, the word-level n-grams are ["hello", "world"], and the character-level n-grams are ["he", "el", "ll", "lo", "o ", " w", "wo", "or", "rl", "ld"]. N-gram similarity is calculated by comparing these sequences between two texts, providing a straightforward way to assess how much the two texts have in common. This method is particularly useful in tasks like text matching, plagiarism detection, and information retrieval.

## Semantic Similarity
Semantic similarity scores, on the other hand, go beyond the surface level of the text and assess the meaning conveyed by the words. These scores are calculated using techniques from natural language processing (NLP) and machine learning, such as word embeddings, which capture the contextual meaning of words in a high-dimensional space. By comparing the vector representations of the texts, semantic similarity scores can identify how similar the meanings of two texts are, regardless of their exact wording. This method is powerful for understanding the relationship between texts in applications like search engines, recommendation systems, and content analysis.

# Future Development Ideas
- Host somewhere other than local server
- Improve UX
- Improve similarity models to provide deeper and more nuanced insights
