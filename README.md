# Text Summarizer Web App

This is a simple web application built with Python and Flask that utilizes natural language processing (NLP) techniques to summarize text. It allows users to input a text, specify the number of lines for the summary, and generates a concise summary of the text.

## Features

- Accepts user input in the form of a text or paragraph.
- Provides the option to specify the number of lines for the summary.
- Utilizes the spaCy library for NLP processing.
- Removes stop words and calculates word frequencies.
- Assigns scores to sentences based on word frequencies.
- Generates a summary by selecting the top-scoring sentences.
- User-friendly web interface with a clean and responsive design.

## Prerequisites

- Python 3.x
- Flask
- spaCy
- en_core_web_sm (spaCy model)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/parthkhajgiwale/Text-Summarizer
   ```

2. Navigate to the project directory:

   ```shell
   cd Text-Summarizer
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required packages:

   ```shell
   pip install -r requirements.txt
   ```

5. Download the spaCy model:

   ```shell
   python -m spacy download en_core_web_sm
   ```

## Usage

1. Run the Flask application:

   ```shell
   python main.py
   ```

2. Open your web browser and go to `http://localhost:5000`.

3. Enter the text you want to summarize in the provided textarea.

4. Specify the number of lines for the summary.

5. Click the "Summarize" button.

6. The summary will be displayed on the result page.



Feel free to modify the content and instructions in the `README.md` file according to your project's needs.
