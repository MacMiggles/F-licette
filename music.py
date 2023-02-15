import discord
from discord.ext import commands
import youtube_dl 

class music(commands.Cog):
  def __init__(self, client):
    self.client = client
  

  @commands.command()
  async def list(self, ctx):
    await ctx.send("This is a bot that plays music. 🤖")
    await ctx.send("Play, pause, resume, stop, leave, ban and copyright. ")

  @commands.command()
  async def leave(self, ctx):
    await ctx.voice_client.disconnect()

  @commands.command()
  async def Play(self,ctx,url):
    async def player(ctx, url):
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
      YDL_OPTIONS = {'format':"bestaudio"}
      vc = ctx.voice_client
      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
          info = ydl.extract_info(url, download = False)
          url2 = info['formats'][0]['url']
          source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
          vc.play(source)


 
    






    if ctx.author.voice is None:
      await ctx.send("📡 You are not connected to any channels!")

    elif ctx.voice_client is None:
      await ctx.author.voice.channel.connect()
      await player(ctx, url)
    else:
      ctx.voice_client.stop()
      await player(ctx, url)

  @commands.command()
  async def pause (self, ctx):
    ctx.voice_client.pause()
    await ctx.send("⏹ Pause")
  @commands.command()
  async def resume (self, ctx):
    ctx.voice_client.resume()
    await ctx.send("⏯ Play")

  @commands.command()
  async def ban(self,ctx):
    
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download = False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
      vc.play(source)

    idiot = ctx.author
    await idiot.move_to(None)


  @commands.command()
  async def stop(self, ctx):
    ctx.voice_client.stop()
    await ctx.send("⛔️")

 

    if ctx.author.voice is None:
        await ctx.send("📡 You are not connected to any channels!")

    elif ctx.voice_client is None:
      await ctx.author.voice.channel.connect()
      await player(ctx)
    else:
      ctx.voice_client.stop()
      await player(ctx)

def setup(client):
  client.add_cog(music(client))
