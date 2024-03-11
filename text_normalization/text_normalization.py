# nltk kütüphanesinden gerekli modülleri import ediyoruz
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# 1) Case Normalization (Büyük/Küçük Harf Normalleştirme)
text_case = "The quick BROWN Fox Jumps OVER the lazy dog."
text_case = text_case.lower()

# 2) Punctuation Removal (Noktalama İşaretlerinin Kaldırılması)
text_punctuation = "The quick BROWN Fox Jumps OVER the lazy dog!!!"
text_punctuation = text_punctuation.translate(str.maketrans("", "", string.punctuation))

# 3) Stop Word Removal (Durak Kelime Kaldırma)
nltk.download('stopwords')
text_stopwords = "The quick BROWN Fox Jumps OVER the lazy dog."
stop_words = set(stopwords.words("english"))
words = text_stopwords.split()
filtered_words = [word for word in words if word.lower() not in stop_words]
text_stopwords = " ".join(filtered_words)

# 4) Stemming (Kök Çıkarma)
stemmer = PorterStemmer()
text_stemming = "running,runner,ran"
words = text_stemming.split(",")
stemmed_words = [stemmer.stem(word) for word in words]
text_stemming = ",".join(stemmed_words)

# 5) Lemmatization
lemmatizer = WordNetLemmatizer()
text_lemmatization = "running,runner,ran"
lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in text_lemmatization.split(",")]
text_lemmatization = ",".join(lemmatized_words)

# 6) Tokenization (Belirteçleme)
text_tokenization = "The quick BROWN Fox Jumps OVER the lazy dog."
text_tokenization = re.sub(r'[^\w\s]', '', text_tokenization)
tokens = word_tokenize(text_tokenization)

# 7) Replacing synonyms and Abbreviation to their full form to normalize the text in NLP (Eşanlamlıları ve Kısaltmaları Tam Hâllerine Dönüştürme)
text_synonyms = "I'll be there at 2pm"
synonyms = {"I'll": "I will", "2pm": "2 pm"}
for key, value in synonyms.items():
    text_synonyms = text_synonyms.replace(key, value)

# 8) Removing numbers and symbol to normalize the text in NLP (Sayıların ve Sembollerin Kaldırılması)
text_numbers = "I have 2 apples and 1 orange #fruits"
text_numbers = re.sub(r"[\d#]", "", text_numbers)

# 9) Removing any remaining non-textual elements to normalize the text in NLP (Kalan Metin Dışı Unsurların Kaldırılması)
text_non_textual = "Please visit <a href='www.example.com'>example.com</a> for more information or contact me at info@example.com"
text_non_textual = re.sub(r"(<[^>]+>)|(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)", "", text_non_textual)

# 10) Birleştirilmiş Normalizasyon Fonksiyonu
def normalize_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    nltk.download('stopwords')
    stop_words = set(stopwords.words("english"))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    text = " ".join(filtered_words)

    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in text.split()]
    text = " ".join(stemmed_words)

    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in text.split()]
    text = " ".join(lemmatized_words)

    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)

    synonyms = {"I'll": "I will", "2pm": "2 pm"}
    for key, value in synonyms.items():
        text = text.replace(key, value)
   
    text = re.sub(r"[\d#]", "", text)

    text = re.sub(r"(<[^>]+>)|(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)", "", text)

    return text

# Test metni
text = "The quick BROWN Fox Jumps OVER the lazy dog. I'll be there at 2pm. Please visit <a href='www.example.com'>example.com</a> for more information or contact me at info@example.com"
# Tüm normalizasyon tekniklerini içeren fonksiyonun uygulanması
normalized_text = normalize_text(text)

# Normalizasyon yöntemlerinin çıktıları
print("Case Normalization (Büyük/Küçük Harf Normalleştirme):")
print(text_case)
print("\nPunctuation Removal (Noktalama İşaretlerinin Kaldırılması):")
print(text_punctuation)
print("\nStop Word Removal (Durak Kelime Kaldırma):")
print(text_stopwords)
print("\nStemming (Kök Çıkarma):")
print(text_stemming)
print("\nLemmatization:")
print(text_lemmatization)
print("\nTokenization (Belirteçleme):")
print(tokens)
print("\nReplacing synonyms and Abbreviation to their full form to normalize the text in NLP (Eşanlamlıları ve Kısaltmaları Tam Hâllerine Dönüştürme):")
print(text_synonyms)
print("\nRemoving numbers and symbol to normalize the text in NLP (Sayıların ve Sembollerin Kaldırılması):")
print(text_numbers)
print("\nRemoving any remaining non-textual elements to normalize the text in NLP (Kalan Metin Dışı Unsurların Kaldırılması):")
print(text_non_textual)
print("\nBirleştirilmiş Normalizasyon Fonksiyonu:")
print(normalized_text)
