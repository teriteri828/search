# search

## 概要

* 分散表現を応用した汎化的な単語ベース検索システム
* 入力された検索ワードに対して、分散表現モデル（word2vec等）を基に、検索ワードの類似語も一緒に、検索することで、検索性能を向上させる。

## 目的

* ある論文（どれか忘れました。。すみません。。。）によると、検索精度が高くなるとのことだったので、それを確認するため。
* 以下、補足。
  * 論文では、検索システムA,検索システムBを複数人に使ってもらい、アンケート形式で比較、評価したものである（だった気がする）。
* レイヤードアーキテクチャで構成にし、オブジェクト指向の理解を深めるため
* テスト駆動開発を経験し、開発力を向上させるため
* docstringの重要性を理解するため。

## 検索処理のイメージ

* 以下の流れで検索処理する
  * 検索ワード入力："犬"
  * 検索ワード増加：["犬", "dog", "わんわん", "ワンちゃん"]
  * OR検索:["犬", "dog", "わんわん", "ワンちゃん"]
  * 検索結果:OR検索で部分一致したデータ

## 備考

* レイヤードアーキテクチャで構成
* テスト駆動開発で開発
* docstringはgoogle style