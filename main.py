import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from flask import Flask, render_template, request

app = Flask(__name__)

def text_summarizer(text, num_lines):
    # Load the pre-trained English NLP model
    nlp = spacy.load("en_core_web_sm")

    # Create a spaCy document
    doc = nlp(text)

    # Remove stop words and punctuation
    stopwords = list(STOP_WORDS)
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in word_frequencies.keys():
                word_frequencies[word.text.lower()] = 1
            else:
                word_frequencies[word.text.lower()] += 1

    # Calculate the weighted frequency of each word
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency

    # Calculate the sentence scores based on word frequencies
    sentence_scores = {}
    for sentence in doc.sents:
        for word in sentence:
            if word.text.lower() in word_frequencies.keys():
                if sentence not in sentence_scores.keys():
                    sentence_scores[sentence] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sentence] += word_frequencies[word.text.lower()]

    # Sort the sentences by score in descending order
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)

    # Select the top n sentences for the summary
    summary = []
    for sentence in sorted_sentences[:num_lines]:
        summary.append(sentence.text)

    return " ".join(summary)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_text = request.form['text']
        summary_lines = int(request.form['lines'])
        summary = text_summarizer(input_text, summary_lines)
        return render_template('result.html', summary=summary)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
