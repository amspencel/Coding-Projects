import random

import discord
from botInfo import TOKEN
import responses
from discord.ext import commands

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = discord.Client(intents=intents)

    bot = commands.Bot(intents=intents, command_prefix=['/','-','+'], case_insensitive=True)

    @bot.command(name="cope")
    async def copium(ctx):
        await ctx.message.delete()
        await ctx.send('https://media.tenor.com/KlvE4ndJha0AAAAd/narc-copium.gif')

    @bot.command(name="LREG")
    async def plusminus(ctx):
        await ctx.message.delete()
        await ctx.send('L Reginald')

    @bot.command(name="LRYA")
    async def deafened(ctx):
       await ctx.message.delete()
       await ctx.send('L deafened boy')

    @bot.command(name='+')
    async def dispicable(ctx):
         if str(ctx.message.author) == 'Colonel#2782':
             await ctx.send('L Reginald')

    @bot.command(name='-')
    async def dispicable2(ctx):
         if str(ctx.message.author) == 'Colonel#2782':
                await ctx.send('L Reginald')

    @bot.command(name='ORDER66')
    async def order_66(ctx):
        await ctx.send('Yes, my Lord.')
        await ctx.send('https://tenor.com/view/anakin-gif-23721049')

    @bot.command(name='onepiece')
    async def one_piece(ctx):
        await ctx.send('https://media.tenor.com/sxLBjystCmIAAAAM/damn-daniel-one-piece.gif')

    @bot.command(name='cry')
    async def crying_baby(ctx):
        await ctx.message.delete()
        await ctx.send('https://media.tenor.com/P8OYV56HSRAAAAAd/cry-sad.gif')

    @bot.command(name='yomama')
    async def yo_mama_joke(ctx):
        your_mother_jokes = [
            'Yo mama\'s so fat, when she fell I didn\'t laugh, but the sidewalk cracked up.',
            'Yo mama\'s so fat, when she skips a meal, the stock market drops.',
            'Yo mama\'s so fat, it took me two buses and a train to get to her good side.',
            'Yo mama\'s so fat, when she goes camping, the bears hide their food.',
            'Yo mama\'s so fat, if she buys a fur coat, a whole species will become extinct.',
            'Yo mama\'s so fat, she stepped on a scale and it said: "To be continued."'
            'Yo momma so fat, I swerved to miss her in my car and ran out of gas.',
            "Yo mama's so fat, when she wears high heels, she strikes oil.",
            "Yo mama's so fat, she was overthrown by a small militia group, and now she's known as the Republic of Yo Mama.",
            "Yo mama so fat, not even Dora can explore her.",
            "Yo mama so fat, she gets group insurance.",
            'Yo mama\'s so fat, when she went to KFC and the cashier asked what size bucket she wanted, she said, "The one on the roof!"',
            'Yo mama so big, her belt size is "equator."',
            "Yo mama so fat, when she talks to herself, it's a long-distance call.",
            'Yo mama so fat, she left in high heels and came back in flip flops.',
            "Yo mama so fat that when she hauls ass, she has to make two trips.",
            "Yo mama so fat, her job title is Spoon and Fork Operator.",
            "Yo mama so fat, when she walked past the TV, I missed three episodes.",
            "Yo momma's so fat, when she sits around the house, she SITS AROUND the house.",
            "Yo mama's so fat, her car has stretch marks.",
            "Yo mama's so fat, she can't even jump to a conclusion.",
            "Yo mama's so fat, her blood type is Ragu.",
            "Yo mama's so fat, if she was a Star Wars character, her name would be Admiral Snackbar.",
            "Yo mama's so fat, she brought a spoon to the Super Bowl.",
        ]
        response = random.choice(your_mother_jokes)
        await ctx.send(response)

    @bot.command(name='die')
    async def die(ctx):
        die_gifs = [
            'https://media.tenor.com/egdvZc6Rz8wAAAAM/you-should-die-saturday-night-live.gif',
            'https://media.tenor.com/E46DBR0-VVoAAAAM/dies-from-cringe-d-ies-from-cringe-star-wars.gif',
            'https://media.tenor.com/YmU-mwdvYqYAAAAM/shazz-dies-of-death.gif',
            'https://media.tenor.com/AmV8vMwODrEAAAAM/waiting-for.gif',
            'https://media.tenor.com/rp8_FjK0CdAAAAAM/dies-of-death.gif',
            'https://media.tenor.com/DdGTR3964QcAAAAM/black-panther-this-is-no-time-to-die.gif',
            'https://media.tenor.com/QCxZFOPHmSgAAAAM/jschlatt-schlatt.gif',
            'https://media.tenor.com/m8sVXGNHDx8AAAAM/die.gif',
            'https://media.tenor.com/-FK2RZYKYz8AAAAM/wtf-dead-chat-dies-of-cringe.gif'

        ]
        response = random.choice(die_gifs)
        await ctx.message.delete()
        await ctx.send(response)

    @bot.command(name='myusername')
    async def name(ctx):
        author = ctx.message.author

        await ctx.send(str(author))

    @bot.command(name='kanyequote')
    async def kanye_quote(ctx):
        kanye_quotes = [
            'Sorry, but I chose not to be no slave',
            'You may be talented, but you’re not Kanye West.',
            'People ask me a lot about my drive. I think it comes from, like, having a sexual addiction at a really young age. '
            'Look at the drive that people have to get sex – to dress like this and get a haircut and be in the club in the freezing cold at 3 A.M., '
            'the places they go to pick up a girl. If you can focus the energy into something valuable, put that into work ethic...',
            'As a man I am flawed, but my music is perfect.',
            'For me to say I wasn’t a genius, I would just be lying to you and to myself',
            'I don’t want to say these really big, over-the-top statements that end up getting quoted.',
            'I liberate minds with my music. That\'s more important than liberating a few people from apartheid or whatever.',
            'One of my biggest Achilles heels has been my ego. And if I, Kanye West, can remove my ego, I think there’s hope for everyone.',
            'You should only believe about 90% of what I say. As a matter of fact, don’t even believe anything that I’m saying at all. '
            'I could be completely f—g with you, and the world, the entire time.',
            'The media crucify me like they did Christ.',
            'George Bush doesn’t care about black people.',
            'I\'m not comfortable with comfort. I\'m only comfortable when I\'m in a place where I\'m constantly learning and growing.'
            'If you put your heart into something and you had a grasp of what was really good and you knew you delivered a good product, '
            'you have the right to defend your product after people criticize it.',
            'Most people are slowed down by the perception of themselves. If you’re taught you can’t do anything, you won’t do anything. I was taught I can do everything.',
            'For me, first of all, dopeness is what I like the most. Dopeness. People who want to make things as dope as possible, and, by default, make money from it.',
            'I am God’s vessel. But my greatest pain in life is that I will never be able to see myself perform live.',
            'If I don\'t win, the award show loses credibility.',
            'Well, my name is Skyler White, yo. My husband is Walter White, yo.',
            '`What\'s scary to me is Henny makes girls look like Halle Berry to me \nSo excuse me miss, I forgot your name`',
            '`She got a light skinned friend look like Michael Jackson \nGot a dark skinned friend look like Michael Jackson`',
            '`Address me as "Your Highness" \nHigh as United, 30,000 feet up and you are not invited \nNiggas be writin’ bullshit like they gotta work \n'
            'Niggas going through real shit, man they outta work \nThat\'s why I never God damn dance track, gotta hurt '
            '\nThat\'s why I rather spit something that gotta perch`',
            '`The plan was to drink until the pain over / But what\'s worse, the pain or the hangover?`',
        ]

        response = random.choice(kanye_quotes)
        await ctx.send(response)

    @bot.command(name='suntzu')
    async def suntzu_quote(ctx):
        suntzu_quotes = [
  "The general who wins the battle makes many calculations in his temple before the battle is fought. The general who loses makes but few calculations beforehand.",
  "A leader leads by example not by force.",
  "The control of a large force is the same principle as the control of a few men: it is merely a question of dividing up their numbers.",
  "The ultimate in disposing one's troops is to be without ascertainable shape. Then the most penetrating spies cannot pry in nor can the wise lay plans against you.",
  "If words of command are not clear and distinct, if orders are not thoroughly understood, the general is to blame. But if his orders ARE clear, and the soldiers nevertheless disobey, then it is the fault of their officers.",
  "Strategy without tactics is the slowest route to victory. Tactics without strategy is the noise before defeat.",
  "All warfare is based on deception.",
  "If fighting is sure to result in victory, then you must fight.",
  "One defends when his strength is inadaquate, he attacks when it is abundant.",
  "The quality of decision is like the well-timed swoop of a falcon which enables it to strike and destroy its victim.",
  "When the enemy is at ease, be able to weary him; when well fed, to starve him; when at rest, to make him move. Appear at places to which he must hasten; move swiftly where he does not expect you.",
  "If you know your enemy and you know yourself you need not fear the results of a hundred battles. If you know yourself but not the enemy for every victory gained you will also suffer a defeat. If you know neither the enemy nor yourself you will succumb in every battle.",
  "The general who advances without coveting fame and retreats without fearing disgrace, whose only thought is to protect his country and do good service for his sovereign, is the jewel of the kingdom.",
  "For to win one hundred victories in one hundred battles is not the acme of skill. To subdue the enemy without fighting is the acme of skill.",
  "What the ancients called a clever fighter is one who not only wins, but excels in winning with ease.",
  "To a surrounded enemy, you must leave a way of escape.",
  "To know your Enemy, you must become your Enemy.",
  "Thus, what is of supreme importance in war is to attack the enemy's strategy.",
  "A leader leads by example, not force.",
  "Too frequent rewards indicate that the general is at the end of his resources; too frequent punishments that he is in acute distress.",
  "Pretend inferiority and encourage his arrogance.",
  "All men can see these tactics whereby I conquer, but what none can see is the strategy out of which victory is evolved.",
  "If we do not wish to fight, we can prevent the enemy from engaging us even though the lines of our encampment be merely traced out on the ground. All we need to do is to throw something odd and unaccountable in his way.",
  "A military operation involves deception. Even though you are competent, appear to be incompetent. Though effective, appear to be ineffective.",
  "Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.",
  "The best victory is when the opponent surrenders of its own accord before there are any actual hostilities... It is best to win without fighting.",
  "Opportunities multiply as they are seized.",
  "Speed is the essence of war. Take advantage of the enemy's unpreparedness; travel by unexpected routes and strike him where he has taken no precautions.",
  "If your opponent is of choleric temperament, seek to irritate him.",
  "Management of many is the same as management of few. It is a matter of organization.",
  "The good fighters of old first put themselves beyond the possibility of defeat, and then waited for an opportunity of defeating the enemy.",
  "Build your opponent a golden bridge to retreat across.",
  "Swift as the wind. Quiet as the forest. Conquer like the fire. Steady as the mountain.",
  "It is essential to seek out enemy agents who have come to conduct espionage against you and to bribe them to serve you. Give them instructions and care for them. Thus doubled agents are recruited and used.",
  "Now the reason the enlightened prince and the wise general conquer the enemy whenever they move and their achievements surpass those of ordinary men is foreknowledge.",
  "And therefore those skilled in war bring the enemy to the field of battle and are not brought there by him.",
  "There is no instance of a nation benefitting from prolonged warfare.",
  "When able to attack, we must seem unable; when using our forces, we must seem inactive; when we are near, we must make the enemy believe we are far away; when far away, we must make him believe we are near.",
  "When torrential water tosses boulders, it is because of its momentum. When the strike of a hawk breaks the body of its prey, it is because of timing.",
  "Secret operations are essential in war; upon them the army relies to make its every move.",
  "It is said that if you know your enemies and know yourself, you will not be imperilled in a hundred battles; if you do not know your enemies but do know yourself, you will win one and lose one; if you do not know your enemies nor yourself, you will be imperilled in every single battle.",
  "He who knows when he can fight and when he cannot will be victorious.",
  "Subtle and insubstantial, the expert leaves no trace; divinely mysterious, he is inaudible. Thus he is master of his enemy's fate.",
  "A skilled commander seeks victory from the situation and does not demand it of his subordinates."
]

        response = random.choice(suntzu_quotes)
        await ctx.send(response)

    # @bot.event
    # async def on_member_join(member):
    #     await bot.get_channel(758699253215789121).send(f'{member.name} has joined')
    #
    # @bot.event
    # async def on_member_remove(member):
    #     await bot.get_channel(758699253215789121).send(f'{member.name} has left')
    #     await bot.get_channel(758699253215789121).send('https://media.tenor.com/CSITQibp6qcAAAAM/sad-upset.gif')
    #     await bot.

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("`I can't goofy`")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`You're missing something homie`")

    # @client.event
    # async def on_message(message):
    #     if message.author == client.user:
    #         return
    #
    #     username = str(message.author)
    #     user_message = str(message.content)
    #     channel = str(message.channel)
    #
    #     print(f"{username} said: '{user_message}' ({channel})")
    #
    #     if user_message[0] == '/':
    #         user_message = user_message[1:]
    #         await send_message( message, user_message, is_private=True)
    #     else:
    #         await send_message(message, user_message, is_private=False)



    bot.run(TOKEN)