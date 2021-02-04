from dataclasses import dataclass

import MeCab
from .search_dto import (
    SearchRequest,
    MorphologicalSearchWords,
    MorphologicalBackDataWords,
)
from search.models import Knowledge
from typing import List

mecab = MeCab.Tagger("")
mecab.parse("")  # 文字列がGCされるのを防ぐ


@dataclass
class Const:
    EXTRACT_WORD_CLASS = ["名詞"]


@dataclass
class MorphologicalWords:
    def create(self, search_request: SearchRequest) -> MorphologicalSearchWords:
       
        search_word_list = []
        node = mecab.parseToNode(search_request.i_data)

        while node:
            # 単語を取得
            word = node.surface
            # 品詞を取得
            word_class = node.feature.split(",")[0]
            if word_class in Const.EXTRACT_WORD_CLASS:
                search_word_list.append(word)

            # 次の単語に進める
            node = node.next
        ret = MorphologicalSearchWords(search_word_list)
        return ret


@dataclass
class BackDataMorphologicalWords:
    """
    DBから受け取ったデータを形態素解析して、結果をオブジェクト化しリストに詰める。
    """

    def create(self, back_datas: List[Knowledge]) -> List[MorphologicalBackDataWords]:

        ret = []
        for bd in back_datas:
            back_word_list = []
            node = mecab.parseToNode(bd.search_word)

            while node:
                # 単語を取得
                word = node.surface
                # 品詞を取得
                word_class = node.feature.split(",")[0]
                if word_class in Const.EXTRACT_WORD_CLASS:
                    back_word_list.append(word)

                # 次の単語に進める
                node = node.next
            ret.append(
                MorphologicalBackDataWords(int(bd.id), [" ".join(back_word_list)])
            )
        return ret
