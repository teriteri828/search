from django.http import HttpResponse
from django.shortcuts import render

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

#word2vecモデルを読み込み
word2vec_model = KeyedVectors.load_word2vec_format(
        Word2VecConst.MODEL_PATH, binary=True
    )

#単語頻度ベクトルモデルを読み込み
counter_vector_model = pickle.load(open(CounterVectorConst.MODEL_PATH, "rb"))

def index(request):
    return render(request, "search/index.html")


def search(request):
    # sentence
    input_data = SearchRequest(request.POST["search"])

    # SearchVectorCreateService
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
    bdsrs = BackDataSimilarRankService(VectorSimilarRank(), BackDataSimilarSort(), sr)

    search_servuce_applacation = SearchSeviceApplication(
        input_data, svcs, sr, bdvc, bdsrs
    )
    search_result = search_servuce_applacation.execute()
    response = {"search_result": search_result}

    return render(request, "search/index.html", response)
