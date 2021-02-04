from django.test import TestCase
from search.views.search_service_application import SearchSeviceApplication

from search.views.back_data_similar_rank_service import BackDataSimilarRankService
from search.views.back_data_similar_sort import BackDataSimilarSort
from search.views.backdata_vector_create_service import BackDataVectorCreateService
from search.views.morphological_wrods import (
    MorphologicalWords,
    BackDataMorphologicalWords,
)
from search.views.search_repository import SearchRepository
from search.views.search_vector_create_service import SearchVectorCreateService
from search.views.search_words_creater import Word2VecConst, SearchWords
from search.views.vector_similar_rank import VectorSimilarRank
from search.views.word_count_vector import (
    CounterVectorConst,
    SearchWordCountVector,
    BackDataWordCountVector,
)
from search.views.search_dto import SeekDataEntity, SeekDatas, SearchRequest
from search.models import Knowledge
from gensim.models import KeyedVectors
import pickle


class TestSearchSeviceApplication(TestCase):
    def test_検索クエリとバックデータのベクトルを基に類似度を計算しバックデータを類似度の降順にし返却する(self):
        td1 = Knowledge(
            id=1,
            title="車 車 車 好き 好き 好き 人間",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="車 車 車 好き 好き 好き 人間",
            article="test_アーティクル",
        )
        td2 = Knowledge(
            id=2,
            title="君は猫が好きです",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="君は猫が好きです",
            article="test_アーティクル2",
        )
        td3 = Knowledge(
            id=3,
            title="私は人間が好きです",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="私は人間が好きです",
            article="test_アーティクル2",
        )
        td1.save()
        td2.save()
        td3.save()

        # sentence
        input_data = SearchRequest("私は人間が好きです")

        # SearchVectorCreateService
        word2vec_model = KeyedVectors.load_word2vec_format(
            Word2VecConst.MODEL_PATH, binary=True
        )
        counter_vector_model = pickle.load(open(CounterVectorConst.MODEL_PATH, "rb"))

        svcs = SearchVectorCreateService(
            MorphologicalWords(),
            SearchWords(word2vec_model),
            SearchWordCountVector(counter_vector_model),
        )
        # SearchRepository
        sr = SearchRepository(Knowledge)

        # BackDataVectorCreateService
        bdvc = BackDataVectorCreateService(
            BackDataMorphologicalWords(), BackDataWordCountVector(counter_vector_model),
        )

        # BackDataSimilarRankService
        bdsrs = BackDataSimilarRankService(
            VectorSimilarRank(), BackDataSimilarSort(), sr
        )

        target = SearchSeviceApplication(input_data, svcs, sr, bdvc, bdsrs)
        actual = target.execute()
        """
        for a in actual.data:
            print(a.data_id)
            print(a.similar)
            print("$$$$$$$")
        """
        ex1 = SeekDataEntity(
            data_id=3,
            title="私は人間が好きです",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="私は人間が好きです",
            article="test_アーティクル2",
            similar=0.6324555320336759,
        )
        ex2 = SeekDataEntity(
            data_id=1,
            title="車 車 車 好き 好き 好き 人間",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="車 車 車 好き 好き 好き 人間",
            article="test_アーティクル",
            similar=0.5656854249492379,
        )
        ex3 = SeekDataEntity(
            data_id=2,
            title="君は猫が好きです",
            category="test_カテゴリ",
            sub_category="test_サブカテゴリ",
            search_word="君は猫が好きです",
            article="test_アーティクル2",
            similar=0.4472135954999579,
        )

        expect = SeekDatas([ex1, ex2, ex3])
        self.assertEqual(actual, expect)
