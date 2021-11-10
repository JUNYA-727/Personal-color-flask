# Description
自分で作ったパーソナルカラー診断のプログラム(https://github.com/JUNYA-727/Personal-color-diagnostics)
を用いてweb上で使用できるようにした｡


<img width="957" alt="スクリーンショット 2021-11-11 0 09 15" src="https://user-images.githubusercontent.com/61785070/141138811-168975ca-c7d8-4509-a7a1-cde52ad16d68.png">

# Requirement
 開発に使用したライブラリなど
 
* tensorflow 2.5.0
* opencv 4.5.2.52
* dlib 19.22.1
* imutils 0.5.4
* flask 2.0.1
* dlib 19.22.1


# Features
ファイル選択のボタンを押すと画像を選択する事ができるので､選択したあとに送信ボタンを押すと画面が切り替わり､春夏秋冬の中でどれが一番パーソナルカラーに近いのかを提示してくれる｡また､それぞれの可能性を提示してくれる｡

# How to use
ファイルの中身は以下のようにしておく必要があります｡

<img width="720" alt="スクリーンショット 2021-11-11 0 15 18" src="https://user-images.githubusercontent.com/61785070/141139774-0ad43c1e-a9fe-4002-ba9f-53bb9bd3a09f.png">

* personal_color_model1.h5は学習済みのモデルで､容量が大きいため以下からダウンロードを行って下さい｡
https://drive.google.com/file/d/1ESLm0Ri3QNrz5isLr1jwXVvSvYaBpNmi/view?usp=sharing
* shape_predictor_68_face_landmarks.datは与えられた画像に対して特徴量となる顔だけを切り取る際に使用します｡こちらも使用する際は同様ダウンロードを行う必要があります｡
https://drive.google.com/file/d/1Ga4OTpjr3YPHyoWOanHiTRQa6Howy5Qn/view?usp=sharing
* 画像の保存を行うため､staticという空ファイルを作っておいて下さい｡
```bash
python server.py
```
サーバーが起動するのであとは､画像を与えるだけで完了です｡

# Installation
 
Requirementで列挙したライブラリなどのインストール方法
```bash
pip install tensorflow 
```
```bash
pip install opencv-python
```
```bash
brew install cmake
brew install boost-python
conda install -c menpo dlib=18.18
pip install dlib
```
```bash
pip install imutils
```
```bash
pip install Flask
```
# Note
MacOSで開発を行いました｡

# Author
* k.junya0727@gmail.com
* 具体的な詳細であったり､質問等ございましたらご気軽に連絡ください
