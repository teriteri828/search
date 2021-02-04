from dataclasses import dataclass
from search.models import Knowledge


@dataclass
class SearchRepository:
    """
    DBから検索リクエストデータと比較するデータを取得
    """

    knowledge: Knowledge

    def select_all(self) -> list:
        """
        DBの中にあるデータを全取得
        """
        ret = self.knowledge.objects.all()

        return ret
