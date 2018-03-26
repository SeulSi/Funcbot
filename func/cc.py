import redis, ast, discord

db = redis.StrictRedis(decode_responses=True)

def set(serverid, title, value):
	if db.get("cc("+serverid+")") is None:
		newdict = {}
	else:
		newdict = ast.literal_eval(db.get("cc("+serverid+")"))
	newdict[title] = value
	db.set("cc("+serverid+")", str(newdict))
	return "Done"
def get(serverid, title):
	if not db.get("cc("+serverid+")") is None:
		newdict = ast.literal_eval(db.get("cc("+serverid+")"))
		try:return newdict[title] 
		except:return None
	else:
		return None
def delete(serverid, title):
	if not db.get("cc("+serverid+")") is None:
		newdict = ast.literal_eval(db.get("cc("+serverid+")"))
		if title in newdict:
			del newdict[title]
			db.set("cc("+serverid+")", str(newdict))
			return "clear"
		else:
			return None
	else:
		return None
def clear(serverid):
	newdict = {}
	db.set("cc("+serverid+")", str(newdict))
def list(serverid):
	if not db.get("cc("+serverid+")") is None:
		newdict = ast.literal_eval(db.get("cc("+serverid+")"))
		if not newdict == {}: return newdict
		else: None
	else:
		return None
async def on_cc(msg):
	if not get(str(msg.guild.id), msg.content) is None:
		await msg.channel.send(get(str(msg.guild.id), msg.content).replace("<맨션>", msg.author.mention).replace("<이름>", msg.author.name).replace("<아이디>", str(msg.author.id)))