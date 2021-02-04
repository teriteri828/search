from django.test import TestCase
from search.views.vector_similar_rank import VectorSimilarRank
from search.views.search_dto import (
    BackDataCountVectorEntity,
    SearchCountVectorEntity,
    VectorSimilarEntity,
)
import numpy as np


class TestVectorSimilarRank(TestCase):
    def test_検索クエリとバックにあるデータのベクトル類似度を計算し類似度降順のオブジェクトリストを作成する(self):
        sv = SearchCountVectorEntity(np.array([1.0, 1.0]))

        bv1 = BackDataCountVectorEntity(1, np.array([1.0, 1.0]))
        bv2 = BackDataCountVectorEntity(2, np.array([1.0, 0.9]))
        bv3 = BackDataCountVectorEntity(3, np.array([1.0, 0.8]))
        bv = [bv1, bv2, bv3]

        target = VectorSimilarRank()
        actual = target.execute(sv, bv)

        ex1 = VectorSimilarEntity(data_id=1, similar=0.9999999999999998)
        ex2 = VectorSimilarEntity(data_id=2, similar=0.9986178293325095)
        ex3 = VectorSimilarEntity(data_id=3, similar=0.9938837346736189)
        expect = [ex1, ex2, ex3]
        self.assertEqual(actual, expect)

    def test_検索クエリのベクトルが０ベクトルの場合は全てオブジェクトが類似度０になる(self):
        sv = SearchCountVectorEntity(np.array([0.0, 0.0]))

        bv1 = BackDataCountVectorEntity(1, np.array([1.0, 1.0]))
        bv2 = BackDataCountVectorEntity(2, np.array([1.0, 0.9]))
        bv3 = BackDataCountVectorEntity(3, np.array([1.0, 0.8]))
        bv = [bv1, bv2, bv3]

        target = VectorSimilarRank()
        actual = target.execute(sv, bv)

        ex1 = VectorSimilarEntity(data_id=1, similar=0.0)
        ex2 = VectorSimilarEntity(data_id=2, similar=0.0)
        ex3 = VectorSimilarEntity(data_id=3, similar=0.0)
        expect = [ex1, ex2, ex3]
        self.assertEqual(actual, expect)

    def test_バックデータのベクトルが０ベクトルの場合はその類似度オブジェクトの類似度は０になる(self):
        sv = SearchCountVectorEntity(np.array([1.0, 1.0]))

        bv1 = BackDataCountVectorEntity(1, np.array([0.0, 0.0]))
        bv2 = BackDataCountVectorEntity(2, np.array([1.0, 0.9]))
        bv3 = BackDataCountVectorEntity(3, np.array([1.0, 0.8]))
        bv = [bv1, bv2, bv3]

        target = VectorSimilarRank()
        actual = target.execute(sv, bv)

        ex1 = VectorSimilarEntity(data_id=2, similar=0.9986178293325095)
        ex2 = VectorSimilarEntity(data_id=3, similar=0.9938837346736189)
        ex3 = VectorSimilarEntity(data_id=1, similar=0.0)
        expect = [ex1, ex2, ex3]
        self.assertEqual(actual, expect)
