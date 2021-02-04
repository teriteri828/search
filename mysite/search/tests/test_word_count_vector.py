from django.test import TestCase

from search.views.search_dto import (
    SearchSynonymsWords,
    SearchCountVectorEntity,
    BackDataCountVectorEntity,
    MorphologicalBackDataWords,
)
import numpy as np
from search.views.word_count_vector import (
    SearchWordCountVector,
    CounterVectorConst,
    BackDataWordCountVector,
)
import pickle


class TestSearchWordCountVector(TestCase):

    # テストクラスが初期化される際に一度だけ呼ばれる
    @classmethod
    def setUpClass(cls):
        pass

    # テストクラスが解放される際に一度だけ呼ばれる
    @classmethod
    def tearDownClass(cls):
        pass

    # テストメソッドを実行するたびに呼ばれる
    def setUp(self):
        pass

    # テストメソッドの実行が終わるたびに呼ばれる
    def tearDown(self):
        pass

    def test_検索単語を格納したリストから単語頻度オブジェクトを生成し返却する(self):
        counter_vector_model = pickle.load(open(CounterVectorConst.MODEL_PATH, "rb"))
        test_data = SearchSynonymsWords(["Apple computer of the apple mark"])
        target = SearchWordCountVector(counter_vector_model)
        del counter_vector_model
        actual = target.create(test_data)
        expect = SearchCountVectorEntity(np.array([0]))

        self.assertEqual(type(actual), type(expect))
        self.assertEqual(type(actual.vector), type(expect.vector))


class TestBackDataWordCountVector(TestCase):
    # テストクラスが初期化される際に一度だけ呼ばれる
    @classmethod
    def setUpClass(cls):
        pass

    # テストクラスが解放される際に一度だけ呼ばれる
    @classmethod
    def tearDownClass(cls):
        pass

    # テストメソッドを実行するたびに呼ばれる
    def setUp(self):
        pass

    # テストメソッドの実行が終わるたびに呼ばれる
    def tearDown(self):
        pass

    def test_検索単語を格納したリストから単語頻度オブジェクトを生成し返却する(self):
        counter_vector_model = pickle.load(open(CounterVectorConst.MODEL_PATH, "rb"))
        td1 = MorphologicalBackDataWords(100, ["私 人間"])
        td2 = MorphologicalBackDataWords(1, ["私 車 好き"])
        test_data = [td1, td2]

        target = BackDataWordCountVector(counter_vector_model)
        del counter_vector_model

        actual = target.create(test_data)
        expect = [
            BackDataCountVectorEntity(100, np.array([0])),
            BackDataCountVectorEntity(1, np.array([0])),
        ]
        for a, e in zip(actual, expect):
            self.assertEqual(type(a), type(e))
            self.assertEqual(a.data_id, e.data_id)
            self.assertEqual(type(a.vector), type(e.vector))
