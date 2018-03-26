import discord, asyncio, datetime, user, func.logger, func.hypixel, func.util, func.wiki, func.cc, func.warn, ast, os, sys

#데이터 선언
adminlist = user.admin
color = user.embed_color
prefix = user.prefix
prefix_size = len(prefix)
tmp = datetime.datetime.now()
warn = func.warn
logger = func.logger
hypixel = func.hypixel
util = func.util
wiki = func.wiki
cc = func.cc
afklist = []
serverlist = []

#이벤트 부분 / Event Part
class bot(discord.Client):
    async def on_ready(self):
        for i in client.guilds: serverlist.append(i.name)
        print("가동 시작")
        print(user.startmessage)
        await client.change_presence(activity=discord.Streaming(name=user.gametext, url=user.streaming), status=user.status) 
        boot_tm, trash = str((datetime.datetime.now() - tmp)).split(".")
        print("부팅 시간 : "+boot_tm+"")
    async def on_message(self, msg):
        ch = msg.channel
        try:serverid = msg.guild.id
        except:serverid = "dm"
        if msg.author.bot:return
        #메시지 인식부
        if msg.author.id in afklist:
            await ch.send(""+msg.author.mention+"님\n```py\n'돌아 오신것을 환영합니다!```")
            afklist.remove(msg.author.id)
        if not serverid == "dm":
            await cc.on_cc(msg)
            await logger.file(msg)
        else:
            time = datetime.datetime.now()
            time = ""+str(time.year)+"/"+str(time.month)+"/"+str(time.day)+" "+str(time.hour)+":"+str(time.minute)+":"+str(time.second)+""
            context = "["+time+"]"+msg.author.name+"("+msg.author.name+"): "+msg.content+"\n"
            file = open("./log/dm.txt", 'a')
            file.write(context)
            file.close()
        if msg.content.startswith(prefix):
            opt = msg.content[prefix_size:]
            #util
            if opt.startswith("도움"):
                em = discord.Embed(colour=color)
                em.add_field(name="유틸",  value="`"+prefix+"핑`  `"+prefix+"주소단축`  `"+prefix+"번역`  `"+prefix+"맞춤법`  `"+prefix+"위키`  `"+prefix+"명령어`  `"+prefix+"주소단축`  `"+prefix+"잠수`", inline=False)
                em.add_field(name="하이픽셀",value="`"+prefix+"듀얼`  `"+prefix+"uhc`  `"+prefix+"베드워즈`  `"+prefix+"스카이워즈`", inline=False)
                em.add_field(name="관리자",value="`"+prefix+"명령어`  `"+prefix+"지우기`  `"+prefix+"로깅 채널` `"+prefix+"경고` `"+prefix+"지우기` `"+prefix+"채널설정`", inline=False)
                await ch.send(embed=em)
            elif opt.startswith("번역"):
                if not opt == "번역":
                    tmp = opt[3:]
                    res = util.tran(tmp)
                    em = discord.Embed(colour=color)
                    em.add_field(name=""+res["src"]+" > "+res["tar"]+"",  value=""+res["answer"]+"", inline=False)
                    await ch.send(embed=em)
                else:
                    em = discord.Embed(colour=color)
                    em.add_field(name="네이버 번역",  value="```"+prefix+"번역```", inline=False)
                    await ch.send(embed=em)   
                return
            elif opt.startswith("맞춤법"):
                if not opt == "맞춤법":
                    tmp = opt[4:]
                    res = util.wrong(tmp)
                    if not res == None:
                        em = discord.Embed(colour=color)
                        em.add_field(name="네이버 맞춤법확인!",  value=""+res+"", inline=False)
                        await ch.send(embed=em)     
                    else:
                        em = discord.Embed(colour=color)
                        em.add_field(name="네이버 맞춤법확인!",  value="다 맞습니다!", inline=False)
                        await ch.send(embed=em)      
                else:
                    em = discord.Embed(colour=color)
                    em.add_field(name="네이버 맞춤법확인",  value="```"+prefix+"맞춤법```", inline=False)
                    await ch.send(embed=em) 
                return
            elif opt.startswith("서버 리스트"):
                em = discord.Embed(colour=color)
                em.add_field(name="서버 리스트",  value=""+"\n".join(serverlist)+"", inline=False)
                await msg.author.send(embed=em)  
                await ch.send(""+msg.author.mention+"님 DM을 참고하세요! ")
                return
            elif opt.startswith("위키"):
                if opt == "위키":
                    em = discord.Embed(colour=color)
                    em.add_field(name=""+prefix+"위키 리스트",  value="펀크 위키의 문서리스트를 출력합니다.", inline=False)
                    em.add_field(name=""+prefix+"위키 지정 <제목>|<내용>",  value="위키 문서를 지정합니다(기여자에 추가됩니다.)", inline=False)
                    em.add_field(name=""+prefix+"위키 검색 <제목>",  value="위키 문서를 검색합니다.", inline=False)
                    await ch.send(embed=em)
                    return
                if opt.startswith("위키 리스트"):
                    data = wiki.get()   
                    count = str(len(data))
                    liststr = ", ".join(data)
                    em = discord.Embed(colour=color)
                    em.add_field(name="펀크 위키 리스트",  value=""+liststr+"", inline=False)
                    em.set_footer(text="문서의 개수는 "+count+"개 입니다.")
                    await msg.author.send(embed=em)
                    await ch.send(""+msg.author.mention+"님 DM을 보세요!")
                    return
                if opt.startswith("위키 지정"):
                    try:title, content = opt[6:].split("|")
                    except:
                        em = discord.Embed(colour=color)
                        em.add_field(name="문서 지정",  value="```"+prefix+"위키 지정 <제목>|<내용>```\n양식을 따라주세요!", inline=False)
                        await ch.send(embed=em)  
                        return
                    author = wiki.make(title, content, msg.author.name)
                    em = discord.Embed(colour=color)
                    em.add_field(name=""+title+"",  value=""+content+"", inline=False)
                    em.set_footer(text="기여자: "+", ".join(author)+" ")
                    await ch.send(embed=em)  
                    return
                if opt.startswith("위키 검색"):
                    if not opt == "위키 검색":
                        title = opt[6:]
                        data = wiki.find(title)
                        if not data is None:
                            content = data["content"]
                            author = data["author"]
                            em = discord.Embed(colour=color)
                            em.add_field(name=""+title+"",  value=""+content+"", inline=False)
                            em.set_footer(text="기여자: "+", ".join(author)+" ")
                            await ch.send(embed=em) 
                        else:
                            em = discord.Embed(colour=color)
                            em.add_field(name="위키 검색",  value="해당 문서를 찾을수가 없네요..", inline=False)
                            await ch.send(embed=em)
                    else:
                        em = discord.Embed(colour=color)
                        em.add_field(name="문서 검색",  value="```"+prefix+"위키 검색 <제목>```\n양식에 따라주십시오!", inline=False)
                        await ch.send(embed=em)           
                    return
                if opt.startswith("위키 제거"):
                    if not msg.author.id in adminlist: return
                    if not opt == "위키 제거":
                        title = opt[6:]
                        res = wiki.delete(title)
                        if not res == None:
                            em = discord.Embed(colour=color)
                            em.add_field(name="관리자 툴",  value="`"+title.replace("`","")+"`문서를 제거하였습니다.", inline=False)
                            await ch.send(embed=em)
                        else:
                            em = discord.Embed(colour=color)
                            em.add_field(name="관리자 툴",  value="`"+title.replace("`","")+"`문서를 제거하는것에 실패하였습니다.", inline=False)
                            await ch.send(embed=em)
                    else:
                        em = discord.Embed(colour=color)
                        em.add_field(name="문서 제거",  value="```"+prefix+"위키 제거 <제목>```\n양식에 따라주십시오!", inline=False)
                        await ch.send(embed=em)   
                    return
            elif opt.startswith("명령어"):
                if opt == "명령어":
                    em = discord.Embed(colour=color)
                    em.add_field(name=""+prefix+"명령어 리스트",  value="서버 명령어를 출력합니다!", inline=False)
                    em.add_field(name=""+prefix+"명령어 제거 <제목>",  value="서버 명령어를 제거합니다.(관리자용)", inline=False)
                    em.add_field(name=""+prefix+"명령어 지정 <제목>|<반응할값>",  value="서버 명령어를 지정합니다(관리자용)", inline=False)
                    em.add_field(name=""+prefix+"명령어 초기화",  value="서버 명령어를 초기화 합니다.(관리자용)", inline=False)
                    await ch.send(embed=em)  
                    return
                if opt.startswith("명령어 리스트"):
                    cclist = cc.list(str(msg.guild.id))
                    if not cclist is None:
                        outputv = "\n".join(cclist)
                        em = discord.Embed(colour=color)
                        em.add_field(name="명령어 리스트",  value=""+outputv+"", inline=False)
                        await ch.send(embed=em)  
                    else:
                        em = discord.Embed(colour=color)
                        em.add_field(name="명령어 리스트",  value="이 서버에는 추가된 명령어가 없습니다!", inline=False)
                        await ch.send(embed=em)  
                    return
                if(msg.author.guild_permissions.administrator == True or userid in config.adminlist):
                    if opt.startswith("명령어 초기화"):
                        cc.clear(str(msg.guild.id))
                        em = discord.Embed(colour=color)
                        em.add_field(name="명령어 초기화",  value="초기화 완료입니다!", inline=False)
                        await ch.send(embed=em)  
                        return
                    if opt.startswith("명령어 지정"): 
                        if not opt == "명령어 지정":
                            try:
                                inputv, outputv = opt[7:].split("|")
                            except:
                                em = discord.Embed(colour=color)
                                em.add_field(name="명령어 지정",  value="```"+prefix+"명령어 지정 <명령어 제목>|<반응할 말>```", inline=False)
                                await ch.send(embed=em)  
                                return
                            cc.set(str(msg.guild.id), inputv, outputv)   
                            em = discord.Embed(colour=color)
                            em.add_field(name="명령어 지정",  value="`"+inputv.replace("`","")+"` > `"+outputv.replace("`","")+"`", inline=False)
                            await ch.send(embed=em) 
                        else:
                            em = discord.Embed(colour=color)
                            em.add_field(name="명령어 지정",  value="```"+prefix+"명령어 지정 <명령어 제목>|<반응할 말>```", inline=False)
                            await ch.send(embed=em) 
                        return 
                    if opt.startswith("명령어 제거"):
                        if not opt == "명령어 제거":
                            inputv = opt[7:]
                            res = cc.delete(str(msg.guild.id),inputv)
                            if not res is None:
                                em = discord.Embed(colour=color)
                                em.add_field(name="명령어 제거",  value="`"+inputv.replace("`","")+"` 제거 되었습니다!", inline=False)
                                await ch.send(embed=em) 
                            else:
                                em = discord.Embed(colour=color)
                                em.add_field(name="명령어 제거",  value="입력하신 명령어가 없습니다.", inline=False)
                                await ch.send(embed=em) 
                        else:
                            em = discord.Embed(colour=color)
                            em.add_field(name="명령어 제거",  value="```"+prefix+"명령어 제거 <명령어 제목>```", inline=False)
                            await ch.send(embed=em)  
                        return
            elif opt.startswith("로깅 채널"):
                if(msg.author.guild_permissions.administrator == True or userid in config.adminlist):
                    if not opt == "로깅 채널":
                        logch = opt[6:].replace("<", "").replace(">","").replace("#","").replace(" ","")
                        res = await util.set_ch(msg.guild.id, int(logch))
                        if res == True:
                            em = discord.Embed(colour=color)
                            em.add_field(name="로깅 채널",  value=""+opt.replace(opt[6:], "")+" 채널로 로깅 채널이 설정되었습니다.", inline=False)
                            await ch.send(embed=em)     
                        else:
                            em = discord.Embed(colour=color)
                            em.add_field(name="로깅 채널",  value="```"+prefix+"로깅 채널```\n양식에 따르십시오!", inline=False)
                            await ch.send(embed=em)  
                    else:
                        em = discord.Embed(colour=color)
                        em.add_field(name="로깅 채널",  value="```"+prefix+"로깅 채널```\n양식에 따르십시오!", inline=False)
                        await ch.send(embed=em) 
                return
            elif opt.startswith("경고"):
                if opt == "경고":
                    em = discord.Embed(colour=color)
                    em.add_field(name=""+prefix+"경고 추가 @언급",  value="`@언급`한 유저의 경고를 추가합니다.(관리자용)", inline=False)
                    em.add_field(name=""+prefix+"경고 제거 @언급",  value="`@언급`한 유저의 경고를 제거합니다.(관리자용)", inline=False)
                    em.add_field(name=""+prefix+"경고 확인",  value="자신의 경고를 확인합니다.", inline=False)
                    em.add_field(name=""+prefix+"경고 초기화",  value="해당 서버 전체 경고를 초기화 합니다.", inline=False)
                    em.add_field(name=""+prefix+"경고 처벌 <벌>",  value="경고가 한계치에 도달하였을시 내려질 처벌을 선택합니다.(예:`밴`,`킥`)\n(관리자용)", inline=False)
                    em.add_field(name=""+prefix+"경고 한계 <한계치>",  value="경고의 한계치를 지정합니다.(관리자용)", inline=False)
                    return
                if opt.startswith("경고 확인"):
                    res = warn.check(str(msg.guild.id), str(msg.author.id))
                    em = discord.Embed(colour=color)
                    em.add_field(name="경고 확인",  value=""+msg.author.mention+"\n`"+res["status"]+"`/`"+res["high"]+"`", inline=False)
                    em.set_footer(text="경고가 한계치에 도달되면 "+res["yokdo"].replace("kick","킥").replace("ban","밴")+"합니다.")
                    await ch.send(embed=em)  
                    return
                if(msg.author.guild_permissions.administrator == True or userid in config.adminlist):
                    if opt.startswith("경고 추가"):
                        if not opt == "경고 추가":
                            target = opt[6:].replace("@","").replace("!","").replace("<","").replace(">","")
                            try:int(target)
                            except:
                                em = discord.Embed(colour=color)
                                em.add_field(name="경고 추가",  value="```"+prefix+"경고 추가 @언급```\n양식에 따르십시오!", inline=False)
                                await ch.send(embed=em) 
                                return
                            res = warn.warn(str(msg.guild.id), target)
                            if res["do"] is None:
                                em = discord.Embed(colour=color)
                                em.add_field(name="경고 추가",  value=""+opt[6:]+"\n`"+res["warn"]+"`/`"+res["setyok"]+"`", inline=False)
                                await ch.send(embed=em)  
                                return
                            target = msg.guild.get_member(int(target))
                            if res["do"] == "kick":
                                try:await target.kick()
                                except discord.Forbidden: 
                                    em = discord.Embed(colour=color)
                                    em.add_field(name="경고 추가",  value="킥을 실행에는 권한이 너무 낮습니다...", inline=False)
                                    await ch.send(embed=em)  
                                    return
                                em = discord.Embed(colour=color)
                                em.add_field(name="경고 추가",  value=""+opt[6:]+"\n킥입니다.", inline=False)
                                await ch.send(embed=em) 
                            if res["do"] == "ban":
                                try:await target.ban()
                                except discord.Forbidden: 
                                    em = discord.Embed(colour=color)
                                    em.add_field(name="경고 추가",  value="밴을 실행에는 권한이 너무 낮습니다...", inline=False)
                                    await ch.send(embed=em)  
                                    return
                                em = discord.Embed(colour=color)
                                em.add_field(name="경고 추가",  value=""+opt[6:]+"\n밴입니다.", inline=False)
                                await ch.send(embed=em) 
                        else:
                            em = discord.Embed(colour=color)
                            em.add_field(name="경고 추가",  value="```"+prefix+"경고 추가 @언급```\n양식에 따르십시오!", inline=False)
                            await ch.send(embed=em)
                        return 
                    if opt.startswith("경고 제거"):
                        if not opt == "경고 제거":
                            target = opt[6:].replace("@","").replace("!","").replace("<","").replace(">","")
                            try:int(target)
                            except:
                                em = discord.Embed(colour=color)
                                em.add_field(name="경고 제거",  value="```"+prefix+"경고 제거 @언급```\n양식에 따르십시오!", inline=False)
                                await ch.send(embed=em)   
                                return
                            res = warn.clear(str(msg.guild.id), target)
                            if res == "clear":
                                em = discord.Embed(colour=color)
                                em.add_field(name="경고 제거",  value=""+opt.replace(opt[6:], "")+"님의 경고가 초기화 되었습니다", inline=False)
                                await ch.send(embed=em)  
                        else:
                            em = discord.Embed(colour=color)
                            em.add_field(name="경고 제거",  value="```"+prefix+"경고 제거 @언급```\n양식에 따르십시오!", inline=False)
                            await ch.send(embed=em) 
                        return
                    if opt.startswith("경고 처벌"):
                        if not opt =="경고 처벌":
                            mod = opt[6:].replace(" ","")
                            if "킥" in mod:
                                warn.yokdo(str(msg.guild.id), 'kick')
                                em = discord.Embed(colour=color)
                                em.add_field(name="경고 처벌",  value="경고가 한계치에 도달하면\n`킥`입니다.", inline=False)
                                await ch.send(embed=em)     
                            elif "밴" in mod: 
                                warn.yokdo(str(msg.guild.id), 'ban') 
                                em = discord.Embed(colour=color)
                                em.add_field(name="경고 처벌",  value="경고가 한계치에 도달하면\n`밴`입니다.", inline=False)
                                await ch.send(embed=em)     
                            else: 
                                em = discord.Embed(colour=color)
                                em.add_field(name="경고 처벌",  value="```"+prefix+"경고 처벌 <옵션>```\n옵션)`밴`, `킥` ", inline=False)
                                await ch.send(embed=em)  
                        else:
                            em = discord.Embed(colour=color)
                            em.add_field(name="경고 처벌",  value="```"+prefix+"경고 처벌 <옵션>```\n옵션)`밴`, `킥` ", inline=False)
                            await ch.send(embed=em)     
                        return
                    if opt.startswith("경고 한계"):
                        if not opt == "경고 한계":
                            count = opt[6:].replace(" ","")
                            try: count = int(count)
                            except:
                                em = discord.Embed(colour=color)
                                em.add_field(name="경고 한계",  value="```"+prefix+"경고 한계 <한계치>```\n양식을 지켜주세요!", inline=False)
                                await ch.send(embed=em)  
                                return
                            res = warn.setyok(str(msg.guild.id), str(count))
                            if res == "clear":
                                em = discord.Embed(colour=color)
                                em.add_field(name="경고 한계",  value="경고의 한계치는\n`"+str(count)+"`입니다", inline=False)
                                await ch.send(embed=em)                              
                            else:
                                em = discord.Embed(colour=color)
                                em.add_field(name="경고 한계",  value="```"+prefix+"경고 한계 <한계치>```\n양식을 지켜주세요!", inline=False)
                                await ch.send(embed=em)      
                        else:
                            em = discord.Embed(colour=color)
                            em.add_field(name="경고 한계",  value="```"+prefix+"경고 한계 <한계치>```\n양식을 지켜주세요!", inline=False)
                            await ch.send(embed=em)    
                        return
                    if opt.startswith("경고 초기화"):
                        res = warn.allclear(str(msg.guild.id))
                        if res == "clear":
                            em = discord.Embed(colour=color)
                            em.add_field(name="경고 초기화",  value="모든유저의 경고가 초기화 되었습니다.", inline=False)
                            await ch.send(embed=em)  
                        else:
                            em = discord.Embed(colour=color)
                            em.add_field(name="경고 초기화",  value="초기화에 실패하였습니다.", inline=False)
                            await ch.send(embed=em)  
                        return
            elif opt.startswith("주소단축"):
                if not opt == "주소단축":
                    res = util.urlcut(opt[5:])
                    em = discord.Embed(colour=color)
                    em.add_field(name="주소단축",  value=""+res+"", inline=False)
                    await ch.send(embed=em)  
                else:
                    em = discord.Embed(colour=color)
                    em.add_field(name="주소단축",  value="```"+prefix+"주소단축 <주소>```\n양식을 지켜주세요!", inline=False)
                    await ch.send(embed=em)    
                    return
            elif opt.startswith("잠수"):
                if not opt == "잠수":
                    text = opt[3:]
                    em = discord.Embed(colour=color)
                    em.add_field(name="잠수",  value=""+msg.author.mention+"\n"+text+"", inline=False)
                    await ch.send(embed=em)    
                    afklist.append(msg.author.id)
                    return
                else:
                    em = discord.Embed(colour=color)
                    em.add_field(name="잠수",  value="```"+prefix+"잠수 <사유>```\n양식을 지켜주세요!", inline=False)
                    await ch.send(embed=em)    
                    return
            elif opt.startswith("듀얼"):
                if not opt == "듀얼":
                    em = discord.Embed(colour=color)
                    em.add_field(name='듀얼',  value="정보를 불러오고 있습니다!", inline=False)
                    dd = await ch.send(embed=em)
                    value = hypixel.duel(opt[3:])
                    if not value["err"] == "none":
                        if value["err"] == "nostats":
                            em = discord.Embed(colour=color)
                            em.add_field(name='듀얼',  value="해당 플레이어에 대한 정보가 없습니다.```"+prefix+"듀얼 <마인크래프트 닉>```", inline=False)
                            await dd.edit(embed=em)
                            return
                        if value["err"] == "noplayer":
                            em = discord.Embed(colour=color)
                            em.add_field(name='듀얼',  value="그런 유저가 없습니다```"+prefix+" <마인크래프트 닉>```", inline=False)
                            await dd.edit(embed=em)
                            return
                    else:
                        em = discord.Embed(colour=color)
                        em.add_field(name='최고 연승',  value="**스카이워즈 듀얼**\n`"+value["duel_sw"]+"`\n**노 디버프**\n`"+value["duel_potion"]+"`\n**콤보 듀얼**\n`"+value["duel_combo"]+"`\n**UHC 듀얼**\n`"+value["duel_uhc"]+"`", inline=True)
                        em.add_field(name='총킬',  value="`"+value["duel_kill"]+"`", inline=False)
                        em.add_field(name='총 우승',  value="`"+value["duel_win"]+"`", inline=False)
                        em.add_field(name='총 패배',  value="`"+value["duel_lose"]+"`", inline=False)
                        em.add_field(name='총 데스',  value="`"+value["duel_death"]+"`", inline=False)
                        em.set_thumbnail(url=value["avatar"])
                        await dd.edit(embed=em)
                else:
                    em = discord.Embed(colour=color)
                    em.add_field(name='듀얼',  value="```"+prefix+"듀얼 <마크닉>```", inline=False)
                    await ch.send(embed=em)
            elif opt.startswith("uhc"):
                if not opt == "uhc":
                    em = discord.Embed(colour=color)
                    em.add_field(name='uhc',  value="정보를 불러오고 있습니다!", inline=False)
                    dd = await ch.send(embed=em)
                    value = hypixel.uhc(opt[4:])
                    if not value["err"] == "none":
                        if value["err"] == "nostats":
                            em = discord.Embed(colour=color)
                            em.add_field(name='uhc',  value="해당 플레이어에 대한 정보가 없습니다.```"+prefix+"uhc <마인크래프트 닉>```", inline=False)
                            await dd.edit(embed=em)
                            return
                        if value["err"] == "noplayer":
                            em = discord.Embed(colour=color)
                            em.add_field(name='uhc',  value="그런 유저가 없습니다```"+prefix+"uhc <마인크래프트 닉>```", inline=False)
                            await dd.edit(embed=em)
                            return
                    else:
                        em = discord.Embed(colour=color)
                        em.add_field(name='코인',  value="`"+value["uhc_coin"]+"`", inline=False)
                        em.add_field(name='총 우승',  value="`"+value["uhc_win"]+"`", inline=False)
                        em.add_field(name='자주쓰는 킷',  value="`"+value["uhc_kit"]+"`", inline=False)
                        em.add_field(name='총 데스',  value="`"+value["uhc_death"]+"`", inline=False)
                        em.add_field(name='총 킬',  value="`"+value["uhc_kill"]+"`", inline=False)
                        em.add_field(name='패키지 개수',  value="`"+value["uhc_package"]+"`", inline=False)
                        em.add_field(name='점수',  value="`"+value["uhc_score"]+"`", inline=False)
                        em.set_thumbnail(url=value["avatar"])
                        await dd.edit(embed=em)
                else:
                    em = discord.Embed(colour=color)
                    em.add_field(name='uhc',  value="```"+prefix+"uhc <마크닉>```", inline=False)
                    await ch.send(embed=em)     
            elif opt.startswith("베드워즈"):
                if not opt == "베드워즈":
                    em = discord.Embed(colour=color)
                    em.add_field(name='베드워즈',  value="정보를 불러오고 있습니다!", inline=False)
                    dd = await ch.send(embed=em)
                    value = hypixel.bedwars(opt[5:])
                    if not value["err"] == "none":
                        if value["err"] == "nostats":
                            em = discord.Embed(colour=color)
                            em.add_field(name='베드워즈',  value="해당 플레이어에 대한 정보가 없습니다.```"+prefix+"베드워즈 <마인크래프트 닉>```", inline=False)
                            await dd.edit(embed=em)
                            return
                        if value["err"] == "noplayer":
                            em = discord.Embed(colour=color)
                            em.add_field(name='베드워즈',  value="그런 유저가 없습니다```"+prefix+"베드워즈 <마인크래프트 닉>```", inline=False)
                            await dd.edit(embed=em)
                            return
                    else:
                        em = discord.Embed(colour=color)
                        em.add_field(name='킬',  value="총:"+value["Bedwars_kill"]+"\n-솔로:"+value["Bedwars_kill_1v"]+" 더블:"+value["Bedwars_kill_2v"]+"\n-3v:"+value["Bedwars_kill_3v"]+" 4v:"+value["Bedwars_kill_4v"]+"", inline=True)
                        em.add_field(name='데스',  value="총:"+value["Bedwars_death"]+"\n-솔로:"+value["Bedwars_death_1v"]+" 더블:"+value["Bedwars_death_2v"]+"\n-3v:"+value["Bedwars_death_3v"]+" 4v:"+value["Bedwars_death_4v"]+"", inline=True)
                        em.add_field(name='우승',  value="총:"+value["Bedwars_win"]+"\n-솔로:"+value["Bedwars_win_1v"]+" 더블:"+value["Bedwars_win_2v"]+"\n-3v:"+value["Bedwars_win_3v"]+" 4v:"+value["Bedwars_win_4v"]+"", inline=True)
                        em.add_field(name='패배',  value="총:"+value["Bedwars_lose"]+"\n-솔로:"+value["Bedwars_lose_1v"]+" 더블:"+value["Bedwars_lose_2v"]+"\n-3v:"+value["Bedwars_lose_3v"]+" 4v:"+value["Bedwars_lose_4v"]+"", inline=True)
                        em.add_field(name='기타',  value="코인:"+value["Bedwars_coin"]+"\n레벨:"+value["Bedwars_level"]+"", inline=True)
                        em.set_thumbnail(url=value["avatar"])
                        await dd.edit(embed=em)
                else:
                    em = discord.Embed(colour=color)
                    em.add_field(name='베드워즈',  value="```"+prefix+"베드워즈 <마크닉>```", inline=False)
                    await ch.send(embed=em)
            elif opt.startswith("스카이워즈"):
                if not opt == "스카이워즈":
                    em = discord.Embed(colour=color)
                    em.add_field(name='스카이워즈',  value="정보를 불러오고 있습니다!", inline=False)
                    dd = await ch.send(embed=em)
                    value = hypixel.skywars(opt[6:])
                    if not value["err"] == "none":
                        if value["err"] == "nostats":
                            em = discord.Embed(colour=color)
                            em.add_field(name='스카이워즈',  value="해당 플레이어에 대한 정보가 없습니다.```"+prefix+"스카이워즈 <마인크래프트 닉>```", inline=False)
                            await dd.edit(embed=em)
                            return
                        if value["err"] == "noplayer":
                            em = discord.Embed(colour=color)
                            em.add_field(name='스카이워즈',  value="그런 유저가 없습니다```"+prefix+"스카이워즈 <마인크래프트 닉>```", inline=False)
                            await dd.edit(embed=em)
                            return
                    else:
                        em = discord.Embed(colour=color)
                        em.add_field(name='킬',  value="총:"+value["SkyWars_kill"]+"\n-솔로:"+value["SkyWars_kill_solo"]+" 팀:"+value["SkyWars_kill_team"]+"\n-메가:"+value["SkyWars_kill_mega"]+" 랭크:"+value["SkyWars_kill_ranked"]+"", inline=True)
                        em.add_field(name='데스',  value="총:"+value["SkyWars_death"]+"\n-솔로:"+value["SkyWars_death_solo"]+" 팀:"+value["SkyWars_death_team"]+"\n-메가:"+value["SkyWars_death_mega"]+" 랭크:"+value["SkyWars_death_ranked"]+"", inline=True)
                        em.add_field(name='우승',  value="총:"+value["SkyWars_win"]+"\n-솔로:"+value["SkyWars_win_solo"]+" 팀:"+value["SkyWars_win_team"]+"\n-메가:"+value["SkyWars_win_mega"]+" 랭크:"+value["SkyWars_win_ranked"]+"", inline=True)          
                        em.add_field(name='패배',  value="총:"+value["SkyWars_lose"]+"\n-솔로:"+value["SkyWars_lose_solo"]+" 팀:"+value["SkyWars_lose_team"]+"\n-메가:"+value["SkyWars_lose_mega"]+" 랭크:"+value["SkyWars_lose_ranked"]+"", inline=True)
                        em.add_field(name='기타',  value="코인:"+value["SkyWars_coin"]+"\n킷 개수:"+value["SkyWars_kit"]+" ", inline=False)
                        em.set_thumbnail(url=value["avatar"])
                        em.set_footer(text="랭크 레이팅은 하픽이 정보제공을 하지 않습니다..")
                        await dd.edit(embed=em)
                else:
                    em = discord.Embed(colour=color)
                    em.add_field(name='스카이워즈',  value="```"+prefix+"스카이워즈 <마크 닉네임>```", inline=True)
                    await ch.send(embed=em)
            elif opt.startswith("지우기"):
                if(msg.author.guild_permissions.administrator == True or userid in config.adminlist):
                    if not opt == "지우기":
                        mgs = []
                        try:                
                            limit = int(opt[4:])
                            if limit > 100:
                                em = discord.Embed(colour=color)
                                em.add_field(name="지우기",  value="100개 이상은 삭제 할수없습니다.", inline=True)
                                await ch.send(embed=em) 
                                return
                        except:
                            em = discord.Embed(colour=color)
                            em.add_field(name="지우기",  value="숫자를 넣으세요\n```"+prefix+".지우기 <지울 메시지 수>```", inline=True)
                            await ch.send(embed=em)
                            return
                        try:
                            async for x in msg.channel.history(limit=limit):
                                mgs.append(x)
                            await ch.delete_messages(mgs)       
                            await ch.send('삭제 완료입니다!!', delete_after = 2.5)     
                        except:
                            await ch.send('14일이 넘은 메시지는 삭제가 불가능합니다!', delete_after = 2.5)
                        return
                else:
                    em = discord.Embed(colour=color)
                    em.add_field(name="지우기",  value="숫자를 넣으세요\n```"+prefix+".지우기 <지울 메시지 수>```", inline=True)
                    await ch.send(embed=em)
                    return
            elif opt.startswith("채널설정"):
                if(msg.author.guild_permissions.administrator == True or userid in config.adminlist):
                    if not opt == "채널설정":
                        tarch = opt[5:].replace("<","").replace(">","").replace("#","").replace("!","")
                        try:int(tarch)
                        except:
                            em = discord.Embed(colour=color)
                            em.add_field(name="채널설정",  value="```"+prefix+"채널설정 #채널```\n양식을 따라주세요!", inline=True)
                            await ch.send(embed=em)
                            return    
                        res = util.set_notice_ch(str(msg.guild.id),tarch) 
                        if res == "clear":
                            em = discord.Embed(colour=color)
                            em.add_field(name="채널설정",  value=""+opt[5:]+"로 채널이 지정되었습니다.", inline=True)
                            em.set_footer(text="위의 채널로 공지가 발송됩니다!")
                            await ch.send(embed=em)
                            return    
                        else:
                            em = discord.Embed(colour=color)
                            em.add_field(name="채널설정",  value="```"+prefix+"채널설정 #채널```\n양식을 따라주세요!", inline=True)
                            await ch.send(embed=em)
                            return  
                    else:
                        em = discord.Embed(colour=color)
                        em.add_field(name="채널설정",  value="```"+prefix+"채널설정 #채널```\n양식을 따라주세요!", inline=True)
                        await ch.send(embed=em)
                        return  
            #측정
            elif opt.startswith("핑"):
                trash, time = str((datetime.datetime.utcnow() - msg.created_at)).split(".")
                time = time[0:3]
                await ch.send(""+msg.author.mention+":ping_pong: `"+time+"`ms!")
                return
            #Bot_Admin_command
            elif opt.startswith("백업"):
                if msg.author.id in adminlist:
                    await msg.author.send(file=discord.File("./log/wiki.txt"))
                    await msg.author.send(file=discord.File("./log/dm.txt"))
                    file = open("./log/wiki_data.txt","a"); file.write(str(wiki.get()));await msg.author.send(file=discord.File("./log/wiki_data.txt"))
                    await msg.author.send(file=discord.File("./run.py"))
                    await msg.author.send(file=discord.File("./user.py"))
                    await ch.send("DM 보세요. "+msg.author.mention+" ")
                    return
            elif opt.startswith("공지"):
                if msg.author.id in adminlist:
                    context = opt[3:]
                    res = await util.notice(context, client)
                    await ch.send("공지가 간 채널 개수 : "+str(res)+"")
                    return
            elif opt.startswith("재시작"):
                if msg.author.id in adminlist:
                    await ch.send("재시작 합니다")
                    os.execl(sys.executable, sys.executable, * sys.argv)
            elif opt.startswith("종료"):
                if msg.author.id in adminlist:
                    await ch.send("종료합니다!")
                    await client.close()
            else:
                await ch.send("그런말은 없어요!\n`"+prefix+"도움`")
    async def on_message_edit(self, bmsg, msg):
        try:serverid = msg.guild.id
        except:serverid = "dm"
        if not serverid == "dm":
            await logger.edit_log(bmsg, msg)
        else:
            time = datetime.datetime.now()
            time = ""+str(time.year)+"/"+str(time.month)+"/"+str(time.day)+" "+str(time.hour)+":"+str(time.minute)+":"+str(time.second)+""
            context = "["+time+"]"+msg.author.name+"("+msg.author.name+"): "+bmsg.content+" > "+msg.content+"\n"
            file = open("./log/dm.txt", 'a')
            file.write(context)
            file.close()    
        if msg.author.id in afklist:
            await msg.channel.send(""+msg.author.mention+"님\n```py\n'돌아 오신것을 환영합니다!```")
            afklist.remove(msg.author.id)
    async def on_raw_bulk_message_delete(self, msglist, ch):
        try:serverid = client.get_channel(ch).guild.id
        except:serverid = "dm"
        if not serverid == "dm":
            await logger.del_bulk_log(msglist, ch)
    async def on_message_delete(self, msg):
        try:serverid = msg.guild.id
        except:serverid = "dm"
        if not serverid == "dm":
            await logger.del_log(msg)
        else:
            time = datetime.datetime.now()
            time = ""+str(time.year)+"/"+str(time.month)+"/"+str(time.day)+" "+str(time.hour)+":"+str(time.minute)+":"+str(time.second)+""
            context = "["+time+"]"+msg.author.name+"("+msg.author.name+"): <삭제>"+msg.content+"\n"
            file = open("./log/dm.txt", 'a')
            file.write(context)
            file.close()    
        if msg.author.id in afklist:
            await msg.channel.send(""+msg.author.mention+"님\n```py\n'돌아 오신것을 환영합니다!```")
            afklist.remove(msg.author.id)

#실행 부분 / Run Part
client = bot()
logger.settings(color, client)
client.run(user.token) 