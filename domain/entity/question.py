from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid4
import dataclasses

JST = timezone(timedelta(hours=+9), 'JST')


@dataclasses.dataclass(frozen=True)
class QuestionEntity:
    """Questionのエンティティ"""
    question_text: str
    pub_date: datetime
    id: UUID = uuid4()

    def __post_init__(self):

        if not isinstance(self.id, UUID):
            raise ValueError("idがuuid型ではありません")

        if not isinstance(self.question_text, str):
            raise ValueError("question_textがstr型ではありません")

        if not isinstance(self.pub_date, datetime):
            raise ValueError("pub_dateがdatetime型ではありません")

        if self.pub_date >= datetime.now(JST):
            raise ValueError("pub_dateが未来日は無効です")
