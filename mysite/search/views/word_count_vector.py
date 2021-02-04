from dataclasses import dataclass
from .search_dto import (
    SearchCountVectorEntity,
    SearchSynonymsWords,
    MorphologicalBackDataWords,
    BackDataCountVectorEntity,
)
import pickle
import os, sys
from sklearn.feature_extraction.text import CountVectorizer
from typing import List


@dataclass
class CounterVectorConst:
    MODEL_PATH = (
        os.path.dirname(os.path.abspath("__file__"))
        + "/search/static/ai_model/count_vector/stab.model"
    )


@dataclass
class SearchWordCountVector:
    counter_vector_model: CountVectorizer

    def create(
        self, search_sysnonyms_words: SearchSynonymsWords
    ) -> SearchCountVectorEntity:
        count_vector = self.counter_vector_model.transform(
            search_sysnonyms_words.words
        ).toarray()
        ret = SearchCountVectorEntity(count_vector[0])
        return ret


@dataclass
class BackDataWordCountVector:
    """
    DBの中のデータの単語頻度ベクトルをオブジェクト化し、リストに詰め込む。
    オブジェクト化は、DBのidと紐づけるidも含める。
    """

    counter_vector_model: CountVectorizer

    def create(
        self, morphological_backdata_words: List[MorphologicalBackDataWords]
    ) -> List[BackDataCountVectorEntity]:
        ret = []
        for mbw in morphological_backdata_words:
            count_vector = self.counter_vector_model.transform(mbw.words).toarray()
            ret.append(BackDataCountVectorEntity(int(mbw.data_id), count_vector[0]))
        return ret
