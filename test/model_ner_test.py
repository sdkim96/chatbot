from utils.Preprocess import Preprocess_1
from models.ner.NerModel import NerModel

p = Preprocess_1(word2index_dic='project/chatbot/train_tools/dict/chatbot_dict.bin',
                 userdic='project/chatbot/utils/user_dic.tsv')


ner = NerModel(model_name='project/chatbot/models/ner/ner_model_with_userdic.h5', preprocess=p)


query = '오늘 오전 13시 2분에 탕수육 주문 하고 싶어요'
query1 = "오늘 오전 13시 2분에 우라늄회 주문 하고 싶어요"    
query2 = "오늘 오전 13시 2분에 우럭회 주문 하고 싶어요"    
query3 = "오늘 오전 13시 2분에 짜장면 주문 하고 싶어요"  
query4 = "오늘 오전 13시 2분에 우라회 주문 하고 싶어요"      
query5 = "오늘 오전 13시 2분에 촐랭이밥 주문 하고 싶어요"
queries = [query, query1, query2, query3, query4, query5]
num = 1

for q in queries:

    print(f'{num}번째 쿼리문 \n')
    predict = ner.predict(q)
    tag = ner.predict_tags(q)
    print(predict)
    print(tag)
    print('\n')
    num+=1

