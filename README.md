## Auto-complete keyword Assignment 

For assignment to make input in search engine complete


File for me to use, You can download in the site, https://cafe.naver.com/nlpk


file name : news1000-utf8.zip


When you run this respository, Keep in mind the location of new1000-utf8 file.

Keep it under data directory


Above all, you have to run the following code

```
python3 make_noun_dict.py

```

The above makse a dictionary which consists of pairs (noun, jamo seqeunce of the noun, count).

  - noun: are extracted by Konlpy's Okt 

  - jamo sequence of the noun: the nouns is decomposed into jamo sequence

  - count: the number of the noun in new1000-utf8 file


Finally, run the file below:

```
python3 main.py
```

After that, Thie program is implemented as follows:

![]()

