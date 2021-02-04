from dataclasses import dataclass
from search.views.vector_similar_rank import VectorSimilarRank
from search.views.back_data_similar_sort import BackDataSimilarSort
from search.views.search_repository import SearchRepository
from search.views.search_dto import (
    SearchCountVectorEntity,
    BackDataCountVectorEntity,
    SeekDatas,
)
from typing import List


@dataclass
class BackDataSimilarRankService:
    """
    検索クエリとバックデータのベクトルを基に類似度を計算し、バックデータを類似度の降順にし、返却するクラス
    """

    vector_similar_rank: VectorSimilarRank
    back_data_similar_sort: BackDataSimilarSort
    search_repository: SearchRepository

    def execute(
        self,
        search_count_vector_entity: SearchCountVectorEntity,
        back_data_count_vector_entitys: List[BackDataCountVectorEntity],
    ) -> SeekDatas:

        sr = self.search_repository.select_all()
        vsr = self.vector_similar_rank.execute(
            search_count_vector_entity, back_data_count_vector_entitys
        )
        bdsse = self.back_data_similar_sort.execute(sr, vsr)

        return bdsse
