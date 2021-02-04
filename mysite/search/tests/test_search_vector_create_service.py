from django.test import TestCase
from unittest import skip

from ..views.search_dto import SearchRequest, SearchCountVectorEntity
from ..views.word_count_vector import SearchWordCountVector, CounterVectorConst
from ..views.morphological_wrods import MorphologicalWords
from ..views.search_words_creater import Word2VecConst, SearchWords
from ..views.search_vector_create_service import SearchVectorCreateService
from gensim.models import KeyedVectors
import pickle
import numpy as np


class TestSearchVectorCreateService(TestCase):
    # @skip("Don't want to test")
    def test_文章を単語頻度ベクトルに変換する(self):
        test_data = SearchRequest("私は人間です")
        word2vec_model = KeyedVectors.load_word2vec_format(
            Word2VecConst.MODEL_PATH, binary=True
        )
        counter_vector_model = pickle.load(open(CounterVectorConst.MODEL_PATH, "rb"))

        target = SearchVectorCreateService(
            MorphologicalWords(),
            SearchWords(word2vec_model),
            SearchWordCountVector(counter_vector_model),
        )
        actual = target.execute(test_data)
        expect = SearchCountVectorEntity(np.array([0]))

        self.assertEqual(type(actual), type(expect))
        self.assertEqual(type(actual.vector), type(expect.vector))
