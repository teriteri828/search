from django.test import TestCase
from django.db.models.query import QuerySet
from search.views.search_repository import SearchRepository
from search.models import Knowledge


class TestSearchRepository(TestCase):
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

    def test_ナレッジテーブルから全データを取得する(self):
        td1 = Knowledge(
            id=100,
            title="私は人間です",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="私は人間です",
            article="test_アーティクル",
        )
        td2 = Knowledge(
            id=2,
            title="私は車が好きです",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="私は車が好きです",
            article="test_アーティクル2",
        )
        td1.save()
        td2.save()
        target = SearchRepository(Knowledge)
        actual = target.select_all()

        ex1 = Knowledge(
            id=2,
            title="私は車が好きです",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="私は車が好きです",
            article="test_アーティクル2",
        )
        ex2 = Knowledge(
            id=100,
            title="私は人間です",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="私は人間です",
            article="test_アーティクル",
        )
        expect = [ex1, ex2]
        for a, e in zip(actual, expect):
            self.assertEqual(a.id, e.id)
            self.assertEqual(a.title, e.title)
            self.assertEqual(a.category, e.category)
            self.assertEqual(a.sub_category, e.sub_category)
            self.assertEqual(a.search_word, e.search_word)
            self.assertEqual(a.article, e.article)
