#-*- coding: utf-8 -*-                                                                
"""
This code is preprocessing phrase for auto-completeness in search 

First of all, this code extracts noun sequence from a line 

Second, this code counts the number of nouns and then write dictrionary (noun, jamo, cnt)


""" 

from konlpy.tag import Okt
from collections import OrderedDict
from hangul_util import decompose_word_to_jamo 


DEBUG_LEVEL0 = "debug_level_0" ## No Debug

DEBUG_LEVEL1 = "debug_level_1" ## easy
DEBUG_LEVEL2 = "debug_level_2" ## middle
DEBUG_LEVEL3 = "debug_level_3" ## hard

DEBUG_OPTION = DEBUG_LEVEL1


RAW_CORPUS = "data/news1000-utf8.txt" 
NOUN_DICT = "data/noun_dict"


def read_raw_corpus(path):
    """This function reads raw corpus 

    we deal with the white-space token as a particular token

    Args: 
        path(string): file location

    Return:
        data(list): data lines 
    """

    with open(path, "r") as rf:
        data = [val.strip() for val in rf.readlines() if val != "\n"]
        
    if DEBUG_OPTION in [DEBUG_LEVEL1, DEBUG_LEVEL2, DEBUG_LEVEL3]:
        print("\n\n===== Reading {} =====".format(path))
        print("\nThe number of lines: {}".format(len(data)))
        print("\nThe top 3 lines:\n{}".format(data[0:3]))

    return data

def write_noun_cnt(path, data):
    """This function write the pair (noun, count)


    Args:
        path(string): file location
        data(dict): the dictionary like (noun, val)
    Return:
        None
    """


    with open(path, "w") as wr:
        for key, val in data.items():
            wr.write(key+"\t"+"".join(decompose_word_to_jamo(key))+"\t"+str(val)+"\n")
 
def make_noun_sequence(txt):
    """This fucntion extracts noun sequences 


    To get noun from each line, we use Okt mopheme analyzer

    for Okt analyzer, refer to https://konlpy.org/en/latest/api/konlpy.tag/

    Args(list): text line by line
   
    Returns(list): nouns sequence for each line
    """ 

    okt = Okt()


    noun_data = []
    noun_cnt = OrderedDict ()

    for idx, val in enumerate(txt):

        # To normalize text
        temp = okt.normalize(val)
        if idx == 0 and DEBUG_OPTION in [DEBUG_LEVEL1, DEBUG_LEVEL2, DEBUG_LEVEL3]:
            print("\n\n===== The normalized text =====")
            print("The previous: {}".format(val)) 
            print("The result: {}".format(temp))

        # To extract nouns
        noun_data.extend(okt.nouns(temp))

   
    for idx, val in enumerate(noun_data):
        if noun_cnt.get(val) == None:
            noun_cnt[val] = 1
        else:
            noun_cnt[val] += 1


    sorted_dict = OrderedDict(sorted(noun_cnt.items(), key=lambda t:t[1], reverse=True))
    
    if DEBUG_OPTION in [DEBUG_LEVEL1, DEBUG_LEVEL2, DEBUG_LEVEL3]:
        print("\n===== The result of extracting nouns =====")
        print("\nThe number of nouns: {}".format(len(noun_data)))
        print("\nThe top 3 lines:\n{}".format(noun_data[0:3]))

    return sorted_dict


if __name__ == "__main__":

   new_lines = read_raw_corpus(RAW_CORPUS)

   nouns_dict = make_noun_sequence(new_lines)

   write_noun_cnt(NOUN_DICT, nouns_dict)

