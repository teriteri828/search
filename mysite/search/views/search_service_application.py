from dataclasses import dataclass

from search.views.search_vector_create_service import SearchVectorCreateService
from search.views.backdata_vector_create_service import BackDataVectorCreateService
from search.views.back_data_similar_rank_service import BackDataSimilarRankService
from search.views.search_dto import SeekDatas, SearchRequest
from search.views.search_repository import SearchRepository


@dataclass
class SearchSeviceApplication:
    """
    検索クエリから、類似度の降順にしたバッグデータを返す
    """

    sentence: SearchRequest
    search_vector_create_service: SearchVectorCreateService
    search_repository: SearchRepository
    backdata_vector_create_service: BackDataVectorCreateService
    back_data_similar_rank_service: BackDataSimilarRankService

    def execute(self,) -> SeekDatas:
        svcs = self.search_vector_create_service.execute(self.sentence)
        sr = self.search_repository.select_all()
        bvcs = self.backdata_vector_create_service.execute(sr)
        bdsrs = self.back_data_similar_rank_service.execute(svcs, bvcs)

        return bdsrs
