from utils.Preprocess import Preprocess_1
from models.intent.IntentModel import IntentModel

p = Preprocess_1(word2index_dic='project/chatbot/train_tools/dict/chatbot_dict.bin')

intent = IntentModel(model_name = 'project/chatbot/models/intent/intent_model.h5', proprocess=p)

query = "오늘 탕수육 주문 가능할까요?"
query = "탕수육 10개 오전주문이요."
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(query)
print("의도 예측 클래스 : ", predict)
print("의도 예측 클래스 : ", predict_label)