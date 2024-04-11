import re
from contection_to_normale import contection_to_normale

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
    sentences = [re.sub(r'[.!?,;"“”\']', '', sentence) for sentence in sentences]

    # Remove empty sentences
    sentences = [sentence for sentence in sentences if sentence != '']

    
    # Remove any leading or trailing whitespace from each sentence
    sentences = [sentence.strip() for sentence in sentences]
    
    return sentences

# Example usage:
file_path = "Alice_and_the_wonderland.txt"
corpus = create_corpus_from_file(file_path)
# Format the corpus to remove newline characters
formatted_corpus = '\n'.join(corpus)

# Write the formatted corpus to an output file
output_file_path = "formatted_corpus.txt"
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(formatted_corpus)
