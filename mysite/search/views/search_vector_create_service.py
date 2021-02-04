from search.views.word_count_vector import SearchWordCountVector
from dataclasses import dataclass
from search.views.morphological_wrods import MorphologicalWords
from search.views.search_words_creater import SearchWords
from search.views.search_dto import SearchCountVectorEntity, SearchRequest


@dataclass
class SearchVectorCreateService:
    morphological_wrods: MorphologicalWords
    search_words: SearchWords
    search_word_count_vector: SearchWordCountVector

    def execute(self, sentence: SearchRequest) -> SearchCountVectorEntity:
        mw = self.morphological_wrods.create(sentence)
        sw = self.search_words.create(mw)
        swcv = self.search_word_count_vector.create(sw)
        return swcv
