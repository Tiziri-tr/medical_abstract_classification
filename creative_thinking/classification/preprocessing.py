import pickle
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from classification.util import to_pickel, file_to_list

vocabulary = file_to_list("biomedical_vocabulary.txt")


# springer_english_train_V4.2 tokenizer + stop word remover + lower case
def english_preprocessing(text):
    """
        Remove stop words + remove words not in medical vocabulary + remove numeric values
    :param text:
    :return: list of words
    """
    return [word.lower() for word in word_tokenize(text) if
            word in vocabulary and word.isalnum() and word not in stopwords.words('springer_english_train_V4.2')]


# springer_german_train_V4.2 tokenizer + stop word remover + lower case
nlp = spacy.load('de_core_news_sm')

def german_preprocessing(text):
    doc = nlp(text)
    return [token.text.lower() for token in doc if
            token.text not in stopwords.words('springer_german_train_V4.2') and token.text.isalpha()]

    # Word embedding
    # biomedical terminologies word embedding


embedding_path = "/home/animal/Bureau/think_collective/pubmed2018_w2v_200D/pubmed2018_w2v_200D.bin"
# word_vectors = KeyedVectors.load_word2vec_format(embedding_path, binary=True)
# def wprd_embedding(word):
# print(word_vectors.most_similar(positive=[word]))
# return word_vectors.word_vec(word)


if __name__ == "__main__":
    corpus = pickle.load(open('../dataset/dataset.pickle', 'rb'))
    # preprocessing
    corpus['text'] = [word_tokenize(entry.lower()) for entry in corpus['abstract']]
    print("Start..")
    for index, row in corpus.iterrows():
        Final_words = []
        if row["language"] == "eng":
            Final_words = english_preprocessing(row["abstract"])
        elif row["language"] == " ger":
            Final_words = german_preprocessing(row["abstract"])
        else:
            Final_words = []
        corpus.loc[index, 'text_final'] = str(Final_words)
    print("Dump pickle..")
    eng_corpus = corpus.loc[corpus['language'] == "eng"]
    # ger_corpus = corpus.loc[corpus['language'] == "ger"]
    to_pickel("preprocessed_eng_dataset", eng_corpus)
    corpus = pickle.load(open('../dataset/preprocessed_eng_dataset.pickle', 'rb'))
    print(corpus["text_final"])
