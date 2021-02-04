from dataclasses import dataclass
from typing import List
from .search_dto import VectorSimilarEntity, SeekDataEntity, SeekDatas
from search.models import Knowledge


@dataclass
class BackDataSimilarSort:
    """
    DBの中のデータを検索データとの類似度で降順にしたオブジェクトリスト生成する
    """

    def execute(
        self, knowledges: List[Knowledge], similar_ranks: List[VectorSimilarEntity]
    ) -> SeekDatas:
        """
         DBの中のデータを類似度とDBのidを内包するオブジェクトリストを基に類似度の降順にする
        """
        order = self.__order_create(similar_ranks)

        sorted_rank_knowledges = sorted(
            knowledges, key=lambda data: order.index(data.id)
        )
        seek_datas = []
        for sr, srk in zip(similar_ranks, sorted_rank_knowledges):
            seek_data_entity = SeekDataEntity(
                srk.id,
                srk.title,
                srk.category,
                srk.sub_category,
                srk.search_word,
                srk.article,
                sr.similar,
            )
            seek_datas.append(seek_data_entity)
        ret = SeekDatas(seek_datas)
        return ret

    def __order_create(self, similar_ranks: List[VectorSimilarEntity]) -> list:
        """
        類似度の降順となったDBのIDのリストを生成
        """
        ret = []
        for sr in similar_ranks:
            ret.append(sr.data_id)
        return ret
