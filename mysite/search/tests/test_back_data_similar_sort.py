from django.test import TestCase
from search.models import Knowledge
from search.views.search_dto import VectorSimilarEntity, SeekDataEntity, SeekDatas
from search.views.back_data_similar_sort import BackDataSimilarSort


class TestBackDataSimilarSort(TestCase):
    def test_DBのデータと類似度オブジェクトを基にDBのデータを類似度の降順にしたオブジェクトリストを返却する(self):
        k_td1 = Knowledge(
            id=1,
            title="私は人間です",
            category="test_カテゴリ1",
            sub_category="test_サブカテゴリ1",
            search_word="私は人間です",
            article="test_アーティクル1",
        )
        k_td2 = Knowledge(
            id=2,
            title="私は車が好きです",
            category="test_カテゴリ2",
            sub_category="test_サブカテゴリ2",
            search_word="私は車が好きです",
            article="test_アーティクル2",
        )
        k_td3 = Knowledge(
            id=3,
            title="私は猫が好きです",
            category="test_カテゴリ3",
            sub_category="test_サブカテゴリ3",
            search_word="私は猫が好きです",
            article="test_アーティクル3",
        )
        ves_td1 = VectorSimilarEntity(data_id=3, similar=1.0)
        ves_td2 = VectorSimilarEntity(data_id=1, similar=0.9)
        ves_td3 = VectorSimilarEntity(data_id=2, similar=0.8)

        k_test_data = [k_td1, k_td2, k_td3]
        ves_test_data = [ves_td1, ves_td2, ves_td3]

        target = BackDataSimilarSort()
        actual = target.execute(k_test_data, ves_test_data)

        ex1 = SeekDataEntity(
            data_id=3,
            title="私は猫が好きです",
            category="test_カテゴリ3",
            sub_category="test_サブカテゴリ3",
            search_word="私は猫が好きです",
            article="test_アーティクル3",
            similar=1.0,
        )
        ex2 = SeekDataEntity(
            data_id=1,
            title="私は人間です",
            category="test_カテゴリ1",
            sub_category="test_サブカテゴリ1",
            search_word="私は人間です",
            article="test_アーティクル1",
            similar=0.9,
        )
        ex3 = SeekDataEntity(
            data_id=2,
            title="私は車が好きです",
            category="test_カテゴリ2",
            sub_category="test_サブカテゴリ2",
            search_word="私は車が好きです",
            article="test_アーティクル2",
            similar=0.8,
        )
        expect = SeekDatas([ex1, ex2, ex3])

        self.assertEqual(actual, expect)
