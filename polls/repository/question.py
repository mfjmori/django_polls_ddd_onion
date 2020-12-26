from uuid import UUID
from typing import List
from domain.repository.question import IQuestionRepository
from domain.entity.question import QuestionEntity
from polls.models import Question as QuestionModel


class QuestionRepository(IQuestionRepository):
    """
    QuestionEntityのリポジトリの実態
    DjangoのORMマッパーをラップする
    """

    def get(self, question_id: UUID) -> QuestionEntity:
        """
        question_idをもとにオブジェクトを取得する
        """
        question_model = QuestionModel.objects.filter(id=question_id).first()
        return self.__to_question_entity(question_model)

    def get_latest_list(self, limit_num: int = None) -> List[QuestionEntity]:
        """
        pub_dateの最新順に<limit_num>件取得する
        """
        question_models = QuestionModel.objects.order_by('-pub_date')[:limit_num]
        return list(map(self.__to_question_entity, question_models))

    def save(self, question_entity: QuestionEntity) -> None:
        """QuestionEntityを永続化する"""
        QuestionModel.objects.create(
            id=question_entity.id,
            question_text=question_entity.question_text,
            pub_date=question_entity.pub_date
        )

    def __to_question_entity(self, question_model: QuestionModel) -> QuestionEntity:
        """
        QuestionモデルをQuestionエンティティに変換する
        """
        return QuestionEntity(
            id=question_model.id,
            question_text=question_model.question_text,
            pub_date=question_model.pub_date
        )
