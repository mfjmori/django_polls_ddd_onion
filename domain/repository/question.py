from uuid import UUID
from typing import List
from abc import ABC, abstractmethod
from domain.entity.question import QuestionEntity


class IQuestionRepository(ABC):
    """
    QuestionEntityのリポジトリ
    """

    @abstractmethod
    def get(self, question_id: UUID) -> QuestionEntity:
        """
        question_idをもとにオブジェクトを取得する
        """
        raise NotImplementedError

    @abstractmethod
    def get_latest_list(self, limit_num: int = None) -> List[QuestionEntity]:
        """
        pub_dateの最新順に<limit_num>件取得する
        """
        raise NotImplementedError

    @abstractmethod
    def save(self, question_entity: QuestionEntity) -> None:
        """QuestionEntityを永続化する"""
        raise NotImplementedError
