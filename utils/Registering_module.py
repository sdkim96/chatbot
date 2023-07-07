# 사용자 정의 모듈입니다.
# 메소드 반환 규칙 : return값을 가지는 모든 메소드들은 무조건 리스트의 형식이어야 합니다.
#                   단, 이 규칙에 해당하지 않는 메소드는 commit_word() 하나뿐임. 
# 명명 규칙 - add ~ : 실제 파일에 추가. commit ~ : git의 commit의 형태(return [])
# 인자 규칙 - lines : [], ~path : 'your/path'

import re
from Preprocess import Preprocess

# 아래 클래스는 새로운 단어를 추가하는데 정의된 부모 클래스입니다.
class RegisterNewwords:
    def __init__(self, path):

        # 클래스의 생성자는 사용자 정의 사전입니다.
        # 사용자 정의 사전을 불러옴으로써 Preprocess 클래스의 객체들에 인자로 넘기기 수월하게 했습니다. 
        self.path = path
        self.keyword_tags = self._load_keyword_tags(self.path)


    # 파일을 읽습니다. 파일의 줄을 하나하나 읽어 리스트의 형태로 반환합니다.
    def read_file(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.readlines()
        except Exception as e:
            print(e)
            return []


    # 파일을 복제합니다. 반환값은 없습니다.
    def copy_file(self, source_path, target_path):
        try:
            with open(source_path, 'r', encoding='utf-8') as src, open(target_path, 'w', encoding='utf-8') as tgt:
                for line in src:
                    tgt.write(line)
        except Exception as e:
            print(e)


    # 기본적으로 corpus.txt 인 경우에 작동되게 합니다. 다른 형식의 파일들은 해당 형식의 자식클래스에서 오버라이딩 됩니다.
    # 아래 메소드는 무조건 read_file()되고 나서 실행되야합니다. 받아들이는 인자가 리스트 형식입니다.
    def switch_vocabs(self, v1, lines):      
        v2 = input(f"{v1}을 무엇으로 바꿀까요?")
        if not v2:
            print('바꿀 대상을 입력하세요.')
            return None
        else:
            switching_vocabs = [re.sub(v1, v2, line) for line in lines if v1 in line]
            print(f"총 바뀐 길이 --> {len(switching_vocabs)}")
            return switching_vocabs


    # commit된 함수들(우리 클래스에서 switch, commit로 정의된 함수들)을 인자로 받아서 해당 파일에 실제로 'add' 합니다.
    # 즉 아래 메소드는 무조건 commit이 되고 실행되야함.
    def add_lines(self, path, lines):
        try:
            with open(path, 'a', encoding='utf-8') as a:

                # 만약 lines가 list 형식이면
                if isinstance(lines, list):
                    for line in lines:
                        if line == lines[0]:
                            a.write('\n')
                            a.write(line)
                        else:
                            a.write(line)
                else:
                    a.write('\n')
                    a.write(lines)

        except Exception as e:
            print(e)


    # lines 로 등록된 파일을 path에 새로 만듭니다.
    def make_file(self, path, lines):
        try:
            with open(path, 'w', encoding='utf-8') as s:
                for line in lines:
                    s.write(line)
        except Exception as e:
            print(e)


    # 생성자에 정의된 메소드인데, 우리 사용자 사전의 형식을 받아와서 1시\tNNG를 기준으로 위에는 B_FOOD로 태깅하고 아래는 B_DT로 태깅합니다. 
    # 이 메소드는 실제로 유저가 사용하는 함수는 아니기 때문에 메소드 앞에 _(언더스코어)를 붙여 캡슐화합니다. 
    def _load_keyword_tags(self, userdic_path):
        keyword_tags = {} 
        time_tag = False

        with open(userdic_path, 'r', encoding='utf-8') as f:
            for line in f:
                keyword = line.strip()
                if keyword == '1시\tNNG':
                    time_tag = True

                tag = 'B_DT' if time_tag else 'B_FOOD'
                keyword_tags[keyword] = tag

        return keyword_tags


    # 이 메소드는 실제로 유저가 사용하는 함수는 아니기 때문에 메소드 앞에 _(언더스코어)를 붙여 캡슐화합니다. 
    # 이 메소드는 {} 형태의 데이터를 가져와 키와 값중 키에 해당하는 값을 반환합니다. 아무것도 해당하지 않는 경우엔 O로 태깅합니다. (B_FOOD, B_DT, O)
    def _decide_pos_final(self, keyword):
        keyword = keyword+'\tNNG'
        return self.keyword_tags.get(keyword, 'O')


# Corp 클래스는 부모클래스와 기능적으로 동일합니다.
class RegisterNewwords_Corp(RegisterNewwords):
    pass
  

# Ner 클래스는 ner_train.txt 기준으로 작성되었습니다.
class RegisterNewwords_Ner(RegisterNewwords):
    def __init__(self, path):
        super().__init__(path)


    # add_lines 오버라이딩 
    def add_lines(self, path, lines):
        try:
            with open(path, 'a', encoding='utf-8') as a:
                for line in lines:
                    a.write('\n')
                    a.write(line)
                    
        except Exception as e:
            print(e)


    # switch_vocabs 오버라이딩 -> ;가 첫글자인 문장을 가지고 바꿀 단어가 있으면 그 문장을
    # 형태소 분석을 하여 새롭게 엔터티 형성 
    def switch_vocabs(self, v1, lines):      
        v2 = input(f"{v1}을 무엇으로 바꿀까요?")
        if not v2:
            print('바꿀 대상을 입력하세요. : ')
            return None
        else:
            switching_vocabs_list = []
            create_entities = []
            
            pp = Preprocess(userdic=self.path)

            # 1. ner_train.txt 에 바꿀 대상의 문장을 모두 가져와서 switching~ []에 넣음.
            # ex) 가락지빵 먹고싶어요, 가락지빵 주문할래요 ... 
            for line in lines:
                if line[0] == ';' and v1 in line:
                    switching_vocabs_list.append(line)
                else:
                    continue
            
            # 2. 바꿀 대상의 문장에 있는 v1들을 찾아 전부 v2키워드로 바꿈
            switching_vocabs_list = [re.sub(v1, v2, v1s).replace(';','') for v1s in switching_vocabs_list]

            # 3. 그 문장 하나하나에 대해 형태소 분석시작
            # ex) l = ; 가락지빵 먹고싶어
            for l in switching_vocabs_list:
                pos = pp.pos(l)
                num = 1
                lines = []
                # entity_first_row = '; 가락지빵 먹고싶어\n'
                entity_first_row = f";{l}"

                # pos = [(가락지빵, NNG), (먹, ASDF) ,...]
                # v = (가락지빵, NNG)
                for v in pos:
                    # final엔 가락지빵, 먹, ... 등등의 형태소가 B_FOOD or B_DT or O 인지 구분함
                    final = self._decide_pos_final(v[0])

                    # 가락지빵이 B_FOOD이니까, entity_second_row엔 가락지빵 먹고싶어에서 가락지빵만
                    # <가락지빵:FOOD>가 되어 문장 똑같이 들어감.
                    # 즉, 1줄에서 음식이름만 <>형식대로 적히는거임. 
                    if 'B_FOOD' == final:
                        entity_food = f"<{v[0]}:FOOD>"
                        entity_second_row = entity_first_row.replace(v[0], entity_food).replace('; ', '$')
                    # 음식이 아닌 것들은 두번째줄이 첫번쨰줄과 같음.(앞의 태깅만 달라짐)
                    else:
                        entity_second_row = entity_first_row.replace('; ', '$')

                    # lines = 1 가락지빵 NNG B_FOOD
                    #       = 2 먹 ASDF O <- 이런식으로 들어감 대신 lines는 리스트 형태임
                    line = f"{num}\t{v[0]}\t{v[1]}\t{final}"
                    lines.append(line)
                    num += 1

                entity = entity_first_row + entity_second_row + '\n'.join(lines) +'\n'
                create_entities.append(entity)

            return create_entities
        

    # commit 형식의 함수. (git의 commit 생각하면 좋음 []를 반환합니다.)
    def commit_entity(self, food):
        line_input = input('입력하고 싶은 문장을 입력하세요. (음식 이름이 제일 앞에 와야합니다.) ')
        
        pp = Preprocess(userdic=self.path)
        pos = pp.pos(line_input)
        num = 1
        lines = []

        for p in pos:
            if food in p:
                final = "B_FOOD"
            else:
                final = "O"

            line = f"{num}\t{p[0]}\t{p[1]}\t{final}"
            lines.append(line)
            num += 1

        # 입력한 문장에서 food를 제외한 나머지 부분을 추출
        remaining_sentence = line_input.replace(food, "").strip()
        
        entity = f"; {line_input}\n$<{food}:FOOD> {remaining_sentence}\n"
        for l in lines:
            entity += l + '\n'

        print(entity)
        entity_lines = entity.split('\n')

        return entity_lines
       

# Dict 클래스는 user_dic.tsv 기준으로 작성되었습니다.
class RegisterNewwords_Dict(RegisterNewwords):
    def __init__(self, path):
        super().__init__(path)


    # 이 메소드만 반환값이 스트링임.
    def commit_word(self):
        word = input('추가하고 싶은 키워드를 입력하세요(NNG만 해당)')
        commit_word = f"{word}\tNNG"

        return commit_word
    
    # 이 메소드는 사용자가 잘못 사용할 경우에 데이터의 손상이 올수 있어서 오버라이딩함.
    def switch_vocabs(self):
        pass
