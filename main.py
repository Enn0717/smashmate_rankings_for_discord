import discord
from discord import app_commands
import getFromSite
import configparser
import dbController
import makeRankBoard

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#コンフィグファイル読み込み
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

#discord.py設定
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(description='スマメイトIDとDiscordアカウントを紐づけします')
async def smashmate(interaction: discord.Interaction,mate_id:int):
    try:
        dbController.dbinit()
        discordname=interaction.user.name
        discord_id=interaction.user.id
        smashmatename=getFromSite.getName(mate_id)
        dbController.dbMakeUser(smashmatename,discord_id)
        dbController.dbSetSmashmate_id(discord_id,mate_id)
        rate=getFromSite.getRateMax(mate_id)
        dbController.dbUpdaterate(discord_id,rate)
        if rate==0:
            message=f'{discordname}さん、{smashmatename}と紐づけされました。最高レートは未測定です。\n試合後に"/reload"でレートが更新できます。'
        else:
            message=f'{discordname}さん、{smashmatename}と紐づけされました。現在の最高レートは{rate}です。'
        await interaction.response.send_message(message)
    except Exception as e:
        await interaction.response.send_message(f'何かエラーが起きました:{e}')
        
@tree.command(description='レートを更新します')
async def reload(interaction: discord.Interaction):
    try:
        dbController.dbinit()
        discord_id=interaction.user.id
        smashmate_id = dbController.dbReadSmashmateID(discord_id)
        name = dbController.dbReadname(discord_id)
        rate = getFromSite.getRateMax(smashmate_id)
        dbController.dbUpdaterate(discord_id,rate)
        await interaction.response.send_message(f'レートが更新されました。現在の{name}さんの最高レートは{rate}です。')
    except Exception as e:
        await interaction.response.send_message(f'何かエラーが起きました:{e}')

@tree.command(description='紐づけを抹消します')
async def delete(interaction: discord.Interaction):
    try:
        dbController.dbinit
        dbController.dbdelete(interaction.user.id)
        await interaction.response.send_message(f'登録が削除されました。')
    except Exception as e:
        await interaction.response.send_message(f'何かエラーが起きました:{e}')

@tree.command(description='ランキングを表示します')
async def rank(interaction: discord.Interaction):
    try:
        embed=makeRankBoard.make()
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f'何かエラーが起きました:{e}')

@tree.command(description='自分以外のユーザーを追加します')
async def add(interaction: discord.Interaction,mate_id:int):
    try:
        dbController.dbinit()
        smashmatename=getFromSite.getName(mate_id)
        dbController.dbMakeUserWithSmashmate_id(smashmatename,mate_id)
        rate=getFromSite.getRateMax(mate_id)
        dbController.dbUpdaterateBysmashmate_id(mate_id,rate)
        if rate==0:
            message=f'{smashmatename}さんを登録しました。最高レートは未測定です。'
        else:
            message=f'{smashmatename}さんを登録しました。現在の最高レートは{rate}です。'
        await interaction.response.send_message(message)
    except Exception as e:
        await interaction.response.send_message(f'何かエラーが起きました:{e}')

@tree.command(description='addコマンドで追加されたユーザーを削除します')
async def remove(interaction: discord.Interaction,mate_id:int):
    try:
        dbController.dbinit()
        dbController.dbdeleteBySmashmate_id(mate_id)
        message=f'登録が抹消されました。'
        await interaction.response.send_message(message)
    except Exception as e:
        await interaction.response.send_message(f'何かエラーが起きました:{e}')

@client.event
async def on_ready():
    dbController.dbinit()
    await tree.sync()


client.run(config_ini['Discord']['key'])