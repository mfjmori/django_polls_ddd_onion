import uuid
from typing import List
from datetime import datetime, timezone, timedelta
from domain.repository.question import IQuestionRepository
from domain.entity.question import QuestionEntity


class TestQuestionRepository(IQuestionRepository):
    """
    QuestionEntityのテスト用のリポジトリの実態
    辞書のリストに値の読み書きを行う
    """
    JST = timezone(timedelta(hours=+9), 'JST')

    def __init__(self):
        self.__storage = []
        self.__set_initial_data()

    def __set_initial_data(self):
        self.__storage.extend([
            {
                "id": uuid.UUID("00000000-0000-0000-0000-000000000000"),
                "question_text": "initial_data_1",
                "pub_date": datetime(2020, 1, 1, 0, 0, 0, tzinfo=self.JST)
            },
            {
                "id": uuid.UUID("00000000-0000-0000-0000-000000000001"),
                "question_text": "initial_data_2",
                "pub_date": datetime(2020, 1, 2, 0, 0, 0, tzinfo=self.JST)
            },
            {
                "id": uuid.UUID("00000000-0000-0000-0000-000000000002"),
                "question_text": "initial_data_3",
                "pub_date": datetime(2020, 1, 3, 0, 0, 0, tzinfo=self.JST)
            },
            {
                "id": uuid.UUID("00000000-0000-0000-0000-000000000003"),
                "question_text": "initial_data_4",
                "pub_date": datetime(2020, 1, 4, 0, 0, 0, tzinfo=self.JST)
            },
            {
                "id": uuid.UUID("00000000-0000-0000-0000-000000000004"),
                "question_text": "initial_data_5",
                "pub_date": datetime(2020, 1, 5, 0, 0, 0, tzinfo=self.JST)
            },
            {
                "id": uuid.UUID("00000000-0000-0000-0000-000000000005"),
                "question_text": "initial_data_6",
                "pub_date": datetime(2020, 1, 6, 0, 0, 0, tzinfo=self.JST)
            },
        ])

    def get_latest_list(self, limit_num: int = None) -> List[QuestionEntity]:
        """
        pub_dateの最新順に<limit_num>件取得する
        """
        sorted_list = sorted(self.__storage, key=lambda x: x["pub_date"], reverse=True)
        latest_list = sorted_list[:limit_num]
        return list(map(self.__to_question_entity, latest_list))

    def __to_question_entity(self, question_dict: dict) -> QuestionEntity:
        """
        辞書をQuestionエンティティに変換する
        """
        return QuestionEntity(
            id=question_dict["id"],
            question_text=question_dict["question_text"],
            pub_date=question_dict["pub_date"]
        )
