from django.test import TestCase
from unittest import skip
from ..views.search_dto import SearchSynonymsWords, MorphologicalSearchWords
from ..views.search_words_creater import Word2VecConst, SearchWords
from gensim.models import KeyedVectors


class TestSearchWordsCreater(TestCase):

    # テストクラスが初期化される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def setUpClass(cls):
        pass

    # テストクラスが解放される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def tearDownClass(cls):
        pass

    # テストメソッドを実行するたびに呼ばれる
    def setUp(self):
        pass

    # テストメソッドの実行が終わるたびに呼ばれる
    def tearDown(self):
        pass

    # @skip("Don't want to test")
    def test_単語データリストを内包したオブジェクトを基に類義語を含む検索単語データリストを内包するオブジェクトを生成する(self):
        word2vec_model = KeyedVectors.load_word2vec_format(
            Word2VecConst.MODEL_PATH, binary=True
        )
        test_data = MorphologicalSearchWords(["私", "人間", "車"])
        target = SearchWords(word2vec_model)
        del word2vec_model
        actual = target.create(test_data)
        expect = SearchSynonymsWords(["金融 銀行"])
        self.assertEqual(type(actual), type(expect))
        self.assertEqual(type(actual.words), type(expect.words))

    def test_word2vecに存在しない単語の場合その単語を二つにして返す(self):
        word2vec_model = KeyedVectors.load_word2vec_format(
            Word2VecConst.MODEL_PATH, binary=True
        )
        test_data = MorphologicalSearchWords(["mikan"])
        target = SearchWords(word2vec_model)
        del word2vec_model
        actual = target.create(test_data)
        expect = SearchSynonymsWords(["mikan mikan"])
        self.assertEqual(actual, expect)