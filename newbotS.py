# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob


cl = LINETCR.LINE() #A)
cl.login(token="EnRnCQuNdVWF7sAfDquf.FyCqvzVAe2RNaWr3/dbP3W.zoOHfQRRd9BFqw5xBAf83OGJ/TSvzOuvJTITcPPuhEA=")
cl.loginResult()

ad = LINETCR.LINE()
ad.login(token="EnsV1kf9Kv7hMYgpmJV5.iur748Us1jyfpKv4oxGLDq.CCM3eRnw8JUvXbQJQBwCJzpMxZdJteHJ0w1Hx8F5EOg=")
ad.loginResult()

ki = LINETCR.LINE()
ki.login(token="Engvk5u8ZJ8DG7gf1p4a.PzuIGrSfbi6ZimWr5ex5QG.VpfMr0jFJyU9qxSTHkKfqheaFecA5tWyM5QNisDIAG0=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="EnN9YazOKYGPZW7JQ8Ef.DRgr2cTxeEiDATETLgm6FW.18J29FJ9MzsZFHYPCvaB95C2a6fqiUSFCM+CeYgTGrM=")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token="EnVJMd88bs4FeqvkBEg0.0xXKLPaf8b6wAiXZDw/zKa.qB2Bj/TEUO9S1VNvQOK6LCiZ2G+a8QnpLMTfTbMIqhM=")
kc.loginResult()

kd = LINETCR.LINE()
kd.login(token="EntVCvViAliX4tcIUxL2.c74e1FIgViqAn7KTUdEVWG.8PiECZroQNySsL4nc8hgA28GDIqHBJhexgW36NQ/cpA=")
kd.loginResult()

ke = LINETCR.LINE()
ke.login(token="EnAhGsD2TGGe1Tl0f19c.fDEuyTzDGQmGfp4ckPUkpa.zEqKstdKpZz46Iyiz7Q88ZAwclBCPamKONDB+GNK3Zk=")
ke.loginResult()

kf = LINETCR.LINE()
kf.login(token="EnKOS9oxIIPfmSL2Trb9.jnrl5WXaTf6U4igiiB7LEq.yEWIm+xKXpLMTthBUl+jcUDEtrp1ld7VVuwKU6NoSFY=")
kf.loginResult()

kg = LINETCR.LINE()
kg.login(token="EnIvDWLSi9gFpLCZiZd9.e1FgUhH3JoxZEfGo0PR5Aq.9caRf92R6qB+HkPjYMvjAgwYCC/rizffLPPK5u2KSzE=")
kg.loginResult()

kh = LINETCR.LINE()
kh.login(token="En1eb5aom8EucO8O55z7.iDoQGqR5vJevZClhLwopPW.BXqY6R5bJ66se3VgSQAoNkyedRVZAqFH4MCfj/6Ek/k=")
kh.loginResult()

kj = LINETCR.LINE()
kj.login(token="EnuQymrrIPL2d7cnwtc4.sumo+F0V0TIBr+nNrlJgna.Ct9OxlUdxlhc6xqz83pok03DetbazIHLRLXVik1jR90=")
kj.loginResult()

kl = LINETCR.LINE()
kl.login(token="EnoeC1tGjQQWX8rtDw71.3QcCJv4kHUj+58p8vc5viq.EYDidsX/LdZ5W+7K0QM0lYTT2UuvanA4oNcVsk/aTfM=")
ki.loginResult()

kn = LINETCR.LINE()
kn.login(token="EnSJUVKkhghnTphgAW40.0tGK0m6LMWuegE+xHNjzKa.EX39mMZ+GUUVfVjXneFgqsgf37qvYAwyr5JEirgUGHY=")
kn.loginResult()


print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""[Help 不給看勒]"""
Inmes ="""邀三小"""
KAC=[cl,ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,kn,ad]
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
fuck = "uf274cd013e86f8bffec153a26e45f247"
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
OOO = []
ticket = []
wait = {
    'protect':False,
    'protectinv':False,
    'protectqr':False,
    'contact':False,
    'autoJoin':False,
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':True,
    'message':"詞語Bot\nAutboLike\nhttp://line.me/ti/p/~fang_xin\nhttp://line.me/ti/p/~.90.11.24.",
    "lang":"JP",
    "comment":"http://line.me/ti/p/~fang_xin\nAuto like By fung xin",
    "likeOn":True,
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "msge":True,
    "clock":True,
    "blacklist":{},
    "P":True,
    "PP":True,
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
#                    if op.param2 in admin:
#                        pass
#                    else:
#                        try:
#                            ki.kickoutFromGroup(op.param1,[op.param2])
#                        except:
#                            try:
#                                kk.kickoutFromGroup(op.param1,[op.param2])
#                            except:
#                                try:
#                                    kc.kickoutFromGroup(op.param1,[op.param2])
#                                except:
#                                    try:
#                                        kd.kickoutFromGroup(op.param1,[op.param2])
#                                    except:
#                                        try:
#                                            ke.kickoutFromGroup(op.param1,[op.param2])
#                                        except:
#                                            pass
#                                        cl.sendText(op.param1,"群名已鎖")
#                                        cl.sendText(op.param1,"更改者為")
#                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
#                                        c.contentMetadata={'mid':op.param2}
#                                        cl.sendMessage(c)
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
                    cl.sendText(msg.to,"黑單已飛")
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        cl.sendText(op.param1,"群名已鎖")
                        cl.sendText(op.param1,"更改者為")
                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':op.param2}
                        cl.sendMessage(c)
                    except:
                        pass
        if op.param1 in autocancel:
            if op.param2 in admin:
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
        if op.param3 == "4":
            if op.param2 not in admin:
              if op.param1 in protecturl:
                  group = cl.getGroup(op.param1)
                  if group.preventJoinByTicket == False:
                      group.preventJoinByTicket = True
                      cl.updateGroup(group)
                  else:
                      pass
#        if op.type == 19:        
#           if op.param1 in wait["pro"]:
#             if op.param2 in admin:
#                 pass
#             elif wait["P"] == True:
#                   try:
#                       ki.kickoutFromGroup(op.param1,[op.param2])
#                   except:
#                       try:
#                           kk.kickoutFromGroup(op.param1,[op.param2])
#                       except:
#                           try:
#                               kc.kickoutFromGroup(op.param1,[op.param2])
#                           except:
#                               try:
#                                   kd.kickoutFromGroup(op.param1,[op.param2])
#                               except:
#                                   try:
#                                       ke.kickoutFromGroup(op.param1,[op.param2])
#                                   except:
#                                       try:
#                                           kf.kickoutFromGroup(op.param1,[op.param2])
#                                       except:
#                                           try:
#                                               kg.kickoutFromGroup(op.param1,[op.param2])
#                                           except:
#                                               try:
#                                                   kh.kickoutFromGroup(op.param1,[op.param2])
#                                               except:
#                                                   try:
#                                                       kj.kickoutFromGroup(op.param1,[op.param2])
#                                                   except:
#                                                       try:
#                                                           kl.kickoutFromGroup(op.param1,[op.param2])
#                                                       except:
#                                                           try:
#                                                               kn.kickoutFromGroup(op.param1,[op.param2])
#                                                           except:
#                                                               pass
#                                                               wait["blacklist"][op.param2] = True
#                                                               f=codecs.open('st2__b.json','w','utf-8')
#                                                               json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        if op.type == 19:
           if op.param2 in admin:
               pass
           if op.param1 in wait["pro"]:
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
        if op.type == 0:
            return 
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.sendText(op.param1,"邀啥小")
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg  = op.message
            if "機器預熱" in msg.text:
                if msg.from_ in fuck:
                    try:
                        ki.kickoutFromGroup(msg.to,msg.from_)
                    except:
                        try:
                            kk.kickoutFromGroup(msg.to,msg.from_)
                        except:
                            try:
                                kc.kickoutFromGroup(msg.to,msg.from_)
                            except:
                                try:
                                    kd.kickoutFromGroup(msg.to,msg.from_)
                                except:
                                    try:
                                        ke.kickoutFromGroup(msg.to,msg.from_)
                                    except:
                                        try:
                                             kf.kickoutFromGroup(msg.to,msg.from_)
                                        except:
                                            try:
                                                kg.kickoutFromGroup(msg.to,msg.from_)
                                            except:
                                                try:
                                                    kh.kickoutFromGroup(msg.to,msg.from_)
                                                except:
                                                    try:
                                                        kj.kickoutFromGroup(msg.to,msg.from_)
                                                    except:
                                                        try:
                                                            kl.kickoutFromGroup(msg.to,msg.from_)
                                                        except:
                                                            try:
                                                                kn.kickoutFromGroup(msg.to,msg.from_)
                                                            except:
                                                                pass
                else:
                    try:
                        ki.sendText(msg.to,"預三小")
                    except:
                        cl.sendText(msg.to,"預三小")
                                                            
        if op.type == 25:
            msg = op.message
            if ("Tgive " in msg.text):
              if msg.from_ in admin:
                print "EXECUTED -- admin TARGET"
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ticket.append(target)
                      cl.sendText(msg.to,"已給")
                   except:
                      pass
            elif ("Tdel " in msg.text):
              if msg.from_ in admin:
                print "EXECUTED -- 刪除"
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ticket.remove(target)
                      cl.sendText(msg.to,"已拔")
                   except:
                      pass
            elif ("Tchk" in msg.text):
                y = cl.getContact(msg.from_)
                k = y.displayName
                cl.sendText(msg.to,ticket.count(k))
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
            elif "Kick:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "ClKo:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("ClKo:","")
                ad.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KiKo:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KiKo:","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "KkKo:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KkKo:","")
                kk.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KcKo:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KcKo:","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "KdKo:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KdKo:","")
                kd.kickoutFromGroup(msg.to,[midd])
            elif "KeKo:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KeKo:","")
                ke.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KfKo:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KfKo:","")
                kf.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KgKo:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KgKo:","")
                kg.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KhKo:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KhKo:","")
                kh.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KjKo:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KjKo:","")
                kj.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KlKo:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KlKo:","")
                kl.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "KnKo:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KnKo:","")
                kn.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "Into:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Into:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "ClIn:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("ClIn:","")
                ad.findAndAddContactsByMid(midd)
                ad.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KiIn:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KiIn:","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KkIn:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KkIn:","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KcIn:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KcIn:","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KdIn:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KdIn:","")
                kd.findAndAddContactsByMid(midd)
                kd.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KeIn:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KeIn:","")
                ke.findAndAddContactsByMid(midd)
                ke.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KfIn:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KfIn:","")
                kf.findAndAddContactsByMid(midd)
                kf.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"         
            elif "KgIn:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KgIn:","")
                kg.findAndAddContactsByMid(midd)
                kg.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KhIn:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KhIn:","")
                kh.findAndAddContactsByMid(midd)
                kh.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KjIn:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KjIn:","")
                kj.findAndAddContactsByMid(midd)
                kj.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KlIn:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KlIn:","")
                kl.findAndAddContactsByMid(midd)
                kl.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif "KnIn:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("KnIn:","")
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
                            cl.sendText(msg.to,"沒有邀請")
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
            elif msg.text in ["K on","Contact on"]:
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
            elif msg.text in ["K off","Contact off"]:
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
            elif msg.text in ["Join on","Auto join:on"]:
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
            elif msg.text in ["Join off","Auto join:off"]:
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
            elif msg.text in ["Leave on","Auto leave:on"]:
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
            elif msg.text in ["Leave off","Auto leave:off"]:
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
            elif msg.text in ["機制/開"]:
              if msg.from_ in admin:
                if wait["PP"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["PP"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟")
                    else:
                        cl.sendText(msg.to,"完成")
            elif msg.text in ["機制/關"]:
              if msg.from_ in admin:
                if wait["PP"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉")
                    else:
                        cl.sendText(msg.to,"完成 ")
                else:
                    wait["PP"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉")
                    else:
                        cl.sendText(msg.to,"完成")
            elif msg.text in ["Set"]:
                md = ""
                O = "•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•"
                if wait["contact"] == True: md+= O + "\n☑調查友資:開啟\n" + O
                else: md+= O + "\n❎調查友資:關閉\n" + O
                if wait["autoJoin"] == True: md+=" \n☑自動進群:開啟\n" + O
                else: md +=" \n❎自動進群:關閉\n" + O
                if wait["leaveRoom"] == True: md+=" \n☑自動離開副本:開啟\n" + O
                else: md+=" \n❎自動離開副本:關閉\n" + O
                if wait["autoAdd"] == True: md+=" \n☑自動加好友:開啟\n" + O
                else:md+=" \n❎自動加好友:關閉\n" + O
                if wait["PP"] == True: md+=" \n☑機制:開啟\n" + O
                else:md+=" \n❎機制:關閉\n" + O
                if msg.to in wait["pro"]: md+=" \n☑防踢:開啟\n" + O
                else: md+=" \n❎防踢:關閉\n" + O
                if msg.to in wait["pro_name"]: md+=" \n☑鎖群名:開啟\n" + O
                else: md+=" \n❎鎖群名:關閉\n" + O
                if msg.to in autocancel: md+=" \n☑鎖邀請:開啟\n" + O
                else: md+=" \n❎鎖邀請:關閉\n" + O
                if msg.to in protecturl: md+=" \n☑鎖網址:開啟\n" + O
                else: md+=" \n❎鎖網址:關閉\n" + O
                cl.sendText(msg.to,md)
            elif msg.text in ["Group id","group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["所有數量"]:
                gid = cl.getGroupIdsJoined()
                fid =  cl.getAllContactIds()
                Iid =  cl.getGroupIdsInvited()
                if Iid is None:
                    Iid = "0"
                else:
                    Iid = cl.getGroupIdsInvited()
                cl.sendText(msg.to,"群組:" + str(len(gid)) + "\n群組邀請中:" + str(len(Iid)) + "\n好友:" + str(len(fid)))
            elif msg.text in ["/listgroup","/Listgroup","/List group","/list group"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                o = int(str(0))
                for i in gid:
                    h += int(str(o)) +"[=> %s\n" % (cl.getGroup(i).name)
                    o = (o + int(str(1)))
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                gid = ki.getGroupIdsInvited()
                gid = kk.getGroupIdsInvited()
                gid = kc.getGroupIdsInvited()
                gid = kd.getGroupIdsInvited()
                gid = ke.getGroupIdsInvited()
                gid = kf.getGroupIdsInvited()
                gid = kg.getGroupIdsInvited()
                gid = kh.getGroupIdsInvited()
                gid = kj.getGroupIdsInvited()
                gid = kl.getGroupIdsInvited()
                gid = kn.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                    ki.rejectGroupInvitation(i)
                    kk.rejectGroupInvitation(i)
                    kc.rejectGroupInvitation(i)
                    kd.rejectGroupInvitation(i)
                    ke.rejectGroupInvitation(i)
                    kf.rejectGroupInvitation(i)
                    kg.rejectGroupInvitation(i)
                    kh.rejectGroupInvitation(i)
                    kj.rejectGroupInvitation(i)
                    kl.rejectGroupInvitation(i)
                    kn.rejectGroupInvitation(i)
                    print "SUKSES -- SEND CANCELALL"
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"全部邀請已清除")
                else:
                    cl.sendText(msg.to,"錯誤")
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
                        cl.sendText(msg.to,"完成")
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
                        cl.sendText(msg.to,"完成")
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
#---------------------------------------------
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
            elif msg.text in ["Adbye"]:
              if msg.from_ in admin:
                    ginfo = ad.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        ad.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kibye"]:
              if msg.from_ in admin:
                    ginfo = ki.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kkbye"]:
              if msg.from_ in admin:
                    ginfo = kk.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kcbye"]:
              if msg.from_ in admin:
                    ginfo = kc.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kdbye"]:
              if msg.from_ in admin:
                    ginfo = kd.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kd.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kebye"]:
              if msg.from_ in admin:
                    ginfo = ke.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        ke.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kfbye"]:
              if msg.from_ in admin:
                    ginfo = kf.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kf.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kgbye"]:
              if msg.from_ in admin:
                    ginfo = kg.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kg.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Khbye"]:
              if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kh.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kjbye"]:
              if msg.from_ in admin:
                   ginfo = kj.getGroup(msg.to)
                   print "EXECUTED -- BOT OUT GROUP"
                   try:
                       kj.leaveGroup(msg.to)
                   except:
                        pass
            elif msg.text in ["Klbye"]:
              if msg.from_ in admin:
                    ginfo = kl.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        kl.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Knbye"]:
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
                      cl.sendText(msg.to,"已封鎖")
                      print "SUKSES -- BAN TARGET"
                   except:
                      pass
            elif ("Unban " in msg.text):
              if msg.from_ in admin:
                print "EXECUTED -- BAN TARGET"
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      del wait["blacklist"][target]
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"已解除")
                      print "SUKSES -- BAN TARGET"
                   except:
                      pass
            elif "Mid " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                c = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,c)
            elif "mid " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                c = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,c)
            elif "Me " in msg.text:
                msg.contentType = 13
                key = eval(msg.contentMetadata["MENTION"])
                c = key["MENTIONEES"][0]["M"]
                msg.contentMetadata = {'mid': c}
                cl.sendMessage(msg)
            elif "me " in msg.text:
                msg.contentType = 13
                key = eval(msg.contentMetadata["MENTION"])
                c = key["MENTIONEES"][0]["M"]
                msg.contentMetadata = {'mid': c}
                cl.sendMessage(msg)
            elif msg.text in ["Slm:"]:
                msg.contentType = 13
                mmid = msg.text.replace("Slm:","")
                msg.contentMetadata = {'mid':mmid}
                cl.sendMessage(msg)
                cl.sendText(msg.to,msg)
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
    #------------邀機---------------#

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
            elif "Sl:" in msg.text:
                if msg.from_ in admin:
                    bctxt = msg.text.replace("Sl:","")
                    cl.sendText(msg.to,(bctxt))
                    ki.sendText(msg.to,(bctxt))
                    kk.sendText(msg.to,(bctxt))
                    kc.sendText(msg.to,(bctxt))
                    kd.sendText(msg.to,(bctxt))
                    ke.sendText(msg.to,(bctxt))
                    kf.sendText(msg.to,(bctxt))
                    kg.sendText(msg.to,(bctxt))
                    kh.sendText(msg.to,(bctxt))
                    kj.sendText(msg.to,(bctxt))
                    kl.sendText(msg.to,(bctxt))
                    kn.sendText(msg.to,(bctxt))
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
                try:
                    cl.sendText(msg.to,"保鏢答數")
                except:
                    pass
                try:
                    ad.sendText(msg.to,"1")
                except:
                    pass
                try:
                    ki.sendText(msg.to,"2")
                except:
                    pass
                try:
                    kk.sendText(msg.to,"3")
                except:
                    pass
                try:
                    kc.sendText(msg.to,"4")
                except:
                    pass
                try:
                    kd.sendText(msg.to,"5")
                except:
                    pass
                try:
                    ke.sendText(msg.to,"6")
                except:
                    pass
                try:
                    kf.sendText(msg.to,"7")
                except:
                    pass
                try:
                    kg.sendText(msg.to,"8")
                except:
                    pass
                try:
                    kh.sendText(msg.to,"9")
                except:
                    pass
                try:
                    kj.sendText(msg.to,"10")
                except:
                    pass
                try:
                    kl.sendText(msg.to,"11")
                except:
                    pass
                try:
                    kn.sendText(msg.to,"12")
                except:
                    pass
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "計算...ing")
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
                    cl.sendText(msg.to,"Goodbye Sampah")
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
            elif ("Admin add " in msg.text):
              if msg.from_ in admin:
                print "EXECUTED -- admin TARGET"
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      admin.append(target)
                      cl.sendText(msg.to,"已給權")
                   except:
                      pass
#            elif "Admin add @" in msg.text:
#                if msg.from_ in admin:
#                    print "[Command]Staff add executing"
#                    _name = msg.text.replace("Admin add @","")
#                    _nametarget = _name.rstrip('  ')
#                    gs = cl.getGroup(msg.to)
#                    targets = []
#                    for g in gs.members:
#                        if _nametarget == g.displayName:
#                            targets.append(g.mid)
#                    if targets == []:
#                        ki.sendText(msg.to,"Contact not found")
#                    else:
#                        for target in targets:
#                            try:
#                                admin.append(target)
#                                cl.sendText(msg.to,"已給權")
#                            except:
#                                pass
#                    print "[Command]Staff add executed"
#                else:
#                    cl.sendText(msg.to,"Command denied.")
#                    cl.sendText(msg.to,"Admin permission required.")
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
            elif msg.text in ["Adminlist","adminlist"]:
                if admin == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"權限名單:")
                    mc = ""
                    for mi_d in admin:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
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
            elif "保護/開" == msg.text:
				if msg.to in wait["pro"]:
					cl.sendText(msg.to,"保護已開啟")
				else:
					wait['pro'][msg.to] = cl.getGroup(msg.to).name
					f=codecs.open('pro.json','w','utf-8')
					json.dump(wait['pro'], f, sort_keys=True, indent=4,ensure_ascii=False)
					protection.append(msg.to)
					cl.sendText(msg.to,"保護開啟")
            elif "保護/關" == msg.text:
				try:
					del wait['pro'][msg.to]
					protection.remove(msg.to)
					cl.sendText(msg.to,"保護已關閉")
				except:
					pass
            elif "群名/開" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"已開啟")
                else:
                    cl.sendText(msg.to,"鎖群名已開啟")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "群名/關" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"已關閉")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"鎖群名已關閉")
            elif "邀請/開" == msg.text:
				try:
					gid = msg.to
					autocancel[gid] = "poni"
					cl.sendText(msg.to,"鎖邀請已開")
				except:
					pass
            elif "邀請/關" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"鎖邀請已關")
				except:
					pass
            elif msg.text in ["全部/開"]:
                if msg.from_ in admin:
                    try:
                        protecturl.append(msg.to)
                        wait['pro'][msg.to] = cl.getGroup(msg.to).name
                        protection.append(msg.to)                        
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
                        gid = msg.to
                        autocancel[gid] = "poni"
                        cl.sendText(msg.to,"全開啟")
                    except:
					    pass
            elif msg.text in ["全部/關"]:
                if msg.from_ in admin:
                    try:
                        protecturl.remove(msg.to)
                        del wait['pro'][msg.to]
                        protection.remove(msg.to)
                        del wait['pro_name'][msg.to]
                        del wait['pname'][msg.to]
                        del autocancel[msg.to]
                        cl.sendText(msg.to,"全關閉")
                    except:
                        pass
            elif msg.text in ["網址/開"]:
                protecturl.append(msg.to)
                cl.sendText(msg.to,"鎖網址已開")
            elif msg.text in ["網址/關"]:
                if msg.from_ in admin:
                    protecturl.remove(msg.to)
                    cl.sendText(msg.to,"鎖網址已關")
                else:
                    cl.sendText(msg.to,"已鎖網址")
#---------------FUNGSI RATAIN GRUP TANPA KICK SESAMA BOT/Admin/Bots----------#
#-----------
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type ==13:
           if admin in op.param3:
               if op.param2 in ticket:
                 ad.acceptGroupInvitation(op.param1)
                 G = ad.getGroup(op.param1)
                 G.preventJoinByTicket = False
                 ad.updateGroup(G)
                 Ticket = ad.reissueGroupTicket(op.param1)
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
                 ad.sendText(op.param1, "保護開始")
                 G.preventJoinByTicket = True
                 kn.updateGroup(G)
                 ticket.remove(op.param2)
               else:
                 ad.acceptGroupInvitation(op.param1)
                 ad.sendText(op.param1,Inmes)
                 ad.leaveGroup(op.param1)
        if op.type ==13:
           if Amid in op.param3:
               if wait["P"] == True:
                   ki.acceptGroupInvitation(op.param1)
                   ki.sendText(op.param1,Inmes)
                   ki.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Bmid in op.param3:
               if wait["P"] == True:
                   kk.acceptGroupInvitation(op.param1)
                   kk.sendText(op.param1,Inmes)
                   kk.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Cmid in op.param3:
               if wait["P"] == True:
                   kc.acceptGroupInvitation(op.param1)
                   kc.sendText(op.param1,Inmes)
                   kc.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Dmid in op.param3:
               if wait["P"] == True:
                   kd.acceptGroupInvitation(op.param1)
                   kd.sendText(op.param1,Inmes)
                   kd.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Emid in op.param3:
               if wait["P"] == True:
                   ke.acceptGroupInvitation(op.param1)
                   ke.sendText(op.param1,Inmes)
                   ke.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Fmid in op.param3:
               if wait["P"] == True:
                   kf.acceptGroupInvitation(op.param1)
                   kf.sendText(op.param1,Inmes)
                   kf.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Gmid in op.param3:
               if wait["P"] == True:
                   kg.acceptGroupInvitation(op.param1)
                   kg.sendText(op.param1,Inmes)
                   kg.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Hmid in op.param3:
               if wait["P"] == True:
                   kh.acceptGroupInvitation(op.param1)
                   kh.sendText(op.param1,Inmes)
                   kh.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Jmid in op.param3:
               if wait["P"] == True:
                   kj.acceptGroupInvitation(op.param1)
                   kj.sendText(op.param1,Inmes)
                   kj.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Lmid in op.param3:
               if wait["P"] == True:
                   kl.acceptGroupInvitation(op.param1)
                   kl.sendText(op.param1,Inmes)
                   kl.leaveGroup(op.param1)
               else:
                   pass
        if op.type ==13:
           if Nmid in op.param3:
               if wait["P"] == True:
                   kn.acceptGroupInvitation(op.param1)
                   kn.sendText(op.param1,Inmes)
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
                pass
        if op.type == 19:
          if wait["PP"] == True:
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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        wait["blacklist"][op.param2] = True

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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        wait["blacklist"][op.param2] = True
                        
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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        wait["blacklist"][op.param2] = True
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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        wait["blacklist"][op.param2] = True
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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        wait["blacklist"][op.param2] = True
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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        wait["blacklist"][op.param2] = True
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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        wait["blacklist"][op.param2] = True
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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        wait["blacklist"][op.param2] = True
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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        wait["blacklist"][op.param2] = True
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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        wait["blacklist"][op.param2] = True
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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        wait["blacklist"][op.param2] = True
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
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                        except:
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
                                                    try:
                                                        G = kf.getGroup(op.param1)
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                        except:
                                                            try:
                                                                G = kh.getGroup(op.param1)
                                                            except:
                                                                try:
                                                                    G = kj.getGroup(op.param1)
                                                                except:
                                                                    try:
                                                                        G = kl.getGroup(op.param1)
                                                                    except:
                                                                        try:
                                                                            G = kn.getGroup(op.param1)
                                                                        except:
                                                                            pass
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
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
                        G.preventJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        try:
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            try:
                                Ticket = cl.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ticket = kd.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    Ticket = ke.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        Ticket = kf.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                Ticket = kh.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    Ticket = kk.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        Ticket = kl.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        try:
                                                                            Ticket = kn.reissueGroupTicket(op.param1)
                                                                        except:
                                                                            pass
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
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
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
                                                    try:
                                                        kf.updateGroup(G)
                                                    except:
                                                        try:
                                                            kg.updateGroup(G)
                                                        except:
                                                            try:
                                                                kh.updateGroup(G)
                                                            except:
                                                                try:
                                                                    kj.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        kl.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            kn.updateGroup(G)
                                                                        except:
                                                                            pass
                        wait["blacklist"][op.param2] = True
                    
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
                profile.displayName = "Cl"
                ad.updateProfile(profile)
                profile = ki.getProfile()
                profile.displayName = "Ki"
                ki.updateProfile(profile)
                profile = kk.getProfile()
                profile.displayName = "Kk"
                kk.updateProfile(profile)
                profile = kc.getProfile()
                profile.displayName = "Kc"
                kc.updateProfile(profile)
                profile = kd.getProfile()
                profile.displayName = "Kd"
                kd.updateProfile(profile)
                profile = ke.getProfile()
                profile.displayName = "Ke"
                ke.updateProfile(profile)
                profile = kf.getProfile()
                profile.displayName = "Kf"
                kf.updateProfile(profile)
                profile = kg.getProfile()
                profile.displayName = "Kg"
                kg.updateProfile(profile)
                profile = kh.getProfile()
                profile.displayName = "Kh"
                kh.updateProfile(profile)
                profile = kj.getProfile()
                profile.displayName = "Kj"
                kj.updateProfile(profile)
                profile = kl.getProfile()
                profile.displayName = "Kl"
                kl.updateProfile(profile)
                profile = kn.getProfile()
                profile.displayName = "Kn"
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
