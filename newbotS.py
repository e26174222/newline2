# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob


cl = LINETCR.LINE()
cl.login(token="EmUXn15KmOSBBeWTHH5f.FyCqvzVAe2RNaWr3/dbP3W.7TNK8NtczfuM2PAPEOIqkd/ytglLi/jyEpm7Ntq7OkY=")
cl.loginResult()

ad = LINETCR.LINE()
ad.login(token="Emtxa1xy0AMhXiEHKAP5.iur748Us1jyfpKv4oxGLDq.EkqBjvk6FS5UCqXHO5AP5WV+Eyxn163JDJGEvlphEMM=")
ad.loginResult()

ki = LINETCR.LINE()
ki.login(token="EmMw4ER2O2fvKUSzEsBa.PzuIGrSfbi6ZimWr5ex5QG.syYDPY2/FKnscrl3eAMV0bGmvnZIjh0J77//M9TYAEo=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="Eml9pcYgeFQNUt807bAf.DRgr2cTxeEiDATETLgm6FW.y/+yTmIXYQW54JtE6J9mE+HzQWWTlrh+bCIMg85NqHI=")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token="EmcQv9uVyz1qfXD5wkK0.0xXKLPaf8b6wAiXZDw/zKa.hITnbZp2CFzFxxVxBFgLT8j/BpGE0W2FfoC61MAI2u8=")
kc.loginResult()

kd = LINETCR.LINE()
kd.login(token="EmsAClk8V7wajdfnd3t2.c74e1FIgViqAn7KTUdEVWG.MupOxn+eaf37ULYh9n6TaZnkBwXWicyaTn3aZy3TVaw=")
kd.loginResult()

ke = LINETCR.LINE()
ke.login(token="Em9XjiXjoIGpjWWUtvbc.fDEuyTzDGQmGfp4ckPUkpa.+kgPaOeMIa8xn+7HsQ2urGm+m3R583MCNVzp2pOCURg=")
ke.loginResult()

kf = LINETCR.LINE()
kf.login(token="EmJY82NxgH1R8v5Za499.jnrl5WXaTf6U4igiiB7LEq.DQvYUfRcv8XjJFfGyRapknKxR4a2KArPMgOyaVEfe14=")
kf.loginResult()

kg = LINETCR.LINE()
kg.login(token="EmJmSdILELDoKwCdwlz9.e1FgUhH3JoxZEfGo0PR5Aq.EDQZCGlfUrNSdsLVUfD1S+xLKWqCGpwyLiJemJjZ3zo=")
kg.loginResult()

kh = LINETCR.LINE()
kh.login(token="EmfuVR8Bqx5W941oxLy7.iDoQGqR5vJevZClhLwopPW.p6dQMnn51VOX+jZ8resNa8Um2POW0qJDCNKo+ADtoec=")
kh.loginResult()

kj = LINETCR.LINE()
kj.login(token="EmJtZKOBCDENmNZYZuB4.sumo+F0V0TIBr+nNrlJgna.35WSsKaujEfZKML1iyMIAJf9eEkhoN4Wwj/SN3ifjWA=")
kj.loginResult()

kl = LINETCR.LINE()
kl.login(token="EmDYYHfLm2MgzaDU8Je1.3QcCJv4kHUj+58p8vc5viq.IGUJpvgLq9JiHSsgtO6iZMoctX3wuzFVJHncsrMHkvM=")
ki.loginResult()

kn = LINETCR.LINE()
kn.login(token="Emjt3hPSHGsBMFDjQ6l0.0tGK0m6LMWuegE+xHNjzKa.rcrrzi7OuwCZX10EMwVlvo4MALmjsK1xZaP5mw1w9Jg=")
kn.loginResult()


print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""[Help 不給看勒]"""
KAC=[cl,ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,kn]
admid = ad.getProfile().mid
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Fmid = kf.getProfile().mid
Gmid = kg.getProfile().mid
Hmid = kh.getProfile().mid
Jmid = kj.getProfile().mid
Lmid = kl.getProfile().mid
Nmid = kn.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Jmid,Lmid,Nmid,admid]
Bots2=[Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Jmid,Lmid,Nmid,admid]
admin = ["u67c43239c865dfce6addb41c6b3c0edd","u29971676114806a574c148f0df876c22","u24d44be70c40b45eaee0818821bee579","u21447be3cb92d496053e457839782575","u76b191d82b5711e21d6ad7ad94633a7f","u15d79462d65d82a32014fe022a9b8a3c","ud17c64969005f01e96688c73756f9990","u0bbe04d5f886bc841a37b92db837afc2","u67c43239c865dfce6addb41c6b3c0edd","u7d8710559bda136ae7030477f83069df","u1357c6b878778ce5f378580ed29af969","u21d3aa810af9563115cdc2c795638fa7","u49430efdfd2fd2d89b47f36744b8c634","ud13824d0cea59b050419efd786725990"]
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []

Administrator = admin
wait = {
    'protect':False,
    'protectinv':False,
    'protectqr':False,
    'contact':False,
    'autoJoin':True,
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':True,
    'message':"詞語Bot\nAutboLike\nhttp://line.me/ti/p/~fang_xin\nhttp://line.me/ti/p/~.90.11.24.",
    "lang":"JP",
    "comment":"http://line.me/ti/p/~fang_xin\nAuto like By fung xin 放芯",
    "likeOn":True,
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "msge":True,
    "clock":True,
    "blacklist":{},
    "P":True,
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":False,
    "pro":{},
    "pname":{},
    "pro_name":{},    
    "pinv":{},
    "purl":{},
    "atjointicket":True,
    "string":"Boter",
    "kickme":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}

cancelinvite = {
    'autoCancel':False
}

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def bot(op):
    try:
        msg = op.message
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = kd.getGroup(op.param1)
				    except:
					try:
                                            G = ke.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        kd.updateGroup(G)
                                    except:
                                        try:
                                            ke.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                            
                                        cl.sendText(op.param1,"群名已鎖")
                                        cl.sendText(op.param1,"更改者為")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
        if op.param3 == "4":
            if op.param1 in wait["purl"]:
                OWN = admin + Bots
                if op.param2 in OWN:
                    pass
                elif wait["P"] == True:
				     group = cl.getGroup(op.param1)
				     if group.preventJoinByTicket == False:
					     group.preventJoinByTicket = True
					     cl.updateGroup(group)
					     cl.sendText(op.param1,"---[不能亂開網址哦]---")
				     else:
					     pass                
        if op.type == 0:
            return 
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"完成")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"完成")
                        print "SUKSES -- BLACKLIST DITAMBAHKAN"

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"已刪除")
                        print "SUKSES -- BLACKLIST DIHAPUS"
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"沒有在黑單中")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return

            elif msg.text in ["help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    print "SUKSES -- KEYWORD"
                    cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                  if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                    print "SUKSES -- CHANGE NAME GROUP"
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Raye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Bye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Aye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ad.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Iye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Kye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kk.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Cye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kc.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Dye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kd.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Eye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ke.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Fye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kf.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Gye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kg.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Hye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kh.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Jye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kj.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Lye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif ("Nye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kn.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "AdKick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("AdKick ","")
                ad.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KiKick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KiKick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "KkKick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KkKick ","")
                kk.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KcKick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KcKick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "KdKick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KdKick ","")
                kd.kickoutFromGroup(msg.to,[midd])
            elif "KeKick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KeKick ","")
                ke.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KfKick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KfKick ","")
                kf.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KgKick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KgKick ","")
                kg.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KhKick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KhKick ","")
                kh.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KjKick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KjKick ","")
                kj.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KlKick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KlKick ","")
                kl.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KnKick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KnKick ","")
                kn.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                ad.findAndAddContactsByMid(midd)
                ad.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "AdInvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("AdInvite ","")
                ad.findAndAddContactsByMid(midd)
                ad.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KiInvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KiInvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KkInvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KkInvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KcInvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KcInvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KdInvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KdInvite ","")
                kd.findAndAddContactsByMid(midd)
                kd.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KeInvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KeInvite ","")
                ke.findAndAddContactsByMid(midd)
                ke.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KfInvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KfInvite ","")
                kf.findAndAddContactsByMid(midd)
                kf.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"         
            elif "KgInvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KgInvite ","")
                kg.findAndAddContactsByMid(midd)
                kg.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KhInvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KhInvite ","")
                kh.findAndAddContactsByMid(midd)
                kh.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KjInvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KjInvite ","")
                kj.findAndAddContactsByMid(midd)
                kj.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KlInvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KlInvite ","")
                kl.findAndAddContactsByMid(midd)
                kl.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KnInvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KnInvite ","")
                kn.findAndAddContactsByMid(midd)
                kn.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif msg.text in ["me","Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
            elif msg.text in ["Gc"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName                
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
            elif msg.text in ["Yid","yid"]:
                cl.sendText(msg.to,msg.from_)
            elif msg.text in ["gift","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
                print "SUKSES -- SEND GIFT"
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text in ["cancel","Cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        print "SUKSES -- CANCEL INVITE GROUP"
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["いいね:オフ","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")

            elif msg.text in ["Ourl","Link on","ourl","our","Our"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    print "SUKSES -- OPEN URL GROUP"
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off","curl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    print "SUKSES -- CLOSE URL GROUP"
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    print "SUKSES -- SEND GINFO"
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to) 
            elif msg.text in ["Mid","mid","MID"]:
                print "SUKSES -- SHOW MID USER"
                cl.sendText(msg.to, msg.from_)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟")
                    else:
                        cl.sendText(msg.to,"完成")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉")
                    else:
                        cl.sendText(msg.to,"完成 ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉")
                    else:
                        cl.sendText(msg.to,"完成")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟")
                    else:
                        cl.sendText(msg.to,"完成")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉")
                    else:
                        cl.sendText(msg.to,"完成")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")

            elif msg.text in ["Cancel off","cancel off"]:
                if msg.from_ in admin:
                    if cancelinvite["autoCancel"] == True:
                        cancelinvite["autoCancel"] = False
                        cl.sendText(msg.to, "Auto Cancel turned off")
                        print "[Command]Cancel off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Cancel off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Cancel on","cancel on"]:
                if msg.from_ in admin:
                    if cancelinvite["autoCancel"] == False:
                        cancelinvite["autoCancel"] = True
                        cl.sendText(msg.to, "Auto Cancel turned on")
                        print "[Command]Cancel on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned on")
                        print "[Command]Cancel on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Set"]:
                md = ""
                if wait["contact"] == True: md+=" 調查友資:開啟\n"
                else: md+=" 調查友資:關閉\n"
                if wait["autoJoin"] == True: md+=" 自動進群:開啟\n"
                else: md +=" 自動進群:關閉\n"
                if wait["leaveRoom"] == True: md+=" 自動離開副本:開啟\n"
                else: md+=" 自動離開副本:關閉\n"
                if wait["autoAdd"] == True: md+=" 自動加好友:開啟"
                else:md+=" 自動加好友:關閉"
                cl.sendText(msg.to,md)
            elif msg.text in ["Group id","group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["/listgroup","/Listgroup","/List group","/list group"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[=> %s\n" % (cl.getGroup(i).name)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                    print "SUKSES -- SEND CANCELALL"
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif msg.text in ["Add on","Auto add:on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Add off","Auto add:off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"已開啟")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"已關閉")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                    print "SUKSES -- OPEN AND SHARE LINK GROUP"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"已開啟")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"完成")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"已關閉")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"完成")
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam Update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")
            
#-----------------------------------------------
            elif msg.text in ["Sljoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ad.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = kn.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kn.updateGroup(G)
                    print "SUKSES -- SUMMON BOT"
                    G.preventJoinByTicket(G)
                    kn.updateGroup(G)
            elif msg.text in ["Cljoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ad.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
            elif msg.text in ["Kijoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
            elif msg.text in ["Kkjoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
            elif msg.text in ["Kcjoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
            elif msg.text in ["Kdjoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
            elif msg.text in ["Kejoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    Ake.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
            elif msg.text in ["Kfjoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
            elif msg.text in ["Kgjoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
            elif msg.text in ["Khjoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
            elif msg.text in ["Kjjoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
            elif msg.text in ["Kljoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
            elif msg.text in ["Knjoin"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
#-----------------------------------------------
            elif msg.text in ["Slbye"]:
              if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        ad.leaveGroup(msg.to)
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        kf.leaveGroup(msg.to)
                        kg.leaveGroup(msg.to)
                        kh.leaveGroup(msg.to)
                        kj.leaveGroup(msg.to)
                        kl.leaveGroup(msg.to)
                        kn.leaveGroup(msg.to)
                        print "SUKSES -- BOT OUT GROUP"
                    except:
                        pass
            elif msg.text in ["Ad bye"]:
              if msg.from_ in admin:
                    ginfo = ad.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        ad.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ki bye"]:
              if msg.from_ in admin:
                    ginfo = ki.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kk bye"]:
              if msg.from_ in admin:
                    ginfo = kk.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kc bye"]:
              if msg.from_ in admin:
                    ginfo = kc.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kd bye"]:
              if msg.from_ in admin:
                    ginfo = kd.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kd.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ke bye"]:
              if msg.from_ in admin:
                    ginfo = ke.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        ke.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kf bye"]:
              if msg.from_ in admin:
                    ginfo = kf.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kf.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kg bye"]:
              if msg.from_ in admin:
                    ginfo = kg.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kg.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kh bye"]:
              if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kh.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kj bye"]:
              if msg.from_ in admin:
                   ginfo = kj.getGroup(msg.to)
                   print "EXECUTED -- BOT OUT GROUP"
                   try:
                       kj.leaveGroup(msg.to)
                   except:
                        pass
            elif msg.text in ["Kl bye"]:
              if msg.from_ in admin:
                    ginfo = kl.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kl.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kn bye"]:
              if msg.from_ in admin:
                    ginfo = kn.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kn.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ad.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"BYE")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ad,ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,kn]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                            print "SUKSES -- SEND KILL"
                        except:
                            pass
            elif "Sk:" in msg.text:
                if msg.from_ in admin:
                       print "EXECUTED -- NK TARGET"
                       nk0 = msg.text.replace("Sk:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,kn]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print "SUKSES -- NK TARGET"
                                except:
                                    pass
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Succes Cv")
                                except:
                                    ki.sendText(msg.to,"error")
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                print "EXECUTED -- BAN TARGET"
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Ter-Banned")
                      print "SUKSES -- BAN TARGET"
                   except:
                      pass
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "EXECUTED -- UNBAN TARGET"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ki.sendText(msg.to,"Succes Unbaned")
                                print "SUKSES -- UNBAN TARGET"
                            except:
                                ki.sendText(msg.to,"Succes UNBANNED")
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Me @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("Me @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                        pass
#-----------------------------------------------
            elif msg.text in ["tagall","tag all","แทก","แท็ก"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#
            elif "Tagall" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
#-----------------------------------------------

#-----------------------------------------------
            elif "Bc " in msg.text:
                if msg.from_ in admin:
                    bctxt = msg.text.replace("Bc ","")
		    ki.sendText(msg.to,(bctxt))
                    kk.sendText(msg.to,(bctxt))
                    cl.sendText(msg.to,(bctxt))
            elif "AGc " in msg.text:
                if msg.from_ in admin:
                  bctxt = msg.text.replace("AGc ","")
                  gid = cl.getGroupIdsJoined()
                  for i in gid:
                    ki.sendText(i,(bctxt))
                    kk.sendText(i,(bctxt))
                    cl.sendText(i,(bctxt))
#-----------------------------------------------
            elif msg.text in ["Respon","respon","absen","Absen"]:
                cl.sendText(msg.to,"保鏢答數")
                ad.sendText(msg.to,"1")
                ki.sendText(msg.to,"2")
                kk.sendText(msg.to,"3")
                kc.sendText(msg.to,"4")
                kd.sendText(msg.to,"5")
                ke.sendText(msg.to,"6")
                kf.sendText(msg.to,"7")
                kg.sendText(msg.to,"8")
                kh.sendText(msg.to,"9")
                kj.sendText(msg.to,"10")
                kl.sendText(msg.to,"11")
                kn.sendText(msg.to,"12")
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"[黑單沒有人]")
                else:
                    cl.sendText(msg.to,"[黑單用戶]")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "EXCUTED -- KILL BAN"
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        print "SUKSES -- KILL BAN"
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Good Bye Sampah")
#--------------------
            elif msg.text == "#set":
              if msg.from_ in admin:
                cl.sendText(msg.to, "輸入#tes(｀・ω・´)")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
	            pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text == "#tes":
              if msg.from_ in admin:
		  if msg.to in wait2['readPoint']:
	            if wait2["ROM"][msg.to].items() == []:
	              chiya = ""
	            else:
	              chiya = ""
	              for rom in wait2["ROM"][msg.to].items():
	                print rom
	                chiya += rom[1] + "\n"

	            cl.sendText(msg.to, "↓↓↓↓↓↓↓↓↓↓已讀的人↓↓↓↓↓↓↓↓↓↓%s"  % (wait2['readMember'][msg.to]))
	          else:
	            cl.sendText(msg.to, "輸入#set")
#-----------------------------------------------------------speed
            elif "Admin add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"已給權")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif "Admin remove @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"已移除")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
#--------------------
            elif "Sb Add @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Add executing"
                        _name = msg.text.replace("Sb Add @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    cl.findAndAddContactsByMid(target)
                                    ki.findAndAddContactsByMid(target)
                                    kk.findAndAddContactsByMid(target)
                                    ki.findAndAddContactsByMid(target)
                                    kk.findAndAddContactsByMid(target)
                                    kc.findAndAddContactsByMid(target)
                                    kd.findAndAddContactsByMid(target)
                                    ke.findAndAddContactsByMid(target)
                                    kf.findAndAddContactsByMid(target)
                                    kg.findAndAddContactsByMid(target)
                                    kh.findAndAddContactsByMid(target)
                                    kj.findAndAddContactsByMid(target)
                                    kl.findAndAddContactsByMid(target)
                                    kn.findAndAddContactsByMid(target)
                                except:
                                    ki.sendText(msg.to,"Error")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")

#-----------------------------保護------------------------------
            elif "Pro:on" == msg.text:
				if msg.to in wait["pro"]:
					cl.sendText(msg.to,"保護已開啟")
				else:
					wait['pro'][msg.to] = cl.getGroup(msg.to).name
					f=codecs.open('pro.json','w','utf-8')
					json.dump(wait['pro'], f, sort_keys=True, indent=4,ensure_ascii=False)
					protection.append(msg.to)
					cl.sendText(msg.to,"保護開啟")
            elif "Pro:off" == msg.text:
				try:
					del wait['pro'][msg.to] = cl.getGroup(msg.to).name
					protection.remove(msg.to)
					cl.sendText(msg.to,"鎖邀請已關閉")
				except:
					pass
            elif "Name:on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"已開啟")
                else:
                    cl.sendText(msg.to,"鎖群名已開啟")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Name:off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"已關閉")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"鎖群名已關閉")
            elif "Invite:on" == msg.text:
				gid = msg.to
				wait['pinv'][msg.to]
				cl.sendText(msg.to,"鎖邀請已開啟")
            elif "Invite:off" == msg.text:
				try:
					del wait['pinv'][msg.to]
					cl.sendText(msg.to,"鎖邀請已關閉")
				except:
					pass
            elif msg.text in ["all:on"]:
                if msg.from_ in Administrator:
                    try:
                        wait['pro'][msg.to] = cl.getGroup(msg.to).name
                        protection.append(msg.to)                        
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
                        gid = msg.to
                        wait['pinv'][gid] = "poni"
                        wait['purl'][msg.to]
                        cl.sendText(msg.to,"全開啟")
                    except:
					    pass
            elif msg.text in ["all:off"]:
                if msg.from_ in Administrator:
                    try:
                        del wait['pro'][msg.to] = cl.getGroup(msg.to).name
                        protection.remove(msg.to)
                        del wait['pro_name'][msg.to]
                        del wait['pname'][msg.to]
                        del wait['pinv'][msg.to]
                        del wait['purl'][msg.to]
                        cl.sendText(msg.to,"全關閉")
                    except:
                        pass
            elif msg.text in ["url:on"]:
                if msg.from_ in Administrator:
                    wait['purl'][msg.to]
                    cl.sendText(msg.to,"已開")
            elif msg.text in ["url:off"]:
                if msg.from_ in Administrator:
                    del wait['purl'][msg.to]
                    cl.sendText(msg.to,"已關閉")
                else:
                    cl.sendText(msg.to,"已關閉")                
            elif msg.text in ["Sset"]:
                md = ""
                if msg.to in wait["pro"]: md+=" 防踢:開啟\n"
                else: md+=" 防踢:關閉\n"
                if msg.to in wait["pro_name"]: md+=" 鎖群名:開啟\n"
                else: md+=" 鎖群名:關閉\n"
                if msg.to in wait["pinv"]: md+=" 鎖邀請:開啟\n"
                else: md+=" 鎖邀請:關閉\n"
                if msg.to in wait["purl"]: md+=" 鎖網址:開啟"
                else: md+=" 鎖網址:關閉"
                cl.sendText(msg.to,md)
#---------------FUNGSI RATAIN GRUP TANPA KICK SESAMA BOT/Admin/Bots----------#
#-----------
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                ad.findAndAddContactsByMid(op.param1)
                ki.findAndAddContactsByMid(op.param1)
                kk.findAndAddContactsByMid(op.param1)
                kc.findAndAddContactsByMid(op.param1)
                kd.findAndAddContactsByMid(op.param1)
                ke.findAndAddContactsByMid(op.param1)
                kf.findAndAddContactsByMid(op.param1)
                kg.findAndAddContactsByMid(op.param1)
                kh.findAndAddContactsByMid(op.param1)
                kj.findAndAddContactsByMid(op.param1)
                kl.findAndAddContactsByMid(op.param1)
                kn.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 17:
            if mid in op.param3:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"這裡沒有黑單用戶")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"黑單勿近")
        if op.type ==13:
           if admid in op.param3:
               if wait["P"] == True:
                   ad.acceptGroupInvitation(op.param1)
                   ad.sendText(op.param1,"請不要邀保鏢,請邀請主帳號\nhttp://line.me/ti/p/~fang_xin")
                   ad.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Amid in op.param3:
               if wait["P"] == True:
                   ki.acceptGroupInvitation(op.param1)
                   ki.sendText(op.param1,"請不要邀保鏢,請邀請主帳號\nhttp://line.me/ti/p/~fang_xin")
                   ki.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Bmid in op.param3:
               if wait["P"] == True:
                   kk.acceptGroupInvitation(op.param1)
                   kk.sendText(op.param1,"請不要邀保鏢,請邀請主帳號\nhttp://line.me/ti/p/~fang_xin")
                   kk.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Cmid in op.param3:
               if wait["P"] == True:
                   kc.acceptGroupInvitation(op.param1)
                   kc.sendText(op.param1,"請不要邀保鏢,請邀請主帳號\nhttp://line.me/ti/p/~fang_xin")
                   kc.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Dmid in op.param3:
               if wait["P"] == True:
                   kd.acceptGroupInvitation(op.param1)
                   kd.sendText(op.param1,"請不要邀保鏢,請邀請主帳號\nhttp://line.me/ti/p/~fang_xin")
                   kd.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Emid in op.param3:
               if wait["P"] == True:
                   ke.acceptGroupInvitation(op.param1)
                   ke.sendText(op.param1,"請不要邀保鏢,請邀請主帳號\nhttp://line.me/ti/p/~fang_xin")
                   ke.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Fmid in op.param3:
               if wait["P"] == True:
                   kf.acceptGroupInvitation(op.param1)
                   kf.sendText(op.param1,"請不要邀保鏢,請邀請主帳號\nhttp://line.me/ti/p/~fang_xin")
                   kf.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Gmid in op.param3:
               if wait["P"] == True:
                   kg.acceptGroupInvitation(op.param1)
                   kg.sendText(op.param1,"請不要邀保鏢,請邀請主帳號\nhttp://line.me/ti/p/~fang_xin")
                   kg.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Hmid in op.param3:
               if wait["P"] == True:
                   kh.acceptGroupInvitation(op.param1)
                   kh.sendText(op.param1,"請不要邀保鏢,請邀請主帳號\nhttp://line.me/ti/p/~fang_xin")
                   kh.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Jmid in op.param3:
               if wait["P"] == True:
                   kj.acceptGroupInvitation(op.param1)
                   kj.sendText(op.param1,"請不要邀保鏢,請邀請主帳號\nhttp://line.me/ti/p/~fang_xin")
                   kj.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Lmid in op.param3:
               if wait["P"] == True:
                   kl.acceptGroupInvitation(op.param1)
                   kl.sendText(op.param1,"請不要邀保鏢,請邀請主帳號\nhttp://line.me/ti/p/~fang_xin")
                   kl.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Nmid in op.param3:
               if wait["P"] == True:
                   kn.acceptGroupInvitation(op.param1)
                   kn.sendText(op.param1,"請不要邀保鏢,請邀請主帳號\nhttp://line.me/ti/p/~fang_xin")
                   kn.leaveGroup(op.param1)
               else:
                   pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    print "BOT 1 Joined"
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    ad.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                    cl.sendText(op.param1, "進入成功.")
                    G.preventJoinByTicket = True
                    kn.updateGroup(G)
                    print "all join"
            else:
                if cancelinvite["autoCancel"] == True:
                    try:
                        X = cl.getGroup(op.param1)
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)
                        print gInviMids + "invite canceled"
                    except:
                        try:
                            print "Retry canceling invitation"
                            X = random.choice(KAC).getGroup(op.param1)
                            gInviMids = [contact.mid for contact in X.invitee]
                            random.choice(KAC).cancelGroupInvitation(op.param1, gInviMids)
                            print gInviMids + "invite canceled"
                        except:
                            print "Bot can't cancel the invitation"
                            pass
        if op.type == 19:        
           if op.param1 in wait["pro"]:
              OWN = admin + Bots
           if op.param2 in OWN:
               pass
           elif wait["P"] == True:
                 try:
                     ki.kickoutFromGroup(op.param1,[op.param2])
                 except:
                     try:
                         kk.kickoutFromGroup(op.param1,[op.param2])
                     except:
                         try:
                             kc.kickoutFromGroup(op.param1,[op.param2])
                         except:
                             try:
                                 kd.kickoutFromGroup(op.param1,[op.param2])
                             except:
                                 try:
                                     ke.kickoutFromGroup(op.param1,[op.param2])
                                 except:
                                     try:
                                         kf.kickoutFromGroup(op.param1,[op.param2])
                                     except:
                                         try:
                                             kg.kickoutFromGroup(op.param1,[op.param2])
                                         except:
                                             try:
                                                 kh.kickoutFromGroup(op.param1,[op.param2])
                                             except:
                                                 try:
                                                     kj.kickoutFromGroup(op.param1,[op.param2])
                                                 except:
                                                     try:
                                                         kl.kickoutFromGroup(op.param1,[op.param2])
                                                     except:
                                                         try:
                                                             kn.kickoutFromGroup(op.param1,[op.param2])
                                                         except:
                                                             pass
                                                             wait["blacklist"][op.param2] = True
                                                             f=codecs.open('st2__b.json','w','utf-8')
                                                             json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

   
        if op.param3 == "1":
            if op.param1 in protectname:
                OWN = admin
                if op.param2 in OWN:
                    pass
                elif wait["P"] == True:
                     group = cl.getGroup(op.param1)
                     try:
                         group.name = wait["pro_name"][op.param1]
                         cl.updateGroup(group)
                         cl.sendText(op.param1, "Groupname protect now")
                         wait["blacklist"][op.param2] = True
                         f=codecs.open('st2__b.json','w','utf-8')
                         json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                     except Exception as e:
                         print e
                         pass
               
        if op.param1 in wait["pinv"]:
           OWN = admin
           if op.param2 in OWN:
              pass
           else:
               Inviter = op.param3.replace("",',')
               InviterX = Inviter.split(",")
               contact = cl.getContact(op.param2)
               cl.cancelGroupInvitation(op.param1,InviterX)
               ki.cancelGroupInvitation(op.param1,InviterX)
               kk.cancelGroupInvitation(op.param1,InviterX)
               kk.cancelGroupInvitation(op.param1,InviterX)
               kc.cancelGroupInvitation(op.param1,InviterX)
               kd.cancelGroupInvitation(op.param1,InviterX)
               ke.cancelGroupInvitation(op.param1,InviterX)
               kf.cancelGroupInvitation(op.param1,InviterX)
               kg.cancelGroupInvitation(op.param1,InviterX)
               kh.cancelGroupInvitation(op.param1,InviterX)
               kj.cancelGroupInvitation(op.param1,InviterX)
               kl.cancelGroupInvitation(op.param1,InviterX)
               kn.cancelGroupInvitation(op.param1,InviterX)            



        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                elif op.param3 in Amid:
                    if op.param2 in Bmid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)

                elif op.param3 in Bmid:
                    if op.param2 in Cmid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        kc.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        
                elif op.param3 in Cmid:
                    if op.param2 in Dmid:
                        G = kd.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kd.updateGroup(G)
                        Ticket = kd.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kd.updateGroup(G)
                    else:
                        G = kd.getGroup(op.param1)

                        kd.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kd.updateGroup(G)
                        Ticket = kd.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kd.updateGroup(G)
                elif op.param3 in Dmid:
                    if op.param2 in Emid:
                        G = ke.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ke.updateGroup(G)
                        Ticket = ke.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ke.updateGroup(G)
                    else:
                        G = ke.getGroup(op.param1)

                        ke.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ke.updateGroup(G)
                        Ticket = ke.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ke.updateGroup(G)
                elif op.param3 in Emid:
                    if op.param2 in Fmid:
                        G = kf.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kf.updateGroup(G)
                        Ticket = kf.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kf.updateGroup(G)
                    else:
                        G = kf.getGroup(op.param1)

                        kf.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kf.updateGroup(G)
                        Ticket = kf.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kf.updateGroup(G)
                elif op.param3 in Fmid:
                    if op.param2 in Gmid:
                        G = kg.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kg.updateGroup(G)
                        Ticket = kg.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kg.updateGroup(G)
                    else:
                        G = kg.getGroup(op.param1)

                        kg.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kg.updateGroup(G)
                        Ticket = kg.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kg.updateGroup(G)
                elif op.param3 in Gmid:
                    if op.param2 in Hmid:
                        G = kh.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kh.updateGroup(G)
                        Ticket = kh.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kh.updateGroup(G)
                    else:
                        G = kh.getGroup(op.param1)

                        kh.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kh.updateGroup(G)
                        Ticket = kh.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kh.updateGroup(G)
                elif op.param3 in Hmid:
                    if op.param2 in Jmid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        kj.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                elif op.param3 in Jmid:
                    if op.param2 in Lmid:
                        G = kl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kl.updateGroup(G)
                        Ticket = kl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kj.updateGroup(G)
                    else:
                        G = kl.getGroup(op.param1)

                        kc.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kl.updateGroup(G)
                        Ticket = kl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kn.updateGroup(G)
                elif op.param3 in Lmid:
                    if op.param2 in Nmid:
                        G = kn.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kn.updateGroup(G)
                        Ticket = kn.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ke.updateGroup(G)
                    else:
                        G = kn.getGroup(op.param1)

                        kf.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kn.updateGroup(G)
                        Ticket = kn.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kn.updateGroup(G)
                elif op.param3 in Nmid:
                    if op.param2 in admid:
                        G = ad.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ad.updateGroup(G)
                        Ticket = ad.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ad.updateGroup(G)
                    else:
                        G = ad.getGroup(op.param1)

                        kg.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ad.updateGroup(G)
                        Ticket = ad.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kh.updateGroup(G)
                elif op.param3 in admid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ad.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kj.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        kj.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ad.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    
            except:
                pass

#----------------------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n☑" + Name
                        wait2['ROM'][op.param1][op.param2] = "☑" + Name
                else:
                    cl.sendText
            except:
                  pass
                  
#-----------------------------------------------------
#-----------------------------------------------------
#-----------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
            if wait["clock"] == True:
                profile = ad.getProfile()
                profile.displayName = "Cl.Bot"
                ad.updateProfile(profile)
                profile = ki.getProfile()
                profile.displayName = "Ki.Bot"
                ki.updateProfile(profile)
                profile = kk.getProfile()
                profile.displayName = "Kk.Bot"
                kk.updateProfile(profile)
                profile = kc.getProfile()
                profile.displayName = "Kc.Bot"
                kc.updateProfile(profile)
                profile = kd.getProfile()
                profile.displayName = "Kd.Bot"
                kd.updateProfile(profile)
                profile = ke.getProfile()
                profile.displayName = "Ke.Bot"
                ke.updateProfile(profile)
                profile = kf.getProfile()
                profile.displayName = "Kf.Bot"
                kf.updateProfile(profile)
                profile = kg.getProfile()
                profile.displayName = "Kg.Bot"
                kg.updateProfile(profile)
                profile = kh.getProfile()
                profile.displayName = "Kh.Bot"
                kh.updateProfile(profile)
                profile = kj.getProfile()
                profile.displayName = "Kj.Bot"
                kj.updateProfile(profile)
                profile = kl.getProfile()
                profile.displayName = "Kl.Bot"
                kl.updateProfile(profile)
                profile = kn.getProfile()
                profile.displayName = "Kn.Bot"
                kn.updateProfile(profile)
                
                #profile = cl.getProfile()
                #profile.statusMessage = wait["string"]
                #cl.updateProfile(profile)
                profile = ki.getProfile()
                profile.statusMessage = wait["string"]
                ki.updateProfile(profile)
                profile = kk.getProfile()
                profile.statusMessage = wait["string"]
                kk.updateProfile(profile)
                profile = kc.getProfile()
                profile.statusMessage = wait["string"]
                kc.updateProfile(profile)
                profile = kd.getProfile()
                profile.statusMessage = wait["string"]
                kd.updateProfile(profile)
                profile = ke.getProfile()
                profile.statusMessage = wait["string"]
                ke.updateProfile(profile)
                profile = kf.getProfile()
                profile.statusMessage = wait["string"]
                kf.updateProfile(profile)
                profile = kg.getProfile()
                profile.statusMessage = wait["string"]
                kg.updateProfile(profile)
                profile = kh.getProfile()
                profile.statusMessage = wait["string"]
                kh.updateProfile(profile)
                profile = kj.getProfile()
                profile.statusMessage = wait["string"]
                kj.updateProfile(profile)
                profile = kl.getProfile()
                profile.statusMessage = wait["string"]
                kl.updateProfile(profile)
                profile = kn.getProfile()
                profile.statusMessage = wait["string"]
                kn.updateProfile(profile)
            time.sleep(200)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(ad.Poll.rev, Op.revision)
            bot(Op)
