# smashmate_rankings_for_discord
## これは何？
DiscordのメンバーとメイトIDを紐づけることができるbotです。
次のような機能があります。
- ランキング表示機能

![image](https://user-images.githubusercontent.com/26502414/208263903-a9b3df28-a02a-4897-b468-c75caa86597e.png)

## 使用可能なコマンド

- /smashmate {MATE ID※}

  自分のDiscordアカウントにメイトIDを紐づけます。このとき自動的に最高レートを取得します。
- /reload

  自分の最高レートを更新します。
- /delete

  自分のアカウントの紐づけを解除し、最高レートを含めて紐づけを抹消します。
- /rank

  ランキングを表示します。
 
 ※MATE IDはスマメイトのサイトのユーザー情報から確認できます。
 
## このbotを使うには？
### このbotを使うには次のものが必要です。
- Python
- Discord bot token
- Discordサーバーの管理者権限
### 手順
1. git clone またはダウンロードします。
2. フォルダに入っている"config.ini"を開きます。
3. botトークンを入力します。トークンをダブルクオーテーション（"）などで囲む必要はありません。
4. "main.py"を開いて起動します。
