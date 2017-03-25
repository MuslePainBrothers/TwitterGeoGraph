# TwitterGeoGraph
twitterを用いた位置情報Webアプリ 

# 概要
① 
twitterAPIを用いてユーザのツイートからユーザの位置を取得してwebアプリに(最終的にはスマホアプリ)の地図状にtwitterアカウントのアイコンマークを表示させるシステム 

② 
位置情報とその発言時のネガポジから、その場所(店)の良し悪しの情報も見れるようにする 

③ 
学生ごとに分類して生息地分布的なのを作成する 

# システム構成図
![image01.jpeg](https://raw.githubusercontent.com/MuslePainBrothers/TwitterGeoGraph/develop/screen_shot/image01.jpeg)

# 機能説明
twitterアカウントの説明画面からwebサイトに移動して、twitter連携をすることによって登録を完了する 
webサイトのマップは最初は何も表示していない 
ユーザが検索を行うことによってピンの数を更新する 

 - ユーザのtwitterIDから検索
 - 名前検索
 - 場所検索
 - 性別検索
 - 時間検索
 - 学生検索（難）

# マップ機能
マップに表示されるI'm atの情報を数字丸ピンで描画
![image02.jpeg](https://raw.githubusercontent.com/MuslePainBrothers/TwitterGeoGraph/develop/screen_shot/image02.jpeg)

ピンをクリックで詳細画面（場所、ユーザ）の表示
![image03.jpeg](https://raw.githubusercontent.com/MuslePainBrothers/TwitterGeoGraph/develop/screen_shot/image03.jpeg)
![image04.jpeg](https://raw.githubusercontent.com/MuslePainBrothers/TwitterGeoGraph/develop/screen_shot/image04.jpeg)

地図を拡大することによって周囲のピンの数を合成して表示
![image05.jpeg](https://raw.githubusercontent.com/MuslePainBrothers/TwitterGeoGraph/develop/screen_shot/image05.jpeg)

特定のユーザ1人を検索して表示
![image06.jpeg](https://raw.githubusercontent.com/MuslePainBrothers/TwitterGeoGraph/develop/screen_shot/image06.jpeg)

