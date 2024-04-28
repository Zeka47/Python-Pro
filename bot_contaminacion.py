import discord
from discord.ext import commands
import random
import os
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesion con {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy {bot.user} y fui creado para dar ideas de manualidades con materiales reciclables!, puedes pedir ayuda sobre los comandos con el comando $help')

@bot.command()
async def help(ctx):
    definicion = "1.- $ideamanualidiad, 2.-$imagmanualidad, 3.-$imagcontaminacion, 4.-$contaminacion"
    await ctx.send(definicion)

manualidades = [
    '⁂1.-Semilleros con vasos de plástico/latas.',
    '⁂2.-Floreros con recipientes de vidrio.',
    '⁂3.-Recipiente De Cepillos de Dientes Hecho Con Botellas De Plástico.',
    '⁂4.-Dispensador de comida para mascotas hecho con botellas de plastico.',
    '⁂5.-Un servilletero de una botella.',
    '⁂6.-Florero con botella de gaseosa o agua.',
    '⁂7.-Porta libros (o porta cuadernos).',
    '⁂8.-Portalápices con rollos de papel higiénico.',
]
@bot.command()
async def ideamanualidiad(ctx):
    idea = random.choice(manualidades)
    await ctx.send(idea)

# Funcion que explica que es la contaminacion
@bot.command()
async def contaminacion(ctx):
    definicion = "La contaminacion es un problema causado por diferentes problemas, los cuales pueden generar cambios en el ecosistema, la flora y fauna del planeta. Estos problemas pueden ser un gran problema para el ser humano y la vida en el planeta tierra"
    await ctx.send(definicion)

@bot.command()
async def imagcontaminacion(ctx):
    Tli = os.listdir('contaminacion')
    img_name = random.choice(Tli)
    with open(f'contaminacion/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def imagmanualidad(ctx):
    Tli = os.listdir('manualidades')
    img_name = random.choice(Tli)
    with open(f'manualidades/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("YOUR TOKEN")
