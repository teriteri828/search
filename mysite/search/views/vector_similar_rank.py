from dataclasses import dataclass
from typing import List
from .search_dto import (
    VectorSimilarEntity,
    SearchCountVectorEntity,
    BackDataCountVectorEntity,
)
import numpy as np


@dataclass
class VectorSimilarRank:
    """
    リクエストのデータとDBのデータのそれぞれの単語頻度ベクトルを比較し、
    DBと紐づけるキー、類似度を内包するオブジェクトリストを生成。
    生成されるオブジェクトリストは、類似度の降順になる。
    """

    def execute(
        self,
        search_count_vector_entity: SearchCountVectorEntity,
        back_data_count_vector_entitys: List[BackDataCountVectorEntity],
    ) -> List[VectorSimilarEntity]:
        vector_similars = []
        sv = search_count_vector_entity

        for bv in back_data_count_vector_entitys:
            similar = self.__calc_cos_sim(sv.vector, bv.vector)
            vector_similars.append(VectorSimilarEntity(bv.data_id, similar))

        ret = sorted(vector_similars, key=lambda vs: vs.similar, reverse=True)
        return ret

    def __calc_cos_sim(
        self, search_vector: np.ndarray, back_data_vector: np.ndarray
    ) -> np.float64:
        if np.all(search_vector == 0) or np.all(back_data_vector == 0):
            return np.float64(0)

        cos_similar = np.dot(search_vector, back_data_vector) / (
            np.linalg.norm(search_vector) * np.linalg.norm(back_data_vector)
        )
        return cos_similar
