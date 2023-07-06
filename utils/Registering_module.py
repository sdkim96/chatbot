import re
from Preprocess import Preprocess


#switch_vocabs 메소드는 무조건 read_file()되고 나서 실행되야함 받아들이는 인자가 리스트 형식임.

class RegisterNewwords:
    def __init__(self):
        pass

    def read_file(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.readlines()
        except Exception as e:
            print(e)
            return []

    def copy_file(self, source_path, target_path):
        try:
            with open(source_path, 'r', encoding='utf-8') as src, open(target_path, 'w', encoding='utf-8') as tgt:
                for line in src:
                    tgt.write(line)
        except Exception as e:
            print(e)

    def switch_vocabs(self, v1, lines):      
        v2 = input(f"{v1}을 무엇으로 바꿀까요?")
        if not v2:
            print('바꿀 대상을 입력하세요.')
            return None
        else:
            switching_vocabs = [re.sub(v1, v2, line) for line in lines if v1 in line]
            print(f"총 바뀐 길이 --> {len(switching_vocabs)}")
            return switching_vocabs

    def add_lines(self, file_path, lines):
        try:
            with open(file_path, 'a', encoding='utf-8') as a:
                for line in lines:
                    if line == lines[0]:
                        a.write('\n')
                        a.write(line)
                    else:
                        a.write(line)
        except Exception as e:
            print(e)

    def make_file(self, file_path, lines):
        try:
            with open(file_path, 'w', encoding='utf-8') as s:
                for line in lines:
                    s.write(line)
        except Exception as e:
            print(e)

class RegisterNewwords_corp(RegisterNewwords):
    pass
  


class RegisterNewwords_Ner(RegisterNewwords):
    def __init__(self):
        super().__init__()

    def add_entity(self, food):
        line_input = input('입력하고 싶은 문장을 입력하세요. (음식 이름이 제일 앞에 와야합니다.) ')
        
        pp = Preprocess()
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

    def remove_entity(self, file_path):
        delete_lines = input('지우고 싶은 문구를 입력하세요')
        
        with open(file_path, 'r') as whole_lines:
            whole_lines.readlines()

        for line in whole_lines:
            if delete_lines in line:
                pass # 수정해야됨.

                 
        

        



    def search_entity(self):
        search_lines = input('찾고 싶은 문구를 검색하세요.')


        

class RegisterNewwords_Dict(RegisterNewwords):
    def __init__(self):
        super().__init__()

    def add_word(self):

        pass

    def remove_word(self):

        pass
