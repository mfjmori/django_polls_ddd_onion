from inject import Binder
from tests.test_setting.repository.question import TestQuestionRepository
from domain.repository.question import IQuestionRepository


def test_config(binder: Binder):
    """
    DI設定
    抽象クラスに対応する実態クラスを設定
    """
    binder.bind(IQuestionRepository, TestQuestionRepository())
