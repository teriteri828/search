from search.views.word_count_vector import BackDataWordCountVector
from dataclasses import dataclass
from search.views.morphological_wrods import BackDataMorphologicalWords
from search.views.search_dto import SearchCountVectorEntity
from typing import List
from search.models import Knowledge


@dataclass
class BackDataVectorCreateService:
    morphological_wrods: BackDataMorphologicalWords
    back_data_word_count_vector: BackDataWordCountVector

    def execute(self, back_datas: List[Knowledge]) -> SearchCountVectorEntity:
        mw = self.morphological_wrods.create(back_datas)
        bdwcv = self.back_data_word_count_vector.create(mw)
        return bdwcv
