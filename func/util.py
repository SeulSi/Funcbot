import requests, json, urllib.request, redis, ast, os, user

db = redis.StrictRedis(decode_responses=True)

api1 = user.naver2
api2 = user.naver2

def tran(context): 
	r = requests.get("http://ws.detectlanguage.com/0.2/detect?q="+context+"&key=demo")
	lang = json.loads(r.content.decode("UTF-8"))["data"]["detections"][0]["language"]
	encText = urllib.parse.quote(context)
	if lang == "ko":
		target = "en"
	else:
		target = "ko"
	sr = "source="+lang+"&target="+target+"&text=" + encText
	url = "https://openapi.naver.com/v1/papago/n2mt"
	request = urllib.request.Request(url)
	request.add_header("X-Naver-Client-Id", api1)
	request.add_header("X-Naver-Client-Secret",api2)
	response = urllib.request.urlopen(request, data=sr.encode("utf-8"))
	rescode = response.getcode()
	finish = {}
	finish["src"] = lang
	finish["tar"] = target
	finish["answer"] = json.loads(response.read().decode("UTF-8"))["message"]["result"]["translatedText"]
	return finish
async def set_ch(serverid, chid):
	if db.get("settings("+str(serverid)+")") is None: tmp = {}
	else: tmp = ast.literal_eval(db.get("settings("+str(serverid)+")"))
	tmp["log"] = chid
	db.set("settings("+str(serverid)+")", str(tmp))
	return True
def get_ch(serverid):
	try:tmp = ast.literal_eval(db.get("settings("+str(serverid)+")"))["log"]	
	except:tmp = None
	return tmp
def wrong(content):
	encText = urllib.parse.quote(content)
	url = "https://openapi.naver.com/v1/search/errata.json?query=" + encText
	request = urllib.request.Request(url)
	request.add_header("X-Naver-Client-Id",api1)
	request.add_header("X-Naver-Client-Secret",api2)
	response = urllib.request.urlopen(request)
	rescode = response.getcode()
	if(rescode==200):
		answer = json.loads(response.read().decode("UTF-8"))["errata"]
		if not answer == "":
			return answer
		else:
			return None
def set_notice_ch(serverid, ch):
	if db.get("settings("+serverid+")") is None:nedict = {}
	else:nedict = ast.literal_eval(db.get("settings("+serverid+")"))
	nedict["channel"] = ch
	db.set("settings("+serverid+")", str(nedict))	
	return "clear"
async def notice(content, client):
	chlist = []
	for i in client.guilds:
		try:tmp_ch = i.get_channel(int(ast.literal_eval(db.get("settings("+str(i.id)+")"))["channel"]));chlist.append(tmp_ch)
		except:pass
	for i in chlist:
		await i.send(content)
	return len(chlist)
def set_hi_text(serverid, text):
	if data.get("settings("+serverid+")") is None:newdict = {}
	else:newdict = ast.literal_eval(data.get("settings("+serverid+")"))
	newdict["sayhi"] = text
	db.set("settings("+serverid+")", str(newdict))
	return "clear"
def set_hi_role(serverid, roleid):
	if data.get("settings("+serverid+")") is None:newdict = {}
	else:newdict = ast.literal_eval(data.get("settings("+serverid+")"))
	newdict["sayhirole"] = roleid
	db.set("settings("+serverid+")", str(newdict))
	return "clear"
def set_bye_text(serverid, text):
	if data.get("settings("+serverid+")") is None:newdict = {}
	else:newdict = ast.literal_eval(data.get("settings("+serverid+")"))
	newdict["saybye"] = text
	db.set("settings("+serverid+")", str(newdict))
	return "clear"
