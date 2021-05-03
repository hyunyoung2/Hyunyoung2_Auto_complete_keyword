#-*- coding: utf-8 -*-                                                                   
"""
This code is  auto-completeness in search 

First of all, load dictionary with paris (noun, count)

Second, auto-complete code 

"""

from hangul_util import decompose_word_to_jamo
from make_noun_dict import NOUN_DICT

DEBUGGING = True

def load_dict(path):
    """This function reads noun dict 

    we read file, the file includes sequences (noun, jamo, cnt)

    Args: 
        path(string): file location

    Return:
        data(list): data
    """


    data = []
    with open(path, "r") as rf:
        for val in rf.readlines():
            if val == "\n":
                continue
            else:
                temp = val.strip().split()
                assert len(temp) == 3, "Your dict file is wrong"
                data.append([temp[0], temp[1], int(temp[2])])
        
    if True == DEBUGGING:
        print("\n\n===== Reading {} =====".format(path))
        print("\nThe number of lines: {}".format(len(data)))
        print("\nThe top 3 lines:\n{}".format(data[0:3]))

    return data



def generate_completeness(data, noun_dict):
    """This code generate the most similar candidates

    Args:
       data(string): input keyword
       noun_dict(list): nouns consists of (noun, jamo, cnt)
   
    Returns:
       ranked_list(list): top 3 of the most similar candidates

    """


    input_keyword = "".join(decompose_word_to_jamo(data))

    ranked_list = []

    for idx, val in enumerate(noun_dict):
        if len(val[1]) < len(input_keyword):
            continue
        elif input_keyword == val[1][:len(input_keyword)]:
            ranked_list.append(val[0])
                     
        if len(ranked_list) == 3:
            break
 
    return ranked_list

 
if __name__=="__main__":

    dict_data = load_dict(NOUN_DICT) 

    print("\nIf you want to finish this program, type in 'exit'\n")

    flag = True
    while(flag):

        keyword = input("Type in Keyword: ")

        if " " in keyword:
            keyword = input("Type in keword without white-space: ")

        if keyword.lower() == "exit":
            print("\nThis program is finished\n")
            break

        candidates = generate_completeness(keyword, dict_data)

        if len(candidates) == 0:
            print("\nThe number of the most similar candidates is {}".format(0))
            print("\nType in another keyword")
            continue
  
        print("The list of top 3 candidates which is the most similar\n{}".format(candidates))

       
           







