import pickle
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
from yellowbrick.text import TSNEVisualizer


def plot_bar_x(labels, values):
    """

    :param labels: classes
    :param values: num occurence
    :return: plot
    """
    # this is for plotting purpose
    index = np.arange(len(labels))
    plt.bar(index, values)
    plt.xlabel('Tags', fontsize=5)
    plt.ylabel('No of Occurence', fontsize=5)
    plt.xticks(index, labels, fontsize=5, rotation=30)
    plt.title('Tags distributions')
    plt.show()


def word_cloud(text):
    """
        word cloud from text
    :param text:
    :return:
    """
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def tsne_visualization(df):
    """
        T-sne representation of corpus
    :param df:
    :return:
    """
    # load data
    # corpus = load_corpus('hobbies')
    tfidf = TfidfVectorizer()
    corpus = df.loc[df['language'] == "eng"]
    abstr = tfidf.fit_transform(corpus["text_final"])

    # Create the visualizer
    tsne = TSNEVisualizer()
    tsne.fit(abstr, corpus["tag"])
    tsne.poof()


def lexical_richness_measures(df):
    """
        Lexicla richness measures
    :param df:
    :return: None
    """
    corpus = []
    for index, row in df.iterrows():
        corpus += literal_eval(row["text_final"])

    vocabulary_size = len(set(corpus))
    corpus_size = len(corpus)
    print("Abstract number",df["abstract"].count())
    print("Vocabulary size: ", vocabulary_size)
    print("Corpus size: ", corpus_size)
    print("Vocabulary richness: ", vocabulary_size/corpus_size)
    print("Abstract Mean words: ", corpus_size / df["abstract"].count())
    print("Number of class", len(set(df["tag"])))
    print("")


def classes_distribution(df):
    """
        Classe distribution
    :param df:
    :return:
    """
    d_tags = Counter(df['tag'])
    print("Class        :       nb_occurence:")
    for elt in d_tags:
        print(elt, "              ", d_tags[elt])


if __name__ == "__main__":
    df = pickle.load(open('../dataset/preprocessed_eng_dataset.pickle', 'rb'))
    lexical_richness_measures(df)
    classes_distribution(df)
