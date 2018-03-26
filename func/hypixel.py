import requests, json

hypixapi = "d5be9c7d-dc6b-4456-ad76-0374bc4278dd"
link = "https://api.hypixel.net/player?key="+hypixapi+"&name="

def skywars(nick):	
	r = requests.get(link + nick)
	hypixeljson = json.loads(r.content.decode("UTF-8"))
	rls = {}
	if hypixeljson["player"] is None:
		rls["err"] = "noplayer"
		return rls
	try:
		SkyWars = hypixeljson["player"]["stats"]["SkyWars"]
	except:
		rls["err"] = "nostats"
		return rls
	try:SkyWars_kill = str(SkyWars["kills"])
	except:SkyWars_kill = "0"
	try:SkyWars_kill_solo = str(SkyWars["kills_solo"])
	except:SkyWars_kill_solo = "0"
	try:SkyWars_kill_team = str(SkyWars["kills_team"])
	except:SkyWars_kill_team = "0"
	try:SkyWars_kill_mega = str(SkyWars["kills_mega"])
	except:SkyWars_kill_mega = "0"
	try:SkyWars_kill_ranked = str(SkyWars["kills_ranked"])
	except:SkyWars_kill_ranked = "0"
	try:SkyWars_death = str(SkyWars["deaths"])
	except:SkyWars_death = "0"
	try:SkyWars_death_solo = str(SkyWars["deaths_solo"])
	except:SkyWars_death_solo = "0"
	try:SkyWars_death_team = str(SkyWars["deaths_team"])
	except:SkyWars_death_team = "0"
	try:SkyWars_death_mega = str(SkyWars["deaths_mega"])
	except:SkyWars_death_mega = "0"
	try:SkyWars_death_ranked = str(SkyWars["deaths_ranked"])
	except:SkyWars_death_ranked = "0"
	try:SkyWars_win = str(SkyWars["wins"])
	except:SkyWars_win = "0"
	try:SkyWars_win_solo = str(SkyWars["wins_solo"])
	except:SkyWars_win_solo = "0"
	try:SkyWars_win_team = str(SkyWars["wins_team"])
	except:SkyWars_win_team = "0"
	try:SkyWars_win_mega = str(SkyWars["wins_mega"])
	except:SkyWars_win_mega = "0"
	try:SkyWars_win_ranked = str(SkyWars["wins_ranked"])
	except:SkyWars_win_ranked = "0"
	try:SkyWars_lose = str(SkyWars["losses"])
	except:SkyWars_lose = "0"
	try:SkyWars_lose_solo = str(SkyWars["losses_solo"])
	except:SkyWars_lose_solo = "0"
	try:SkyWars_lose_team = str(SkyWars["losses_team"])
	except:SkyWars_lose_team = "0"
	try:SkyWars_lose_mega = str(SkyWars["losses_mega"])
	except:SkyWars_lose_mega = "0"
	try:SkyWars_lose_ranked = str(SkyWars["losses_ranked"])
	except:SkyWars_lose_ranked = "0"
	try:SkyWars_kit = str(len(SkyWars["packages"]))
	except:SkyWars_kit = "0"
	try:SkyWars_coin = str(SkyWars["coins"])
	except:SkyWars_coin = "0"
	avatar = "https://crafatar.com/renders/body/"+hypixeljson["player"]["uuid"]+"?size=10&default=MHF_Steve&overlay&scale=10"
	rls["err"] = "none"
	rls["SkyWars_kill"] = SkyWars_kill
	rls["SkyWars_lose"] = SkyWars_lose
	rls["SkyWars_kill_solo"] = SkyWars_kill_solo
	rls["SkyWars_kill_team"] = SkyWars_kill_team
	rls["SkyWars_kill_mega"] = SkyWars_kill_mega
	rls["SkyWars_kill_ranked"] = SkyWars_kill_ranked
	rls["SkyWars_death"] = SkyWars_death
	rls["SkyWars_death_solo"] = SkyWars_death_solo
	rls["SkyWars_death_team"] = SkyWars_death_team
	rls["SkyWars_death_mega"] = SkyWars_death_mega
	rls["SkyWars_death_ranked"] = SkyWars_death_ranked
	rls["SkyWars_win"] = SkyWars_win
	rls["SkyWars_win_solo"] = SkyWars_win_solo
	rls["SkyWars_win_team"] = SkyWars_win_team
	rls["SkyWars_win_mega"] = SkyWars_win_mega
	rls["SkyWars_win_ranked"] = SkyWars_win_ranked
	rls["SkyWars_lose_solo"] = SkyWars_lose_solo
	rls["SkyWars_lose_team"] = SkyWars_lose_team
	rls["SkyWars_lose_mega"] = SkyWars_lose_mega
	rls["SkyWars_lose_ranked"] = SkyWars_lose_ranked
	rls["SkyWars_kit"] = SkyWars_kit
	rls["SkyWars_coin"] = SkyWars_coin
	rls["avatar"] = avatar
	return(rls)
def bedwars(nick):
	r = requests.get(link + nick)
	hypixeljson = json.loads(r.content.decode("UTF-8"))
	rls = {}
	if hypixeljson["player"] is None:
		rls["err"] = "noplayer"
		return rls
	try:
		Bedwars = hypixeljson["player"]["stats"]["Bedwars"]
	except:
		rls["err"] = "nostats"
		return rls
	try:Bedwars_death_4v = str(Bedwars["four_four_deaths_bedwars"])
	except:Bedwars_death_4v = "0"
	try:Bedwars_kill_4v = str(Bedwars["four_four_kills_bedwars"])
	except:Bedwars_kill_4v = "0"
	try:Bedwars_win_4v = str(Bedwars["four_four_wins_bedwars"])
	except:Bedwars_win_4v = "0"
	try:Bedwars_lose_4v = str(Bedwars["four_four_losses_bedwars"])
	except:Bedwars_lose_4v = "0"
	try:Bedwars_death_2v = str(Bedwars["eight_two_deaths_bedwars"])
	except:Bedwars_death_2v = "0"
	try:Bedwars_kill_2v = str(Bedwars["eight_two_kills_bedwars"])
	except:Bedwars_kill_2v = "0"
	try:Bedwars_win_2v = str(Bedwars["eight_two_wins_bedwars"])
	except:Bedwars_win_2v = "0"
	try:Bedwars_lose_2v = str(Bedwars["eight_two_losses_bedwars"])
	except:Bedwars_lose_2v = "0"
	try:Bedwars_death_1v = str(Bedwars["eight_one_deaths_bedwars"])
	except:Bedwars_death_1v = "0"
	try:Bedwars_kill_1v = str(Bedwars["eight_one_kills_bedwars"])
	except:Bedwars_kill_1v = "0"
	try:Bedwars_win_1v = str(Bedwars["eight_one_wins_bedwars"])
	except:Bedwars_win_1v = "0"
	try:Bedwars_lose_1v = str(Bedwars["eight_one_losses_bedwars"])
	except:Bedwars_lose_1v = "0"
	try:Bedwars_death_3v = str(Bedwars["four_three_deaths_bedwars"])
	except:Bedwars_death_3v = "0"
	try:Bedwars_kill_3v = str(Bedwars["four_three_kills_bedwars"])
	except:Bedwars_kill_3v = "0"
	try:Bedwars_win_3v = str(Bedwars["four_three_wins_bedwars"])
	except:Bedwars_win_3v = "0"
	try:Bedwars_lose_3v = str(Bedwars["four_three_losses_bedwars"])
	except:Bedwars_lose_3v = "0"
	try:Bedwars_lose = str(Bedwars["losses_bedwars"])
	except:Bedwars_lose = "0"
	try:Bedwars_win = str(Bedwars["wins_bedwars"])
	except:Bedwars_win = "0"
	try:Bedwars_death = str(Bedwars["deaths_bedwars"])
	except:Bedwars_death = "0"
	try:Bedwars_kill = str(Bedwars["kills_bedwars"])
	except:Bedwars_kill = "0"
	try:Bedwars_level = str(hypixeljson["player"]["achievements"]["bedwars_level"])
	except:Bedwars_level = "0"
	try:Bedwars_coin = str(Bedwars["coins"])
	except:Bedwars_coin = "0"
	avatar = "https://crafatar.com/renders/body/"+hypixeljson["player"]["uuid"]+"?size=10&default=MHF_Steve&overlay&scale=10"
	rls["Bedwars_death_4v"] = Bedwars_death_4v
	rls["Bedwars_kill_4v"] = Bedwars_kill_4v
	rls["Bedwars_win_4v"] = Bedwars_win_4v
	rls["Bedwars_lose_4v"] = Bedwars_lose_4v
	rls["Bedwars_death_2v"] = Bedwars_death_2v
	rls["Bedwars_kill_2v"] = Bedwars_kill_2v
	rls["Bedwars_win_2v"] = Bedwars_win_2v
	rls["Bedwars_lose_2v"] = Bedwars_lose_2v
	rls["Bedwars_death_1v"] = Bedwars_death_1v
	rls["Bedwars_kill_1v"] = Bedwars_kill_1v
	rls["Bedwars_win_1v"] = Bedwars_win_1v
	rls["Bedwars_lose_1v"] = Bedwars_lose_1v
	rls["Bedwars_death_3v"] = Bedwars_death_3v
	rls["Bedwars_kill_3v"] = Bedwars_kill_3v
	rls["Bedwars_win_3v"] = Bedwars_win_3v
	rls["Bedwars_lose_3v"] = Bedwars_lose_3v
	rls["Bedwars_lose"] = Bedwars_lose
	rls["Bedwars_win"] = Bedwars_win
	rls["Bedwars_death"] = Bedwars_death
	rls["Bedwars_kill"] = Bedwars_kill
	rls["Bedwars_level"] = Bedwars_level
	rls["Bedwars_coin"] = Bedwars_coin
	rls["avatar"] = avatar
	rls["err"] = "none"
	return rls
def duel(nick):
	r = requests.get(link + nick)
	hypixeljson = json.loads(r.content.decode("UTF-8"))
	rls = {}
	if hypixeljson["player"] is None:
		rls["err"] = "noplayer"
		return rls
	try:
		duel = hypixeljson["player"]["stats"]["Duels"]
	except:
		rls["err"] = "nostats"
		return rls
	try:duel_kill = str(duel["kills"])
	except:duel_kill = "0"
	try:duel_win = str(duel["wins"])
	except:duel_win = "0"
	try:duel_lose = str(duel["losses"])
	except:duel_lose = "0"
	try:duel_death = str(duel["deaths"])
	except:duel_death = "0"
	try:duel_sw = str(duel["duels_winstreak_best_sw_duel"])
	except:duel_sw = "0"
	try:duel_potion = str(duel["duels_winstreak_best_potion_duel"])
	except:duel_potion = "0"
	try:duel_combo = str(duel["duels_winstreak_best_combo_duel"])
	except:duel_combo = "0"
	try:duel_uhc = str(duel["duels_winstreak_best_uhc_duel"])
	except:duel_uhc = "0"
	avatar = "https://crafatar.com/renders/body/"+hypixeljson["player"]["uuid"]+"?size=10&default=MHF_Steve&overlay&scale=10"
	rls["avatar"] = avatar
	rls["duel_kill"] = duel_kill
	rls["duel_win"] = duel_win
	rls["duel_lose"] = duel_lose
	rls["duel_death"] = duel_death
	rls["duel_sw"] = duel_sw
	rls["duel_potion"] = duel_potion
	rls["duel_combo"] = duel_combo
	rls["duel_uhc"] = duel_uhc
	rls["err"] = "none"
	return rls
def uhc(nick):
	r = requests.get(link + nick)
	hypixeljson = json.loads(r.content.decode("UTF-8"))
	rls = {}
	if hypixeljson["player"] is None:
		rls["err"] = "noplayer"
		return rls
	try:
		uhc = hypixeljson["player"]["stats"]["UHC"]
	except:
		rls["err"] = "nostats"
		return rls
	rls["err"] = "none"
	try:uhc_coin = str(uhc["coins"])
	except:uhc_coin = "0"
	try:uhc_win = str(uhc["wins"])
	except:uhc_win = "0"
	try:uhc_kit = uhc["equippedKit"]
	except:uhc_kit = "정보 없음"
	try:uhc_death = str(uhc["deaths"])
	except:uhc_death ="0"
	try:uhc_kill = str(uhc["kills"])
	except:uhc_kill = "0"
	try:uhc_package = str(len(uhc["packages"]))
	except:uhc_package = "0"
	try:uhc_score = str(uhc["score"])
	except:uhc_score = "0"
	rls["uhc_coin"] = uhc_coin
	rls["uhc_win"] = uhc_win
	rls["uhc_kit"] = uhc_kit
	rls["uhc_death"] = uhc_death
	rls["uhc_kill"] = uhc_kill
	rls["uhc_package"] = uhc_package
	rls["uhc_score"] = uhc_score
	avatar = "https://crafatar.com/renders/body/"+hypixeljson["player"]["uuid"]+"?size=10&default=MHF_Steve&overlay&scale=10"
	rls["avatar"] = avatar
	return rls

