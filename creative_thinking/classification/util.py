import os
import pickle


def to_pickel(pickle_name, dataframe, dir="../dataset"):
    """
        save dataframe on pickle format
    :param dataframe:
    :param dir:
    :return:
    """
    os.chdir(dir)
    pickle.dump(dataframe, open(pickle_name + '.pickle', 'wb'))


def file_to_list(filename, dir="../resources"):
    """
        Build list from file, where each row in file is saved as a string in list
    :param filename:
    :param dir:
    :return: list
    """
    os.chdir(dir)
    vocabulary = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        vocabulary.append(line.replace("\n", ""))
    return vocabulary
