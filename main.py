from flask import Flask, request, send_file, render_template
import csv
import pandas as pd
import comparison

application = Flask(__name__)

@application.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@application.route('/compare', methods=['POST'])
def compare():
    url1 = request.form['url1']
    url2 = request.form['url2']
    semantic_similarity, ngram_similarity = comparison.compare(url1, url2)
    return f'Semantic similarity: {semantic_similarity}, N-gram similarity: {ngram_similarity}'

@application.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['csvfile']

        # Load csv file into pandas dataframe
        data = pd.read_csv(f)

        # Initialize result list
        result = []

        # Iterate over each row of dataframe
        for index, row in data.iterrows():
            url1 = row[0]
            url2 = row[1]
            semantic_similarity, ngram_similarity = comparison.compare(url1, url2)
            result.append([url1, url2, semantic_similarity, ngram_similarity])

        # Convert result into pandas dataframe and save it to csv file
        result_df = pd.DataFrame(result, columns=['URL1', 'URL2', 'Semantic Similarity', 'N-gram Similarity'])
        result_file = 'result.csv'
        result_df.to_csv(result_file, index=False)

        # Send the result csv file
        return send_file(result_file, as_attachment=True)

if __name__ == '__main__':
    application.run(debug=True)
