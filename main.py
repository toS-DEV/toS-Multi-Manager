# Pycordを読み込む
import discord
import config


# アクセストークンを設定
TOKEN = config.TOKEN  # 自分のアクセストークンと置換してください

# Botの大元となるオブジェクトを生成する
bot = discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Game("Discord Bot入門"),  # "〇〇をプレイ中"の"〇〇"を設定,
)


# 起動時に自動的に動くメソッド
# #03で詳しく説明します
@bot.event
async def on_ready():
    # 起動すると、実行したターミナルに"Hello!"と表示される
    print("Hello!")


# Botが見える場所でメッセージが投稿された時に動くメソッド
@bot.event
async def on_message(message: discord.Message):
    # メッセージ送信者がBot(自分を含む)だった場合は無視する
    if message.author.bot:
        return

    # メッセージが"GOMIGAME"だった場合、"Y0star"と返信する
    if message.content == 'GOMIGAME':
        await message.reply("Y0star")
        



# Botを起動
bot.run(TOKEN)

