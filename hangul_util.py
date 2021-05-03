# -*- coding: utf-8 -*-

class Jamo():
    """
    Hangul consists of 14 consonants(자음) and 10 vowels(모음)
      
    """
    # Check the Hangul unicod table in https://jjeong.tistory.com/696
    # Unicode for Hangul
    # oxAC00 ('가')
    # 0xAC00 + (Chosung_index * JUNGSUNGS_NUM * JONGSUNGS_NUM) + (Jungsung_index * JONGSUNGS_NUM) + (Jongsung_index)
    CHO = [ "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ",
            "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
    JUNG = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ",
            "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
    JONG = ["<non-jong>", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ",
            "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ",
            "ㅍ", "ㅎ" ]

    JAMO = CHO + JUNG + JONG

    Cho_num = len(CHO) # 19
    Jung_num = len(JUNG) # 21
    Jong_num = len(JONG) # 28

class Hangul():
    FIRST_HANGUL = "가"
    FIRST_HANGUL_UNICODE = 0xAC00 #'가'
    LAST_HANGUL = "힝"
    LAST_HANGUL_UNICODE = 0xD7A3 #'힣'

def is_hangul(token):
    """Check if the token is hangul.

    https://jjeong.tistory.com/696

    https://github.com/bluedisk/hangul-toolkit     

    ord function is built-in function that return unicode value
    """
    code = ord(token)
    
    if  Hangul.FIRST_HANGUL_UNICODE <= code and code <= Hangul.LAST_HANGUL_UNICODE:
        return True

    else:
        return False


def decompose_index(token):
    """Return the index number of jamo, which is cho, jung, jong 

    If you understand this URL below 
        https://frhyme.github.io/python/python_korean_englished/   
    """

    ## chosung chages in period which is 588(21*28)

    code = hangul_unicode_index(token)

    ## Cho_num = len(CHO) # 19
    ## Jung_num = len(JUNG) # 21
    ## Jong_num = len(JONG) # 28

    cho = code//(Jamo.Jung_num*Jamo.Jong_num) #(21*28)

    code = code - (Jamo.Jung_num*Jamo.Jong_num*cho) #(21*28*cho)

    # jungsung is 28 in total
    jung = code//Jamo.Jong_num #28

    jong = code - Jamo.Jong_num*jung #28*jung

    return cho, jung, jong


def decompose_jamo(token):
    """character by character 

    """
    if len(token) != 1:
        raise Exception("The token has the lenghth of 1, {}!! When you call the function named decompose_jamo",format(token))

    jamo_list = []

    cho, jung, jong = decompose_index(token)

    jamo_list.extend([Jamo.CHO[cho], Jamo.JUNG[jung], Jamo.JONG[jong]])

    return jamo_list

def hangul_unicode_index(token):
    """
    """
    return ord(token) - ord(Hangul.FIRST_HANGUL)

def is_jamo(token):
    """Check whether the token is included in JAMO of Korean

    Korean character can be split into jamo unit.

    The set of jamo is three sets, one is chosung and some is jungsung, the other one is jongsung 

    Input:
        - token(str): character
    Output(boolean):
    """
    
    if token in Jamo.JAMO:
        return True
  
    else:
        return False 

def decompose_word_to_jamo(word):
    """This function doesn't matter 

    word is string or  a list consting of a seqeucne of character in a word.

    word = "각!홍"  or ['각', '!', '홍']
    
    """

    if " " in word:
        raise Exception("Your input includes more than a white-sapce token '{}', when you decompose your word".format(word))

    j_list =  []

    for wIdx, wVal in enumerate(word):
        if is_hangul(wVal):
            j_list.extend(decompose_jamo(wVal))
        else:
            j_list.append(wVal)      

    return j_list

if __name__ == "__main__":

   test = "1a각@홍우ㄷㄲ힋해왕"
  
   print("Test: length of {} with '{}'".format(len(test), test))
   print(decompose_word_to_jamo(word=test))    
  
