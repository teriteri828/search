from django.test import TestCase
from unittest import skip
from gensim.models import KeyedVectors
import pickle
import numpy as np
from search.views.backdata_vector_create_service import BackDataVectorCreateService
from search.views.morphological_wrods import BackDataMorphologicalWords
from search.views.word_count_vector import BackDataWordCountVector, CounterVectorConst
from search.models import Knowledge
from search.views.search_dto import BackDataCountVectorEntity


class TestBackDataVectorCreateService(TestCase):
    # @skip("TESTSKIP")
    def test_文章を単語頻度ベクトルに変換する(self):
        td1 = Knowledge(
            id=100,
            title="私は人間です",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="私は人間です",
            article="test_アーティクル",
        )
        td2 = Knowledge(
            id=1,
            title="私は車が好きです",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="私は車が好きです",
            article="test_アーティクル2",
        )
        test_data = [td1, td2]

        counter_vector_model = pickle.load(open(CounterVectorConst.MODEL_PATH, "rb"))

        target = BackDataVectorCreateService(
            BackDataMorphologicalWords(), BackDataWordCountVector(counter_vector_model),
        )
        actual = target.execute(test_data)

        expect = [
            BackDataCountVectorEntity(100, np.array([0])),
            BackDataCountVectorEntity(1, np.array([0])),
        ]
        for a, e in zip(actual, expect):
            self.assertEqual(type(a), type(e))
            self.assertEqual(a.data_id, e.data_id)
            self.assertEqual(type(a.vector), type(e.vector))
