# -*- coding: utf-8 -*-
from linepy import *
import json, time, random, tempfile, os, sys, codecs
from gtts import gTTS
from googletrans import Translator

#===================SELF========================
try:
    client = LineClient(authToken='auth_')
except:
    client = LineClient()
channel = LineChannel(client)
poll = LinePoll(client)
#===================ASSIST========================
try:
    assist = LineClient(authToken='auth_')
except:
    assist = LineClient()
assistchannel = LineChannel(assist)
assistpoll = LinePoll(assist)
#==================BOT LOGIN SUCCESS===============

#=================   BOT SETUP  ==================
clientMid = client.getProfile().mid
assistMid = assist.getProfile().mid
renBot = [clientMid,assistMid]
KCML = [client,assist]

vol = """[ Help Command ]

[ Help Menu ]
[√] Help <- Look command
[√] Me <- Look your contact
[√] Speed <- Look speedbot
[√] Mention <- Tagall
[√] Sideron <- Check reader
[√] Sideroff <- Stop Check reader
[ Menu Assist Admin ]
[√] . <- Joined assist
[√] , <- Assist out
[ Menu Protect ]
[√] ; <- Restart bot
[√] Pkick:[on/off] <- Protectkick
[√] ! @tag <- Kick with tag
[ Rework ]
[√] Admin -23 
[√] Id Line -> http://line.me/ti/p/zNkQ4FqYmc 
[ Note ]
[√] Pergunakanlah Dengan Bijak •

[ Admin -23 Selfbot ]

[©opy ®ight 2018 ]"""

protect = {
    "kick":{}
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops != None:
          for op in ops:
            if op.type == 19:
                if op.param1 in protect["kick"]:
                    if op.param2 in renBot:
                        pass
                    else:
                        try:
                            random.choice(KCML).kickoutFromGroup(op.param1, [op.param2])
                        except:
                            client.kickoutFromGroup(op.param1, [op.param2])
                else:
                    pass
            if op.type == 19:
                if op.param3 in clientMid:
                    if op.param2 not in renBot:
                        assist.kickoutFromGroup(op.param1, [op.param2])
                        P = assist.getGroup(op.param1)
                        P.preventedJoinByTicket = False
                        assist.updateGroup(P)
                        invsend = 0
                        Ticket = assist.reissueGroupTicket(op.param1)
                        client.acceptGroupInvitationByTicket(op.param1, Ticket)
                        A = assist.getGroup(op.param1)
                        A.preventedJoinByTicket = False
                        assist.updateGroup(A)
                if op.param3 in assistMid:
                    if op.param2 not in renBot:
                        client.kickoutFromGroup(op.param1, [op.param2])
                        P = client.getGroup(op.param1)
                        P.preventedJoinByTicket = False
                        client.updateGroup(P)
                        invsend = 0
                        Ticket = client.reissueGroupTicket(op.param1)
                        assist.acceptGroupInvitationByTicket(op.param1, Ticket)
                        A = client.getGroup(op.param1)
                        A.preventedJoinByTicket = False
                        client.updateGroup(A)
            if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                msg.from_ = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType in [0,2]:
                            contact = client.getContact(sender)
                            if text.lower() == 'help':
                                client.sendText(receiver, vol)
                            elif text.lower() == 'me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == 'speed':
                                start = time.time()
                                client.sendText(receiver, "[ C H E C K ] : [sendText]")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "[T I M E Response] : \n%s" % (elapsed_time))
                            elif text.lower() == 'mention':
                                group = client.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    client.mention(receiver, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    client.mention(receiver, nm5)             
                            elif text.lower() == '.':
                                try:
                                    G = client.getGroup(receiver)
                                    G.preventedJoinByTicket = False
                                    client.updateGroup(G)
                                    invsend = 0
                                    Ticket = client.reissueGroupTicket(receiver)
                                    assist.acceptGroupInvitationByTicket(receiver, Ticket)
                                    X = client.getGroup(receiver)
                                    X.preventedJoinByTicket = True
                                    client.updateGroup(X)
                                except Exception as axsd:
                                    print(axsd)
                            elif text.lower() == ',':
                                assist.leaveGroup(receiver)
                            elif text.lower() == 'sideron':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                    client.sendText(receiver, "Cek sider on!")
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                            elif text.lower() == 'sideroff':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    client.sendText(receiver, "Check reader off!")
                                else:
                                    client.sendText(receiver, "Type sideron to get data siders")
                            elif text.lower() == ';':
                                restart_program()
                            elif text.lower().startswith("!"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in renBot:
                                        random.choice(KCML).kickoutFromGroup(receiver, [target])
                            elif text.lower().startswith("pkick"):
                                pset = text.split(":")
                                pk = text.replace(pset[0] + ":","")
                                if pk == "on":
                                    if receiver in protect["kick"]:
                                        client.sendText(receiver, "Protect kick already On!")
                                    else:
                                        protect["kick"][receiver] = True
                                        client.sendText(receiver, "Protect kick set On!")
                                if pk == "off":
                                    if receiver in protect["kick"]:
                                        del protect["kick"][receiver]
                                        client.sendText(receiver, "Protect kick set Off!")
                                    else:
                                        client.sendText(receiver, "Protect kick already Off!")
                         elif text.lower() == '1':
                                if msg.toType == 2:
                                    gs = client.getGroup(receiver)
                                    client.sendText(receiver,"2")
                                    targets = []
                                    for g in gs.members:
                                        targets.append(g.mid)
                                    if targets == []:
                                        client.sendText(receiver, 'Attack By : Admin-23!')
                                    else:
                                        for target in targets:
                                            client.kickoutFromGroup(receiver, [target])
                                else:
                                    client.sendText(receiver, 'Lu ngapain onin selain di grup?')
                            elif text.lower().startswith("broadcast"):
                                txt = text.split(" ")
                                tastk = text.replace(txt[0] + " ","")
                                sx = client.getGroupIdsJoined()
                                for ak in sx:
                                    client.sendText(receiver, '[ B R O A D C A S T ]\n' + ak)
                elif text.lower() == 'gcreator':
                    group = boteater.getGroup(to)
                    GS = group.creator.mid
                    boteater.sendContact(to, GS)
                elif text.lower() == 'gpicture':
                    group = boteater.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    boteater.sendImageWithURL(to, path)
                elif text.lower() == 'glink':
                    if msg.toType == 2:
                        group = boteater.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            link = boteater.reissueGroupTicket(to)
                            boteater.sendMessage(to, ">> LINK GRUP <<<\nhttps://line.me/R/ti/g/{}".format(str(link)))
                        else:
                            boteater.sendMessage(to, "QR NYA DI CLOSE")
                elif text.lower() == 'qr on':
                    if msg.toType == 2:
                        group = boteater.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            boteater.sendMessage(to, "QR GRUP SUDAH DI OPEN!!!")
                        else:
                            group.preventedJoinByTicket = False
                            boteater.updateGroup(group)
                            boteater.sendMessage(to, "GRUP QR OPENED!!!")
                elif text.lower() == 'qr off':
                    if msg.toType == 2:
                        group = boteater.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            boteater.sendMessage(to, "QR GRUP SUDAH DI CLOSE!!!")
                        else:
                            group.preventedJoinByTicket = True
                            boteater.updateGroup(group)
                            boteater.sendMessage(to, "GRUP QR CLOSED!!!")
                elif text.lower() == 'ginfo':
                    group = boteater.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "GRUP CREATOR HILANG!!!"
                    if group.preventedJoinByTicket == True:
                        gQr = "CLOSED"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "OPEN"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(boteater.reissueglink(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = ">>> GRUP INFO <<<"
                    ret_ += "\nNAMA GRUP : {}".format(str(group.name))
                    ret_ += "\nCREATOR GRUP : {}".format(str(gCreator))
                    ret_ += "\nJUMBLAH MEMBER : {}".format(str(len(group.members)))
                    ret_ += "\nGRUP QR : {}".format(gQr)
                    ret_ += "\nLINK JOIN : {}".format(gTicket)
                    boteater.sendMessage(to, str(ret_))
                    boteater.sendImageWithURL(to, path)
                elif text.lower() == 'gmember':
                    if msg.toType == 2:
                        group = boteater.getGroup(to)
                        ret_ = ">>> LIST MEMBER <<<"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\nTOTAL MEMBER: \n{}".format(str(len(group.members)))
                        boteater.sendMessage(to, str(ret_))
                elif text.lower() == 'glist':
                        groups = boteater.groups
                        ret_ = ">>> LIST GRUP <<<"
                        no = 0 + 1
                        for gid in groups:
                            group = boteater.getGroup(gid)
                            ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\nTOTAL GRUP : \n{}".format(str(len(groups)))
                        boteater.sendMessage(to, str(ret_))
                          if op.type == 5:
                        print ("INFO SELBOT : ADA YANG ADD")
                        if settings["autoAdd"] == True:
                                boteater.sendMessage(op.param1, "=== Admin-23 Bot Publik V.01 === \nTERIMAKASIH {} TELAH ADD SAYA".format(str(boteater.getContact(op.param1).displayName)))
                if op.type == 13:
                        print ("INFO SELBOT : ADA YANG INVITE GRUP")
                        group = boteater.getGroup(op.param1)
                        if settings["autoJoin"] == True:
                                boteater.acceptGroupInvitation(op.param1)
                if op.type == 24:
                        print ("INFO SELBOT : LEAVE ROOM")
                        if settings["autoLeave"] == True:
                                boteater.leaveRoom(op.param1)
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                client.sendText(op.param1, 'Terbaca oleh: '+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
