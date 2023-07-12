from config.DatabaseConfig import *
from utils.Database import Database
from utils.Preprocess import Preprocess_1

p_ner = Preprocess_1(word2index_dic='project/chatbot/train_tools/dict/chatbot_dict.bin',
                 userdic='project/chatbot/utils/user_dic.tsv')

p_intent = Preprocess_1(word2index_dic='project/chatbot/train_tools/dict/chatbot_dict.bin')

db = Database(
    host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME
)
db.connect()

query = "오늘 오전 13시 2분에 탕수육 주문 하고 싶어요"

from models.intent.IntentModel import IntentModel
intent = IntentModel(model_name='project/chatbot/models/intent/intent_model.h5', 
                     proprocess=p_intent)
predict = intent.predict_class(query)
intent_name = intent.labels[predict]

from models.ner.NerModel import NerModel
ner = NerModel(model_name='project/chatbot/models/ner/ner_model_with_userdic.h5',
               preprocess=p_ner)
predicts = ner.predict(query)
ner_tags = ner.predict_tags(query)

print("질문 : ", query)
print("=" * 40)
print("의도 파악 : ", intent_name)
print("개체명 의식 : ", predicts)
print("답변 검색에 필요한 NER 태그 : ", ner_tags)
print("=" * 40)

from utils.Findanswer import FindAnswer

try:
    f = FindAnswer(db)
    answer_text, answer_image = f.search(intent_name, ner_tags)
    answer = f.tag_to_word(predicts, answer_text)

except:
    answer = "죄송해요 무슨 말인지 모르겠어요."

print("답변 : ", answer)

db.close()