from uuid import UUID, uuid4
import dataclasses


def create_uuid():
    return uuid4()


@dataclasses.dataclass(frozen=True)
class ChoiceEntity:
    """Choiceのエンティティ"""
    question_id: UUID
    choice_text: str
    votes: int
    id: UUID = uuid4()

    def __post_init__(self):

        if not isinstance(self.id, UUID):
            raise ValueError("idがuuid型ではありません")

        if not isinstance(self.question_id, UUID):
            raise ValueError("question_idがuuid型ではありません")

        if not isinstance(self.votes, int):
            raise ValueError("votesがint型ではありません")

        if self.votes < 0:
            raise ValueError("votesは0または正の整数のみ有効です")
