import re
from contection_to_normale import contection_to_normale
from nltk.parse.corenlp import CoreNLPParser

def create_corpus_from_file(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
    # Optionally preprocess the text:
    # Convert text to lowercase
    text = text.lower()

    # Replace "al I'm" with "I am" and other similar words
    text = contection_to_normale(text)
    
    # Remove chapter lines
    text = re.sub(r'chapter \w+.', '', text)
    
    # Split text into sentences (simple approach)
    sentences = re.split(r'(?<=[.!?,;\']) +', text)

    # Remove .!?"
    sentences = [re.sub(r'[\d.!?,;"“”\'-)(—-]', '', sentence) for sentence in sentences]

    # Remove empty sentences
    sentences = [sentence for sentence in sentences if sentence != '']

    
    # Remove any leading or trailing whitespace from each sentence
    sentences = [sentence.strip() for sentence in sentences]
    
    return sentences

# Example usage:
file_path = "corpus.txt"
corpus = create_corpus_from_file(file_path)

# Write the formatted corpus to an output file
output_file_path = "formatted_corpus.txt"
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for sentence in corpus:
        output_file.write(sentence + '\n')

# Connect to the CoreNLP server (make sure it is running on port 9000)
parser = CoreNLPParser(url='http://localhost:9000')

# Loop through the sentences and write each parsed sentence to a text file
output_file_path = "formatted_sentences.txt"
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for sentence in corpus:
        # Check if the sentence is not empty or None
        if sentence and sentence.strip() != '':
            parsed_tree = next(parser.raw_parse(sentence))
            output_file.write(str(parsed_tree))