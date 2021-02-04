from django.test import TestCase
from search.views.back_data_similar_rank_service import BackDataSimilarRankService
from search.views.search_dto import (
    SearchCountVectorEntity,
    BackDataCountVectorEntity,
    SeekDatas,
    SeekDataEntity,
)
from search.models import Knowledge
import numpy as np
from search.views.vector_similar_rank import VectorSimilarRank
from search.views.back_data_similar_sort import BackDataSimilarSort
from search.views.search_repository import SearchRepository


class TestBackDataSimilarRankService(TestCase):
    def test_検索クエリとバックデータのベクトルを基に類似度を計算しバックデータを類似度の降順にし返却する(self):
        td1 = Knowledge(
            id=1,
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
        td3 = Knowledge(
            id=3,
            title="私は猫が好きです",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="私は猫が好きです",
            article="test_アーティクル2",
        )
        td1.save()
        td2.save()
        td3.save()

        sv = SearchCountVectorEntity(np.array([1.0, 1.0]))

        bv1 = BackDataCountVectorEntity(1, np.array([1.0, 0.9]))
        bv2 = BackDataCountVectorEntity(2, np.array([1.0, 0.8]))
        bv3 = BackDataCountVectorEntity(3, np.array([1.0, 1.0]))
        bv = [bv1, bv2, bv3]

        target = BackDataSimilarRankService(
            VectorSimilarRank(), BackDataSimilarSort(), SearchRepository(Knowledge)
        )
        actual = target.execute(sv, bv)

        ex1 = SeekDataEntity(
            data_id=3,
            title="私は猫が好きです",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="私は猫が好きです",
            article="test_アーティクル2",
            similar=0.9999999999999998,
        )
        ex2 = SeekDataEntity(
            data_id=1,
            title="私は人間です",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="私は人間です",
            article="test_アーティクル",
            similar=0.9986178293325095,
        )
        ex3 = SeekDataEntity(
            data_id=2,
            title="私は車が好きです",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="私は車が好きです",
            article="test_アーティクル2",
            similar=0.9938837346736189,
        )

        expect = SeekDatas([ex1, ex2, ex3])
        self.assertEqual(actual, expect)
