import discord, datetime, func.util, ast
deletelist = {}
global client
global color

def settings(one, two):
	global client
	global color
	client = two
	color = one
async def edit_log(bmsg, msg):
	if msg.author.bot: return
	if not msg.embeds == []: return  
	em = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
	em.add_field(name="수정 하기전",  value=""+bmsg.content+"", inline=False)
	em.add_field(name="수정한 후",  value=""+msg.content+"", inline=False)
	em.add_field(name="유저",  value=""+msg.author.mention+"", inline=False)
	em.add_field(name="채널",  value=""+msg.channel.mention+"", inline=False)
	em.set_footer(text="수정한 시간")
	em.set_thumbnail(url=msg.author.avatar_url)
	tmp = func.util.get_ch(msg.guild.id)
	if not tmp is None: ch = msg.guild.get_channel(tmp)
	else:return
	await ch.send(embed=em)
async def del_bulk_log(msglist, ch):
	tmp = []
	for i in msglist: 
		tmp.append(i)
	deletelist[str(client.get_channel(ch).guild.id)] = tmp
async def del_log(msg):	
	if not msg.embeds == []:return
	try:tmp = deletelist[str(msg.guild.id)]
	except:tmp = []
	if not tmp == []:
		try:tmp.remove(msg.id)
		except:tmp = []
		deletelist[str(msg.guild.id)] = tmp
		if tmp == []:
			em = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
			em.add_field(name="로깅", value="동시에 많은 메시지가\n제거 되었습니다", inline=False)
			em.set_footer(text="삭제된 시간")
			tmp = func.util.get_ch(msg.guild.id)
			if not tmp is None: ch = msg.guild.get_channel(tmp)
			else:return
			await ch.send(embed=em)
	else:
		if msg.author.bot:return
		em = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
		em.add_field(name="삭제된 내용", value=""+msg.content+"", inline=False)
		em.add_field(name="유저", value=""+msg.author.mention+"", inline=False)
		em.add_field(name="채널",  value=""+msg.channel.mention+"", inline=False)
		em.set_footer(text="삭제된 시간")
		em.set_thumbnail(url=msg.author.avatar_url)
		tmp = func.util.get_ch(msg.guild.id)
		if not tmp is None: ch = msg.guild.get_channel(tmp)
		else:return
		await ch.send(embed=em)
async def file(msg):
	if not msg.attachments == []:
		filename = msg.attachments[0].filename
		fileurl = msg.attachments[0].url
		em = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow(), title="파일 업로드!")
		if filename.lower().endswith(".png") or filename.lower().endswith('.jpg') or filename.endswith(".jpeg"):
			em.set_image(url=fileurl)
		else:
			em.add_field(name=""+filename+"", value="파일 링크:\n"+fileurl+"", inline=False)
		em.add_field(name="유저", value=""+msg.author.mention+"", inline=False)
		em.add_field(name="채널",  value=""+msg.channel.mention+"", inline=False)
		em.set_footer(text="업로드 된 시간!")
		em.set_thumbnail(url=msg.author.avatar_url)
		tmp = func.util.get_ch(msg.guild.id)
		if not tmp is None: ch = msg.guild.get_channel(tmp)
		else:return
		await ch.send(embed=em)