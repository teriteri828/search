from dataclasses import dataclass
from typing import List
import numpy as np


@dataclass(eq=True, frozen=True)
class SearchRequest:
    i_data: str


@dataclass(eq=True, frozen=True)
class MorphologicalSearchWords:
    """
    parameters
        words: List[str] 
    exaple
        words: ["私", "人間", "車"]
    """

    words: List[str]


@dataclass(eq=True, frozen=True)
class MorphologicalBackDataWords:
    """
    parameters
        data_id: DBから取得したidと紐づけるキー
        words: 形態素解析した結果
    exaple
        data_id: 1
        words: ["私 人間 車"]
    """

    data_id: int
    words: List[str]


@dataclass(eq=True, frozen=True)
class SearchSynonymsWords:
    """
    parameters
        words: List[str] 
    exaple
        words: ["私 人間 車"]
    """

    words: List[str]


@dataclass(eq=True, frozen=True)
class SearchCountVectorEntity:
    vector: np.ndarray


@dataclass(eq=True, frozen=True)
class BackDataCountVectorEntity:
    """
    parameters
        data_id: DBから取得したidと紐づけるキー
        vector: DBに格納されたデータの単語頻度ベクトル
    exaple
        data_id: 1
        vector: [1.0, 1.1]
    """

    data_id: int
    vector: np.ndarray


@dataclass(eq=True, frozen=True)
class VectorSimilarEntity:
    """
    parameters
        data_id: DBから取得したidと紐づけるキー
        similar: 2つのベクトル類似度
    exaple
        data_id: 1
        vector: 1.0
    """

    data_id: int
    similar: np.float64


@dataclass(eq=True, frozen=True)
class SeekDataEntity:
    """
    parameters
        data_id: データID
        title: タイトル
        category: カテゴリ
        sub_category:サブカテゴリ 
        search_word:検索用データ
        article: 内容
        similar: 検索データとの類似度
    """

    data_id: int
    title: str
    category: str
    sub_category: str
    search_word: str
    article: str
    similar: np.float64


@dataclass(eq=True, frozen=True)
class SeekDatas:
    """
    parameters
        data: 検索結果。ユーザーが求めているデータ群
    """

    data: List[SeekDataEntity]
