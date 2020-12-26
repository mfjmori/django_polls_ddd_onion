from uuid import UUID
from typing import List
from domain.repository.choice import IChoiceRepository
from domain.entity.choice import ChoiceEntity
from polls.models import Choice as ChoiceModel


class ChoiceRepository(IChoiceRepository):
    """
    ChoiceEntityのリポジトリの実態
    DjangoのORMマッパーをラップする
    """

    def get_relate_list(self, question_id: UUID = None) -> List[ChoiceEntity]:
        """
        親のquestion_idに紐づくオブジェクトを取得する
        """
        choice_models = ChoiceModel.objects.filter(question=question_id)
        return list(map(self.__to_choice_entity, choice_models))

    def add_vote(self, choice_id: UUID) -> None:
        """
        choice_idのオブジェクトのvoteに1を加算する
        """
        choice_model = ChoiceModel.objects.filter(id=choice_id).first()
        choice_model.votes += 1
        choice_model.save()

    def save(self, choice_entity: ChoiceEntity) -> None:
        """ChoiceEntityを永続化する"""
        ChoiceModel.objects.create(
            id=choice_entity.id,
            question_id=choice_entity.question_id,
            choice_text=choice_entity.choice_text,
            votes=choice_entity.votes
        )

    def __to_choice_entity(self, choice_model: ChoiceModel) -> ChoiceEntity:
        """
        ChoiceモデルをChoiceエンティティに変換する
        """
        return ChoiceEntity(
            id=choice_model.id,
            question_id=choice_model.question_id,
            choice_text=choice_model.choice_text,
            votes=choice_model.votes
        )
