import requests, json, urllib.request, redis,time,os, ast

db = redis.StrictRedis(decode_responses=True)

try:dict1 = ast.literal_eval(db.get("wiki"))
except: dict1 = {}

def make(title,content, author):
	now = time.localtime()
	s = ""+str(now.tm_year)+"/"+str(now.tm_mon)+"/"+str(now.tm_mday)+" "+str(now.tm_hour)+":"+str(now.tm_min)+":"+str(now.tm_sec)+""
	tmp_list = []
	try:tmp = dict1[title]
	except:	tmp = {}
	tmp_list.append(author)
	tmp["content"] = content
	author_list = []
	author_list.append(author)
	try:
		author_list = tmp["author"] 
		if not author in author_list:
			author_list.append(author)
		tmp["author"] = author_list
	except Exception as e:
		print(e)
		tmp["author"] = author_list
	dict1[title] = tmp
	db.set("wiki", str(dict1))
	file = open("./log/wiki.txt", 'a')
	file.write("["+s+"]\n -문서명:"+title+"\n -문서내용: "+content+"\n -수정자: "+author+"\n -현재 기여자:"+", ".join(tmp["author"])+"\n")
	file.close()
	return tmp["author"]
def find(tag):
	if tag in dict1:
		return dict1[tag]
	else:
		return None
def get():
	return dict1
def delete(title):
	try:
		now = time.localtime()
		s = ""+str(now.tm_year)+"/"+str(now.tm_mon)+"/"+str(now.tm_mday)+" "+str(now.tm_hour)+":"+str(now.tm_min)+":"+str(now.tm_sec)+""
		del dict1[title]
		db.set("wiki", str(dict1))
		file = open("./log/wiki.txt", 'a')
		file.write("["+s+"]\n -문서명:"+title+"\n(데이터 제거)")
		file.close()
		return "clear"
	except:
		return None