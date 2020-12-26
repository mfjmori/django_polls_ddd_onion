import inject
from typing import List
from django.db import transaction
from domain.repository.question import IQuestionRepository
from domain.repository.choice import IChoiceRepository
from domain.entity.question import QuestionEntity
from domain.entity.choice import ChoiceEntity
from uuid import uuid4, UUID


class QuestionApplicationService:
    """
    Questionエンティティを取り扱うためのアプリケーションサービス
    """

    @staticmethod
    @inject.autoparams("repository")
    def get(question_id: UUID, repository: IQuestionRepository = None) -> List[QuestionEntity]:
        return repository.get(question_id=question_id)

    @staticmethod
    @inject.autoparams("repository")
    def get_latest_list(limit_num: int = None, repository: IQuestionRepository = None) -> List[QuestionEntity]:
        return repository.get_latest_list(limit_num=limit_num)

    @staticmethod
    @inject.autoparams("question_repository", "choice_repository")
    def create_question_choice_set(
                                   question_data: dict,
                                   choice_data_list: List[dict],
                                   question_repository: IQuestionRepository,
                                   choice_repository: IChoiceRepository,
                                   ) -> None:
        question_entity = QuestionEntity(
            question_text=question_data["question_text"],
            pub_date=question_data["pub_date"]
            )
        choice_entity_list = []
        for choice_data in choice_data_list:
            choice_entity = ChoiceEntity(
                question_id=question_entity.id,
                choice_text=choice_data["choice_text"],
                votes=choice_data["votes"],
                id=uuid4()  # ChoiceEntity生成時のデフォルト値を使用すると全て同じuuidになってしまうので値をセット(バグ？)
            )
            choice_entity_list.append(choice_entity)

        with transaction.atomic():
            question_repository.save(question_entity)
            for choice_entity in choice_entity_list:
                choice_repository.save(choice_entity)


class ChoiceApplicationService:
    """
    Choiceエンティティを取り扱うためのアプリケーションサービス
    """

    @staticmethod
    @inject.autoparams("repository")
    def get_relate_list(question_id: UUID = None, repository: IChoiceRepository = None) -> List[ChoiceEntity]:
        return repository.get_relate_list(question_id=question_id)

    @staticmethod
    @inject.autoparams("repository")
    def add_vote(choice_id: UUID, repository: IChoiceRepository = None) -> List[ChoiceEntity]:
        return repository.add_vote(choice_id=choice_id)
