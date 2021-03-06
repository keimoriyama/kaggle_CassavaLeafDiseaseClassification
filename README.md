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

|                                                                   題名（URL）                                                                   |                                 内容                                 |
| :---------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------: |
|           [Sharing some improvements and experiments](https://www.kaggle.com/c/cassava-leaf-disease-classification/discussion/203594)           |         金メダル圏内の人の精度を上げるためのヒントみたいなの         |
| [[place holder] let's try something new ... vision transformer](https://www.kaggle.com/c/cassava-leaf-disease-classification/discussion/199276) | vision Transformerの話と思ったら、いろいろなモデルについて語ってある |
|          [Research Papers related to this competition](https://www.kaggle.com/c/cassava-leaf-disease-classification/discussion/198146)          |                    このコンペに関する論文のまとめ                    |
|            [Important points to boost the LB score](https://www.kaggle.com/c/cassava-leaf-disease-classification/discussion/208402)             |                     LBを爆上げする方法みたいなの                     |
|    [if you are not getting lb 0.901 and above, here is why](https://www.kaggle.com/c/cassava-leaf-disease-classification/discussion/202017)     |                             これから読む                             |

# Notebooks


|                                                             題名（URL）                                                             |                                     内容                                     |
| :---------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------: |
|     [Vision Transformer (ViT): Tutorial + Baseline](https://www.kaggle.com/abhinand05/vision-transformer-vit-tutorial-baseline)     |                      Vision Transfomerのチュートリアル                       |
|       [Vision Transformer (ViT): CUDA as usual](https://www.kaggle.com/szuzhangzhi/vision-transformer-vit-cuda-as-usual/data)       | Vision Transformerのpythonライブラリを使って学習させるサンプル。自作らしい。 |
| [Ensemble: Resnext50_32x4d + Efficientnet = 0.903](https://www.kaggle.com/japandata509/ensemble-resnext50-32x4d-efficientnet-0-903) |                                  題名のまま                                  |

<details>

<summary>上位陣の解法</summary>

## 3rd solution

[3rd Place Solution](https://www.kaggle.com/c/cassava-leaf-disease-classification/discussion/221150)

### model

3つのvitモデルを使った

  - vit_A
    - image_size : 384
    - 5x TTA
  - vit_B
    - image_size : 448
    - 5x TTA
  - vit_C
    - image_size : 448
    - 5x TTA
    - Label Smoothing

### Augmentation

- Random sized crop
- Transpose
- H & V filp
- Shift scale rotate
- Normalize & ToTensor

### Scheduler

- Lambda LR

### Attentionについて（vit_B, vit_C）

モデルの画像の入力サイズは224＊224なので以下のフローで処理する

1. 画像を4分割する
2. 同じモデル（ViT)に画像を入力する
3. 出力を1つの行列の値にまとめる
4. Softmaxをかける
5. 重みをつけて列の和を計算
6. 5次元に写像

## 5th solution

[5th Place Solution Summary](https://www.kaggle.com/c/cassava-leaf-disease-classification/discussion/221249)

### model

vit_16, efNet_b4, Deitのアンサンブル

#### train

    - vit
      - img_size : 384
      - bi-templated logistic loss
    - efNet
      - img+size : 512
      - bi-templated logistic loss
    - Deit
      - img_size : 384
      - bi-templated logistic loss

### Augmentation

- Random crop
- transpose
- H & V flip
- hue
- random brightness
- normalize

### important things

1. ensemble はいいぞ
2. Cutmixは小さいモデルにおいて有効
3. ラベルのノイズ除去は有効
4. 2020年のものだけを使ったほうが良かった
5. bi-templated lossは有効だった

## 8th solution

[8th place solution](https://www.kaggle.com/c/cassava-leaf-disease-classification/discussion/220994)

### data

2020年のものだけを使用した

### model

EfNet_B6，ResNetSt50，Vit_16

### Augmantation

- H & V flip
- transpose
- Hue, Coarse
- RandomBright
- shift scale
- RGB_shift
- Cutmix, Fmix, snapmix

CutmixとFmixを使ってCVをブーストし，Snapmixで安定化させた

### Loss

label smoothing

### message

諦めなければなんとかなる

</details>

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

## 2021/01/15

アンサンブルした。ViTよりもEfficient Netのほうが精度が良かった。

fine-tuningするような構成になったので、前処理を追加して見ようかな。

画像のバランスを変えてある程度差が無いようにしたい。

Efficient netのPublic Scoreが良くない。学習時のAccが良いのになんでだろう。

画像サイズを変えて試してみる。（ViTをやめる）

## 2021/01/18

resNetとEfficient Netのアンサンブルに変更した。

highスコアが出た（0.887)

しばらくdiscussionを読もうと思う

## 2021/01/25

データの偏りをなくすようなノイズ付画像を作った

画像は粗めにしたので精度が出なかったら高解像度にしようと思う

## 2021/02/09

↑のやつはむだでした．

Pseudo　Labelingをためしてみたいけど，lossのとり方がいまいちわからないのどどうしていいかわからない．

MSELossっていうやつを使えばよい？

[How to implement pseudo-labeling?](https://discuss.pytorch.org/t/how-to-implement-pseudo-labeling/68557)←これを参考にする

## 2021/02/13

pseudo labelingは事前学習したモデルを使ってやってみる．現状うまくいってないけど

LBを更新した．

学習データの不足分を，2019年のデータで補って学習させる

## 2021/02/14

efNet_b4に変えて画像の大きさを348に変更して様子を見る（計算量を節約したい）

# コンペ終了

- 順位 1795/3900

使ったモデルはef-Net-b4+ResNet50のアンサンブル．学習データには，今回のデータと2019年度のデータで不均衡分を補った

# 感想

初めてのコンペだった．画像分類だったからなめてかかってたけど，実際に精度を出すのは難しかった．画像処理って難しいんだなと

スコアが上がった時が嬉しかった．今回は論文を読んでいないので使ったモデルの論文は最低限読んで起きたい