
import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    game = discord.Game("TESTING")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("READY")
@bot.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content[0:4] == "$검색 ":
        messagesplit = message.content.split(" ")
        messagesplit = ''.join(messagesplit[1:])
        webpage = requests.get("https://www.google.com/search?q="+str(messagesplit)+"&hl=ko&tbm=isch")
        soup = BeautifulSoup(webpage.text, "html.parser")
        img = soup.find_all('img')
        img2=img[2]
        img_src=img2.get('src')
        embed = discord.Embed(title=message.content[4:]+":",
                              description="https://www.google.com/search?q="+str(messagesplit)+"&hl=ko&tbm=isch",
                              color=0x383b38)
        embed.set_footer(
            icon_url="https://www.google.com/search?q="+str(messagesplit)+"&hl=ko&tbm=isch")
        embed.set_image(url=img_src)
        await message.channel.send(message.content, embed=embed)
    if message.content[0:4] == "$계산 ":
        splitphase = message.content.split(" ")
        first1 = int(splitphase[1])
        second2 = splitphase[2]
        third3 = int(splitphase[3])
        result2 = 0
        if second2 == "*":
            result2 = first1 * third3
        elif second2 == "/":
            result2 = first1 / third3
        elif second2 == "+":
            result2 = first1 + third3
        elif second2 == "-":
            result2 = first1 - third3
        await message.channel.send(result2)
    if message.content[0:5] == "$계산기 ":
        splitphase = message.content.split(" ")
        result3 = int(splitphase[1])

        for i in range(len(splitphase)):
            if i == 0 or i == 1:
                pass
            elif splitphase[i] != "*" and splitphase[i]!="+"and splitphase[i]!= "/"and splitphase[i]!= "-":
                pass
            elif splitphase[i] == "*":
                result3 *= int(splitphase[i+1])
            elif splitphase[i] == "+":
                result3 += int(splitphase[i+1])
            elif splitphase[i] == "-":
                result3 -= int(splitphase[i+1])
            elif splitphase[i] == "/":
                result3 /= int(splitphase[i+1])
        await message.channel.send(result3)
    if message.content[0:4] == "$삭제 ":
        split4 = message.content.split(" ")
        split4 = int(split4[1])
        await message.channel.purge(limit=split4)
    if message.content[0:4] == "$도배 ":
        split5 = message.content.split(" ")
        split6 = int(split5[1])
        split7 = ' '.join(split5[2:])
        for i in range(split6):
            await message.channel.send(split7)




access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
