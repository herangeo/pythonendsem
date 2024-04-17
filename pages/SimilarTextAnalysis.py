import nltk
import pandas as pd
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

df = pd.read_csv('WomensClothingE-CommerceReviews.csv')

def preprocess_text(text):

    tokens = nltk.word_tokenize(text.lower())
    

    tokens = [token for token in tokens if token.isalnum()]
    

    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]



    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    

    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    
    return tokens



df = pd.read_csv('WomensClothingE-CommerceReviews.csv')


text1_reviews = df['text'][:20]


text2_reviews = df['text'][20:40]


with open('Text1.txt', 'w', encoding='utf-8') as text1_file:
    for review in text1_reviews:
        text1_file.write(review + '\n')


with open('Text2.txt', 'w', encoding='utf-8') as text2_file:
    for review in text2_reviews:
        text2_file.write(review + '\n')



tokens1 = set(preprocess_text(Text1))
tokens2 = set(preprocess_text(Text2))

similarity_score = jaccard_similarity(tokens1, tokens2)
print(f"Jaccard Similarity: {similarity_score}")
print(f"Tokens 1: {tokens1}\nTokens 2: {tokens2}")

vectorizer = TfidfVectorizer()
vector1 = vectorizer.fit_transform([' '.join(tokens1)])
vector2 = vectorizer.transform([' '.join(tokens2)])

cos_similarity = cosine_similarity(vector1, vector2)


df['proccessed_text'] = df['text'].apply(preprocess_text)


scores = [0.22837370242214533, 0.5935921]
methods = ['Jaccard Similarity', 'Cosine Similarity']

# Bar plot
plt.figure(figsize=(8, 5))
plt.bar(methods, scores, color=['blue', 'green'])
plt.xlabel('Similarity Method')
plt.ylabel('Similarity Score')
plt.title('Comparison of Similarity Scores')
plt.ylim(0, 1)  # Set the y-axis limit from 0 to 1
plt.show()

give me streamlit code to plot all these