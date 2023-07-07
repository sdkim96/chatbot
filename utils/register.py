# 말뭉치/ner.train/유저 딕셔너리 읽고, 복사하고, 변경하여 추가하는 실행파일입니다.
# 아래 요구사항과 메소드 규칙을 지켜주세요!

# 요구사항 : 모든 클래스의 로직은 다음과 같습니다.
# 1. read_file()를 통하여 읽고 -> 2. copy_file() 하여 기존 파일을 복제하고 -> 
# 3. switch_vocabs()를 통해 원하는 키워드를 다른 키워드로 바꾸고 -> 4. add_lines()를 통하여 해당 파일에 변경사항을 반영하고, ->
# 5. make_file()를 통해 변경사항을 새로운 파일로 저장합니다.(요건 선택사항)

# 메소드 설명 :
    # 반환값이 있는 함수 :
        # .read_file(string 경로) : 파일을 읽어서 [] 형태로 반환합니다.
        # .switch_vocabs(변환할 string 키워드, 변환할 데이터 가져올 []) : 파일을 읽어서 기존 switch_vocabs의 바뀐 내용을 [] or str 형태로 반환합니다.
        # -> 실행하면 input()이 나오면서 변환하고 싶은 키워드를 입력하게 합니다.
    # 반환값이 없는 함수 : 
        # .add_lines(라인 추가할 string 경로, 적을 라인 [])
        # .copy_file(복제할 파일 string 경로, 복제될 파일 string 경로)
        # .make_file(만들 파일 string 경로, 적을 라인 [])

# 메소드 중에 .switch_vocabs()의 반환값은 _corp() 면 [], _Ner()면 [], _Dict()면 str를 반환합니다.

import os
from Registering_module import *

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("1. Corpus.txt 바꾸기")
        print("2. ner_train.txt 바꾸기")
        print("3. user_dic.tsv 바꾸기")
        print("4. 종료")
        choice = input("옵션을 고르세요 : ")

        if choice == "1":
            while True:
                print("1. 파일 읽기")
                print("2. 뒤로")
                choice_1 = input("옵션을 고르세요 : ")

                corpus = RegisterNewwords_Corp(path='project/chatbot/utils/user_dic3.tsv')

                if choice_1 == "1":
                    corpus_original_file = corpus.read_file('project/chatbot/train_tools/dict/corpus.txt')

                    print("1. 원본 파일 수정")
                    print("2. 복제 파일 생성 후 수정")
                    print("3. 뒤로")
                    choice_1_1 = input("옵션을 고르세요 : ")

                    if choice_1_1 == "1":
                        before_switching_vocab = input('원본 파일의 바꿀 키워드를 입력하세요: ')
                        after_switching_vocab = corpus.switch_vocabs(before_switching_vocab, corpus_original_file)
                        corpus.add_lines('project/chatbot/train_tools/dict/corpus.txt', after_switching_vocab)
                        corpus.make_file('project/chatbot/train_tools/dict/input03.txt', after_switching_vocab)

                    elif choice_1_1 == "2":
                        copyfile_name = input("복제 파일의 이름을 설정하세요. (경로는 같습니다, .txt는 제외하고 이름만 작성하세요) : ")
                        before_switching_vocab = input('원본 파일의 바꿀 키워드를 입력하세요: ')
                        corpus.copy_file('project/chatbot/train_tools/dict/corpus.txt', f'project/chatbot/train_tools/dict/{copyfile_name}.txt')
                        corpus_copy_file = corpus.read_file(f'project/chatbot/train_tools/dict/{copyfile_name}.txt')
                        after_switching_vocab = corpus.switch_vocabs(before_switching_vocab, corpus_copy_file)
                        corpus.add_lines(f'project/chatbot/train_tools/dict/{copyfile_name}.txt', after_switching_vocab)
                        corpus.make_file(f'project/chatbot/train_tools/dict/{copyfile_name}_input.txt', after_switching_vocab)

                    elif choice_1_1 == "3":
                        break
                    else:
                        print("옵션을 다시 선택하세요.")
                        continue

                elif choice_1 == "2":
                    break
                else:
                    print("옵션을 다시 선택하세요.")
                    continue

        elif choice == "2":
            while True:
                ner = RegisterNewwords_Ner(path='project/chatbot/utils/user_dic3.tsv')
                
                print("1. 파일 읽기")
                print("2. 뒤로")
                choice_2 = input("옵션을 고르세요 : ")

                if choice_2 == "1":
                    ner_original_file = ner.read_file('project/chatbot/models/ner/ner_train.txt')

                    print("1. 원본 파일 수정")
                    print("2. 복제 파일 생성 후 수정")
                    print("3. 뒤로")
                    choice_2_1 = input("옵션을 고르세요 : ")

                    if choice_2_1 == "1":
                        before_switching_vocab = input('원본 파일의 바꿀 키워드를 입력하세요: ')
                        after_switching_vocab = ner.switch_vocabs(before_switching_vocab, ner_original_file)
                        ner.add_lines('project/chatbot/models/ner/ner_train.txt', after_switching_vocab)
                        
                    elif choice_2_1 == "2":
                        copyfile_name = input("복제 파일의 이름을 설정하세요. (경로는 같습니다, .txt는 제외하고 이름만 작성하세요) : ")
                        before_switching_vocab = input('원본 파일의 바꿀 키워드를 입력하세요: ')
                        ner.copy_file('project/chatbot/models/ner/ner_train.txt', f'project/chatbot/models/ner/{copyfile_name}.txt')
                        ner_copy_file = ner.read_file(f'project/chatbot/models/ner/{copyfile_name}.txt')
                        after_switching_vocab = ner.switch_vocabs(before_switching_vocab, ner_copy_file)
                        ner.add_lines(f'project/chatbot/models/ner/{copyfile_name}.txt', after_switching_vocab)

                    elif choice_2_1 == "3":
                        break
                        
                    else:
                        print("옵션을 다시 선택하세요.")
                        continue
                        
                elif choice_2 == "2":
                    break

                else:
                    print("옵션을 다시 선택하세요.")
                    continue
                    
        elif choice == "3":
            while True:
                dic = RegisterNewwords_Dict(path='project/chatbot/utils/user_dic3.tsv')
                
                print("1. 파일 읽기")
                print("2. 뒤로")
                choice_3 = input("옵션을 고르세요 : ")

                if choice_3 == "1":
                    dic_original_file = dic.read_file('project/chatbot/utils/user_dic.tsv')

                    print("1. 원본 파일 키워드 추가")
                    print("2. 복제 파일 키워드 추가")
                    print("3. 뒤로")
                    choice_3_1 = input("옵션을 고르세요 : ")

                    if choice_3_1 == "1":
                        after_adding_vocab = dic.commit_word()
                        dic.add_lines(dic_original_file, after_adding_vocab)
                        
                    elif choice_3_1 == "2":
                        copyfile_name = input("복제 파일의 이름을 설정하세요. (경로는 같습니다, .tsv는 제외하고 이름만 작성하세요) : ")
                        dic.copy_file('project/chatbot/utils/user_dic.tsv', f'project/chatbot/utils/{copyfile_name}.tsv')
                        dic_copy_file = dic.read_file(f'project/chatbot/utils/{copyfile_name}.tsv')
                        after_adding_vocab = dic.commit_word()
                        dic.add_lines(f'project/chatbot/utils/{dic_copy_file}.tsv', after_adding_vocab)

                    elif choice_3_1 == "3":
                        break
                        
                    else:
                        print("옵션을 다시 선택하세요.")
                        continue
                        
                elif choice_3 == "2":
                    break

                else:
                    print("옵션을 다시 선택하세요.")
                    continue
                
        elif choice == "4":
            break
            
        else:
            print("Invalid option. Please enter a number between 1 and 4.")
            continue

menu()