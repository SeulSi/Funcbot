import ast, redis

db = redis.StrictRedis(decode_responses=True)

def check(serverid, userid):
	if db.get("settings("+serverid+")") is None:setyok = "20"
	else:
		try:setyok = ast.literal_eval(db.get("settings("+serverid+")"))["yokhigh"]
		except:setyok = "20"
		try:asdf = ast.literal_eval(db.get("settings("+serverid+")"))["yokdo"]
		except:asdf = "kick"
	if db.get("ylev("+serverid+")") is None:
		dict1 = {}
		dict1["high"] = setyok
		dict1["status"] = "0"
		dict1["yokdo"] = asdf
		return dict1
	if userid in ast.literal_eval(db.get("ylev("+serverid+")")):
		value = ast.literal_eval(db.get("ylev("+serverid+")"))[userid]
		dict1 = {}
		dict1["high"] = setyok
		dict1["status"] = value
		dict1["yokdo"] = asdf
		return dict1
	else:
		dict1 = {}
		dict1["high"] = setyok
		dict1["status"] = "0"
		dict1["yokdo"] = asdf
		return dict1
def warn(serverid, userid):
	res = {}
	try:setyok = ast.literal_eval(db.get("settings("+serverid+")"))["yokhigh"]
	except:setyok = "20"
	try:sd = ast.literal_eval(db.get("settings("+serverid+")"))["yokhigh"]
	except: sd = "20"
	try:newdict = ast.literal_eval(db.get("ylev("+serverid+")"))
	except:newdict = {}
	try:newdict[userid] = str(int(newdict[userid]) + 1)
	except:newdict[userid] = "1"
	if int(newdict[userid]) > int(sd) - 1:
		del newdict[userid]
		try:asdf = ast.literal_eval(db.get("settings("+serverid+")"))["yokdo"]
		except:asdf = "kick"
		res["do"] = asdf.replace("mute", "kick")
		res["warn"] = None
		res["setyok"] = setyok
	else:
		res["do"] = None
		res["warn"] = newdict[userid]
		res["setyok"] = setyok
	db.set("ylev("+serverid+")", str(newdict))
	return res
def clear(serverid, userid):
	try:newdict = ast.literal_eval(db.get("ylev("+serverid+")"))
	except:
		return "claer"
	try:del newdict[userid]; db.set("ylev("+serverid+")", str(newdict));return "clear"
	except Exception as e: print(e);return "clear"
def allclear(serverid):
	newdict = {}
	db.set("ylev("+serverid+")", str(newdict))
	return "clear"
def setyok(serverid, value):
	try:sd = ast.literal_eval(db.get("settings("+serverid+")"))
	except: sd = {}
	sd["yokhigh"] = value
	db.set("settings("+serverid+")", str(sd))
	return "clear"
def yokdo(serverid, value):
	try:sd = ast.literal_eval(db.get("settings("+serverid+")"))
	except: sd = {}
	sd["yokdo"] = value
	db.set("settings("+serverid+")", str(sd))
	return "clear"