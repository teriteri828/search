from dataclasses import dataclass
from typing import List
from gensim.models import KeyedVectors
import os, sys
from .search_dto import MorphologicalSearchWords, SearchSynonymsWords


class Word2VecConst:
    MODEL_PATH = (
        os.path.dirname(os.path.abspath("__file__"))
        + "/search/static/ai_model/entity_vector/stanby-jobs-200d-word2vector.bin"
    )
    TOPN = 20


@dataclass
class SearchWords:
    """
    return: "金 銀行 金融"みたいな感じのstr型変数を内包するオブジェクト
    """

    word2vec_model: KeyedVectors

    def create(
        self, morphological_search_words: MorphologicalSearchWords
    ) -> SearchSynonymsWords:
        synonyms_words = []
        for word in morphological_search_words.words:
            synonyms_words.extend(self.__most_similar_word_get(word))
        ret = SearchSynonymsWords([" ".join(synonyms_words)])
        print(ret)
        return ret

    def __most_similar_word_get(self, word: str) -> List[str]:
        """
        return: ["金", "銀行", "金融", ・・・]みたいな感じのリスト
        """
        synonyms_word_list = [word]
        try:
            word_similar_tuples = self.word2vec_model.most_similar(
                word, topn=Word2VecConst.TOPN
            )
        except KeyError:
            word_similar_tuples = [[word]]

        for wst in word_similar_tuples:
            synonyms_word_list.append(wst[0])
        return synonyms_word_list
