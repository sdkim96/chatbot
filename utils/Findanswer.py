class FindAnswer:
    def __init__(self, db):
        self.db= db


    def _make_query(self, intent_name, ner_tags):
        sql = "SELECT * FROM chatbot_train_data "
        if intent_name is not None and ner_tags is None:
            sql += f"WHERE intent = '{intent_name}' "

        elif intent_name is not None and ner_tags is not None:
            sql += f"WHERE intent = '{intent_name}' "
            if len(ner_tags) > 0:
                sql += "AND ("
                for ne in ner_tags:
                    sql += f"ner LIKE '%{ne}%' OR "
                sql = sql[:-3] + ") "

        sql += "ORDER BY RAND() LIMIT 1"
        return sql


    def search(self, intent_name, ner_tags):
        sql = self._make_query(intent_name, ner_tags)
        answer = self.db.select_one(sql)

        if answer is None:
            sql = self._make_query(intent_name, None)
            answer = self.db.select_one(sql)

        return (answer['answer'], answer['answer_image'])
    

    def tag_to_word(self, ner_predicts, answer):

        for word, tag in ner_predicts:

            if tag =='B_FOOD':
                answer = answer.replace(tag,word)

        answer = answer.replace('{', '')
        answer = answer.replace('}', '')

        return answer