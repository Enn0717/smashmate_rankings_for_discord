import dbController
import discord

def make():
    rankings=dbController.dbPrintall()

    printranking=""
    printranking=printranking+"順位\t名前\t\tレート\n"
    count=1
    for ranking in reversed(rankings):
        if count == 1:
            star = "🏆"
        elif count == 2:
            star = "🥈"
        elif count == 3:
            star = "🥉"
        else:
            star = count
        #タブ調整
        if 3<len(ranking[1]):
            tab = "\t"
        else:
            tab = "\t\t"
        printranking=printranking+star+"\t"+ranking[1]+tab+ranking[2]+"\n"
        count=count+1

    embed = discord.Embed(title="スマメイト レートランキング",description=printranking)
    return embed