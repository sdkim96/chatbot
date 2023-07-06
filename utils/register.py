from Registering_module import *

corps = RegisterNewwords_corp()

# lines = corps.read_file('project/chatbot/train_tools/dict/corpus.txt')
# corps.copy_file('project/chatbot/train_tools/dict/corpus.txt', 'project/chatbot/train_tools/dict/corpus02.txt')
# v = corps.switch_vocabs('짜장면', lines)
# corps.add_lines('project/chatbot/train_tools/dict/corpus02.txt', v)
# corps.make_file('project/chatbot/train_tools/dict/input01.txt', v)

ner = RegisterNewwords_Ner()

ner.add_entity('강냉이')

