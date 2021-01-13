# Cassava Leaf Disease Classification

## Description

キャッサバの葉の病気を特定する。

データセットにはウガンダで入手したラベル付きの画像を用いる

## Evaluation

評価は分類の正確性でおこなう

### Submission Format

次のようなcsvファイルで行う

```
image_id,label
1000471002.jpg,4
1000840542.jpg,4
etc.
```

# Data

## Files

### train.csv

- image_id 画像ファイルの名前

- label　どの病気かを表すラベル

### sample_submission.csv

提出フォーマットのサンプル

- image_id　同上
- label 同上

# Discussion

|題名（URL）|内容|
|:--:|:--:|
|[Sharing some improvements and experiments](https://www.kaggle.com/c/cassava-leaf-disease-classification/discussion/203594)|金メダル圏内の人の精度を上げるためのヒントみたいなの|
|[[place holder] let's try something new ... vision transformer](https://www.kaggle.com/c/cassava-leaf-disease-classification/discussion/199276)|vision Transformerの話と思ったら、いろいろなモデルについて語ってある|
|[Research Papers related to this competition](https://www.kaggle.com/c/cassava-leaf-disease-classification/discussion/198146)| このコンペに関する論文のまとめ　|
|[Important points to boost the LB score](https://www.kaggle.com/c/cassava-leaf-disease-classification/discussion/208402)|LBを爆上げする方法みたいなの|

# Notebooks


|題名（URL）|内容|
|:--:|:--:|
|[Vision Transformer (ViT): Tutorial + Baseline](https://www.kaggle.com/abhinand05/vision-transformer-vit-tutorial-baseline)| Vision Transfomerのチュートリアル|
|[Vision Transformer (ViT): CUDA as usual](https://www.kaggle.com/szuzhangzhi/vision-transformer-vit-cuda-as-usual/data)| Vision Transformerのpythonライブラリを使って学習させるサンプル。自作らしい。|

# Logs

## 2020/11/23

画像処理について無知すぎるので、pytorchのチュートリアルをやる

## 2020/12/19

モデルはCNNを使うことにした

画像のサイズを調整したほうがスコアがよくなった。

回転や左右反転などの前処理を加えてから学習してsubmitしてみる

画像をランダムに黒くすると精度がよくなるらしい。

次は自作のtransformを作って画像の一部を黒くする処理を追加したい。

## 2020/12/21

モデルを変えてみようかなとか思ったり

画像の前処理（回転と、左右反転）を追加しても、改善が見られなかった

一番精度が良かったものと層を同じにして学習させてみる

参考にしたEDAを使って一通り可視化してみる

transformsに一部を黒く塗りつぶす処理を追加して様子を見てみる

## 2020/12/28

卒研を終わらせたので再開する

使用モデルをCNNからViTに変更した。

ViTは事前学習モデルを使って転移学習させてsubmitしてみる

画像のEDAをしてみる。どのようなフィルターを通すといい感じに病気の検知ができるかを調べたい

## 2020/12/29

モデルが３しか予測しない問題に直面した。モデルをViTに変更していろいろ試してみようと思う

## 2021/01/05

スコアに改善が見られない

サンプル通りの前処理をして改善するか試してみようと思う

今は画像の読み込みにPILを使っているけどOpenCVを使うように変更する

## 2021/01/10

なんか、baselineで画像サイズを変えたら良さそうな結果が出そう。

うれしい。

おそらく、色のフィルタは意味があまりないと思うので画像処理の精度向上手法を勉強していく必要があると思う。

## 2021/01/11

Efficient Netとのアンサンブルにしてみた。ダメそうだった。

正解率に改善が見られなかったので、前処理を色々つくっていこうと思う

## 2021/01/12

KFoldを使ってデータを分割して学習させる（discussionに精度が改善したとあったので）

モデルのアンサンブルは有効みたい

2つのモデルをカーネル上で訓練するのは無謀なので1つはローカルで訓練して重みをアップロードする方向で行きたい