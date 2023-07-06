# chatbot/utils/register_newwords.py

import re

try:
    with open('project/chatbot/train_tools/dict/corpus.txt', 'r') as original_corpus:
        lines = original_corpus.readlines() 
        
    switching_vocabs = [] 
    for l in lines:
        if '짜장면' in l:
            print(l)
            switching_vocabs.append(re.sub('짜장면', '촐랭이밥', l))

    print(f"num --> {len(switching_vocabs)}")

    with open('project/chatbot/train_tools/dict/input01.txt', 'w', encoding='utf-8') as new_corpus:
        for new_v in switching_vocabs:
            new_corpus.write(new_v)

    with open('project/chatbot/train_tools/dict/corpus02.txt', 'a', encoding='utf-8') as copy_corpus:
        for new_v in switching_vocabs:
            copy_corpus.write(new_v)

except Exception as e :
    print("오류 발생 : ",e)




        
    





