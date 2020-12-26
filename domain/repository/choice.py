from uuid import UUID
from typing import List
from abc import ABC, abstractmethod
from domain.entity.choice import ChoiceEntity


class IChoiceRepository(ABC):
    """
    ChoiceEntityのリポジトリ
    """

    @abstractmethod
    def get_relate_list(self, question_id: UUID) -> List[ChoiceEntity]:
        """
        親のquestion_idに紐づくオブジェクトを取得する
        """
        raise NotImplementedError

    @abstractmethod
    def add_vote(self, choice_id: UUID) -> None:
        """
        choice_idのオブジェクトのvoteに1を加算する
        """
        raise NotImplementedError

    @abstractmethod
    def save(self, choice_entity: ChoiceEntity) -> None:
        """ChoiceEntityを永続化する"""
        raise NotImplementedError
