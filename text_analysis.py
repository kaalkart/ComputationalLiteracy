from nltk import FreqDist
from nltk.corpus import stopwords
import MeCab

# Configuring the stopwords that need to be excluded from the analysis -
stopWords = set(stopwords.words('Japanese'))

def create_statistics(search_word, source_text, index):
    # Add an entry to the list for each time that the search word appears in the text - 
    filtered_tokens=[word for word in source_text if word == search_word]
    co_occur=FreqDist()
    # For cleaning up the file for every program run - 
    if index == 1:
        with open(r"./analysis_final.txt", "w", encoding='utf-8') as first_time:
            first_time.write(f"This is statistics about {search_word}: \n")
    # Otherwise append to the file -
    else:
        with open(r"./analysis_final.txt", "a", encoding='utf-8') as other_time:
            other_time.write(f"This is statistics about {search_word}: \n")
    # Find the context around the places with the search word -
    for i, word in enumerate(filtered_tokens):
        context=source_text[max(0, i-5): i] + source_text[i+1: min(len(source_text), i+6)]
        co_occur.update(context)
    # Write the statistics of the most common 50 context words into the file -
    with open(r"./analysis_final.txt", "a", encoding='utf-8') as output_file:
        for i in co_occur.most_common(50):
            output_file.write("".join(map(str, i)))
        output_file.write("\n")

# Define the text that will be analysed
with open('Tanizaki_texts_final.txt', 'r', encoding='utf-8') as file:
    Tanizaki_texts = file.read()
Tanizaki_texts = Tanizaki_texts.encode('utf-8').decode('utf-8')
mecab=MeCab.Tagger("-Owakati")
# Remove whitespaces from the text -
tokens=mecab.parse(Tanizaki_texts).split()
new_tokens = []

# Filter out stopwords -
for i in tokens:
    for a in i:
        if a not in stopWords:
            new_tokens.append(a)

# Defining the specific search words around which we want to analyse the context -
specif_words=['体', '姿', '身', '形', '隠', '影', '格', '女', '男', '性', '彼', '者', '方', '人', '服', '装', '態', '袴', '袖', '髪']
index = 1

# Analyse the words one by one using the function defined above -
for i in specif_words:
    create_statistics(i, new_tokens, index)
    index += 1