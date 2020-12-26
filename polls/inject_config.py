from inject import Binder
from polls.repository.question import QuestionRepository
from polls.repository.choice import ChoiceRepository
from domain.repository.question import IQuestionRepository
from domain.repository.choice import IChoiceRepository


def default_config(binder: Binder):
    """
    DI設定
    抽象クラスに対応する実態クラスを設定
    """
    binder.bind(IQuestionRepository, QuestionRepository())
    binder.bind(IChoiceRepository, ChoiceRepository())
