import dbController
import discord

def make():
    rankings=dbController.dbPrintall()
    printranking=""
    printranking=printranking+"順位\t名前\t\tレート\n"
    count=1
    lastrate=0
    for ranking in reversed(rankings):
        if ranking[2]==lastrate:
            count=count-1
        if count == 1:
            star = "🏆"
        elif count == 2:
            star = "🥈"
        elif count == 3:
            star = "🥉"
        else:
            star = count
        tab = "\t"
        if ranking[2] is None:
            printranking=printranking+str(star)+"\t"+ranking[1]+tab+"未計測"+"\n"
        else:
            printranking=printranking+str(star)+"\t"+ranking[1]+tab+ranking[2]+"\n"
        if ranking[2]==lastrate:
            count=count+1
        lastrate=ranking[2]
        count=count+1

    embed = discord.Embed(title="スマメイト レートランキング",description=printranking)
    return embed