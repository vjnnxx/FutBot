import discord
import os
import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': os.getenv('FUT_APITOKEN') }
connection.request('GET', '/v2/teams/586', None, headers )
response = connection.getresponse().read().decode()

arquivo = open('file1.txt', 'w')
arquivo.write(response)
arquivo.close()

print (response)

client = discord.Client()

@client.event
async def on_ready():
  print('Logado como: {0.user}' .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('-coe'):
    await message.channel.send('Salve menozada botzao aqui B)')
  if message.content.startswith('-ajuda'):
    await message.channel.send('Tamo trabalhando ainda menor, novidades em breve!')

#Inicia o bot e pega o token através de uma variável do ambiente
client.run(os.getenv('TOKEN'))