import discord
import youtube_dl

playlist = {
    "Huge Dance Hits": "https://www.youtube.com/watch?v=tyITL_exICo&list=RDCLAK5uy_kWiJXUNLZM9EyS3GBGznl1ku8_cOos97U&start_radio=1",
    "Afropop Hits": "https://www.youtube.com/watch?v=Ecl8Aod0Tl0&list=RDCLAK5uy_lLMOe89gNlI8asCCYU_bcEc_2TC4M4bQY&start_radio=1",
    "Massive Rock Hits": "https://www.youtube.com/watch?v=pXRviuL6vMY&list=RDCLAK5uy_k7h5535MeHE8xmgHsrZx7HOKH4lb5vAfY&start_radio=1",
    "Heavy Hitters": "https://www.youtube.com/watch?v=hBTNyJ33LWI&list=RDCLAK5uy_nVT2-bFfxplES7OQSLcnwlJqpsQ9gn0yY&start_radio=1",
    "Totally Pop": "https://www.youtube.com/watch?v=vfE5z-l1zH0&list=RDCLAK5uy_lznqoXCDt_wH0Yu3_IK6q3chQI3d2G1cU&start_radio=1",
    "Totally Hits": "https://www.youtube.com/watch?v=TUVcZfQe-Kw&list=RDCLAK5uy_nrS6tX1-aHomOfpEBSbVYNfM9R58rAlrs&start_radio=1",
    "Pop Gold": "https://www.youtube.com/watch?v=hLQl3WQQoQ0&list=RDCLAK5uy_nHSqCJjDrW9HBhCNdF6tWPdnOMngOv0wA&start_radio=1",
    "Soft Rock Ballads": "https://www.youtube.com/watch?v=Ak_MTXQALa0&list=RDCLAK5uy_nyKVppE-RpLkeCcwLct4rvN9e8AAsS_qw&start_radio=1",
    "Happy Pop Hits": "https://www.youtube.com/watch?v=Il0S8BoucSA&list=RDCLAK5uy_mfdqvCAl8wodlx2P2_Ai2gNkiRDAufkkI&start_radio=1",
    "Chilled Hip-Hop": "https://www.youtube.com/watch?v=yEG2VTHS9yg&list=RDCLAK5uy_myzznSrnHv4d3VAWYEFRkjuSvgiAXZshk&start_radio=1",
    "Feel-good RnB Vibes": "https://www.youtube.com/watch?v=tsO01Nl5TO4&list=RDCLAK5uy_kF-D-D23zHZ5JcC1mO5EhQEPqZ9-SK4NU&start_radio=1",
    "Feel-good Dance Vibes": "https://www.youtube.com/watch?v=m7Bc3pLyij0&list=RDCLAK5uy_m8UYTpmaUGhIlXpWiyukIgw4Ug_POVPNw&start_radio=1",
    "Shout-Out Pop Hits": "https://www.youtube.com/watch?v=TUVcZfQe-Kw&list=RDCLAK5uy_lb6CVU6S4uVugLVNTU9WhqfaomWAgnho4&start_radio=1",
    "Lose Yourself": "https://www.youtube.com/watch?v=xFYQQPAOz7Y&list=RDCLAK5uy_lVm93MPGWY2gMYbeUHn2Y5HnRNRzMbQfM&start_radio=1",
    "Pop n Indie Easy Listening": "https://www.youtube.com/watch?v=uJ_1HMAGb4k&list=RDCLAK5uy_nn3qxym-fhKvsUZShqgxWUr7lQKURa3w0&start_radio=1",
    "Easy EDM": "https://www.youtube.com/watch?v=3no252J8-VA&list=RDCLAK5uy_n4bsKshkdwxaEJYz8ZXxh6kF9Frsf369k&start_radio=1",
    "Feeling Epic EDM": "https://www.youtube.com/watch?v=gV6KNVii7XQ&list=RDCLAK5uy_nBQm8_YpP--R6zU8p3dypKm1QKqzWY6qU&start_radio=1",
    "Feel-Good Pop n Rock": "https://www.youtube.com/watch?v=mk48xRzuNvA&list=RDCLAK5uy_m0wlRoNn5iCTTgBedfoOQ19Jq9P3XTLIA&start_radio=1",
    "Queens Speak": "https://www.youtube.com/watch?v=hsm4poTWjMs&list=RDCLAK5uy_lnUHokP0KoSlL-ZliOoUWhsKfU5id-b2E&start_radio=1",
    "Hip Hop Classics": "https://www.youtube.com/watch?v=eaPzCHEQExs&list=RDCLAK5uy_kP2172rQNb3KFXz880xp6M98R_ME5CIKA&start_radio=1",
    "Ultimate Indie Anthems": "https://www.youtube.com/watch?v=TDe1DqxwJoc&list=RDCLAK5uy_nGla7fZdBfRak2-LrbYP0aHdjz8Lwv7lQ&start_radio=1",
    "Indie Overload": "https://www.youtube.com/watch?v=LQziZUGuEFE&list=RDCLAK5uy_kIEEMKpM6yjpBI82J-4Ua3AAAwULUx7AE&start_radio=1",
    "Alt on Repeat": "https://www.youtube.com/watch?v=tjpgJjdk52c&list=RDCLAK5uy_nGTZ-bU3GDTL3y16JZY8OVn1rXIEgqkOM&start_radio=1"
}
class YLBotClient(discord.Client):
    async def on_ready(self):
        print('Вы зашли как {0.user}'.format(client))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('!play'):
            voice_channel = message.author.voice.channel
            if voice_channel is not None:
                url = message.content.split(' ')[1]
                vc = await voice_channel.connect()
                with youtube_dl.YoutubeDL() as ydl:
                    info = ydl.extract_info(url, download=False)
                    URL = info['formats'][0]['url']
                    vc.play(discord.FFmpegPCMAudio(URL))
            else:
                await message.channel.send('Вы должны быть в голосовом канале чтобы использовать эту команду')
    async def on_message_playlist(self, name):
        if name.author == client.user:
            return

        if name.content.startswith('!find'):
            voice_channel = name.author.voice.channel
            if voice_channel is not None:
                command = name.content.split(' ')
                if len(command) == 2:
                    if command[1] in playlist:
                        url = playlist[command[1]]
                    else:
                        url = command[1]
                else:
                    await name.channel.send('Invalid command')
                    return
                vc = await voice_channel.connect()
                with youtube_dl.YoutubeDL() as ydl:
                    info = ydl.extract_info(url, download=False)
                    URL = info['formats'][0]['url']
                    vc.play(discord.FFmpegPCMAudio(URL))
            else:
                await name.channel.send('Вы должны быть в голосовом канале чтобы использовать эту команду')
intents = discord.Intents.default()
client = YLBotClient(intents=intents)
client.run("MTA5OTk3NDUzMTcyMTk5NDI5MQ.GwavQk.t6UHFiCQftRiv1WMRUfiKafEDmRero8GihK-GY")