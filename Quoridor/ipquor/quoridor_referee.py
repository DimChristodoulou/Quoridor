#! /usr/bin/env python
import sys
import os
import subprocess
import signal
import atexit
from time import time
from getopt import getopt
from select import select
TEJHXE=0
oiOZFx=1
QFltAr=2
XwlrFA=0
fqMXOa=1
iUHDEw=2
class QfefNy(object):
 ipqVbU=0
 gMQjtG=0
 ozospI=XwlrFA
 def __init__(self,ipqVbU,gMQjtG,ozospI):
  self.ipqVbU=ipqVbU
  self.gMQjtG=gMQjtG
  self.ozospI=ozospI
class vNQcFu(object):
 path=""
 name=None
 subprocess=None
 LvnKSq=TEJHXE
 WkhYlB=0
 ipqVbU=0
 gMQjtG=0
 gamesWon=0
 time_left=0
 last_command=""
 running=False
 def __init__(self,LvnKSq):
  self.LvnKSq=LvnKSq
 def readName(self):
  self.write("name")
  s=self.read()
  if s is None:
   self.timeOut("response")
   return
  if s.startswith("="):
   self.name=s[1:].strip()
  else:
   unexpectedOutput(self,s)
   slef.name=self.path
 def run(self):
  try:
   self.subprocess=subprocess.Popen(["./"+self.path,"-seed",str(seed)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,bufsize=0)
  except:
   print("Could not execute %s, quiting..."%mdiVZe.DigkJE.getTitle())
   sys.exit(4)
  self.running=True
  self.readName()
 def kill(self):
  try:
   os.kill(self.subprocess.pid,signal.SIGINT)
  except:
   print("Could not kill %s"%self.getTitle())
  self.running=False
 def winner(self):
  if(self.LvnKSq==QFltAr and self.gMQjtG==mdiVZe.gPVHyw-1)or(self.LvnKSq==oiOZFx and self.gMQjtG==0):
   return True
  return False
 def memory(self):
  return int(os.popen("ps -o vsz %d | tail -n 1"%self.subprocess.pid).readline())
 def getTitle(self):
  if self.LvnKSq==QFltAr:
   LvnKSq="black"
  else:
   LvnKSq="white"
  if self.name is None:
   title=self.path
  else:
   title=self.name
  return "%s (%s player)"%(title,LvnKSq)
 def write(self,s):
  try:
   self.subprocess.stdin.write((s+'\n').encode("utf-8"))
   self.subprocess.stdin.flush()
   self.last_command=s
  except:
   notResponding(self)
 def timeOut(self,s):
  if verbose>0:
   print("time out waiting for %s from %s after command: \"%s\""%(s,self.getTitle(),self.last_command))
 def read(self,timeout=2):
  start_time=time()
  try:
   if select([self.subprocess.stdout],[],[],timeout)[0]:
    s=self.subprocess.stdout.readline().decode("utf-8").strip()
   else:
    return None
   while s=="" or s.startswith('#'):
    if s.startswith('#')and verbose>0:
     print("%s comments: %s"%(self.getTitle(),s))
    if select([self.subprocess.stdout],[],[],timeout-(time()-start_time))[0]:
     s=self.subprocess.stdout.readline().decode("utf-8").strip()
    else:
     return None
   return s
  except:
   notResponding(self)
 def readOK(self):
  s=self.read()
  while s!="=":
   if s is None:
    self.timeOut("'='")
    return 0
   unexpectedOutput(self,s)
   s=self.read()
  return 1
 def readMove(self,timeout):
  start_time=time()
  line=self.read(timeout)
  if line is None:
   return None
  while(not line.startswith("="))or len(line)<3:
   unexpectedOutput(self,line)
   line=self.read(timeout-(time()-start_time))
   if line is None:
    return None
  s=line[1:].strip().split()
  ipqVbU,gMQjtG=mdiVZe.stringToCoords(s[0])
  if len(s)==1:
   return XwlrFA,ipqVbU,gMQjtG
  else:
   s=s[1].lower()
   if s=="h" or s=="horizontal":
    ozospI=fqMXOa
   elif s=="v" or s=="vertical":
    ozospI=iUHDEw
   else:
    unexpectedOutput(self,line)
    return self.readMove(timeout-(time()-start_time))
   return ozospI,ipqVbU,gMQjtG
 def readWinner(self):
  while True:
   line=self.read()
   if line is None:
    self.timeOut("response")
    return TEJHXE
   if line.startswith("?"):
    unexpectedOutput(self,line)
    continue
   s=line[1:].strip().lower()
   if s=="true white":
    return oiOZFx
   elif s=="true black":
    return QFltAr
   elif s=="false":
    return TEJHXE
   else:
    unexpectedOutput(self,line)
class HgbQxn(object):
 gPVHyw=9
 WkhYlB=[]
 DigkJE=vNQcFu(QFltAr)
 JReXWh=vNQcFu(oiOZFx)
 def coordsToString(self,ipqVbU,gMQjtG):
  return "%c%d"%(ord("A")+ipqVbU,self.gPVHyw-gMQjtG)
 def stringToCoords(self,s):
  ipqVbU=ord(s[0].lower())-ord('a')
  gMQjtG=self.gPVHyw-int(s[1:3])
  return ipqVbU,gMQjtG
 def orientationToString(self,ozospI):
  if ozospI==fqMXOa:
   return "horizontal"
  elif ozospI==iUHDEw:
   return "vertical"
  else:
   return "unknown orientation"
 def gdlHUU(self,ipqVbU,gMQjtG,ozospI):
  for jiRSVU in self.WkhYlB:
   if jiRSVU.ipqVbU==ipqVbU and jiRSVU.gMQjtG==gMQjtG and jiRSVU.ozospI==ozospI:
    return True
  return False
 def NjqeRR(self):
  sys.stdout.write("\n     ")
  for j in range(0,self.gPVHyw):
   sys.stdout.write("%c   "%(ord('A')+j))
  print("")
  for i in range(0,self.gPVHyw):
   sys.stdout.write("   ")
   for j in range(0,self.gPVHyw):
    if self.gdlHUU(j-1,i-1,fqMXOa):
     sys.stdout.write('=')
    elif self.gdlHUU(j-1,i-1,iUHDEw):
     sys.stdout.write('H'.encode("utf-8"))
    else:
     sys.stdout.write('+')
    if self.gdlHUU(j-1,i-1,fqMXOa)or self.gdlHUU(j,i-1,fqMXOa):
     sys.stdout.write("===")
    else:
     sys.stdout.write("---")
   print("+")
   sys.stdout.write("%2d "%(self.gPVHyw-i))
   for j in range(0,self.gPVHyw):
    if self.gdlHUU(j-1,i-1,iUHDEw)or self.gdlHUU(j-1,i,iUHDEw):
     sys.stdout.write('H'.encode("utf-8"))
    else:
     sys.stdout.write('|')
    if self.DigkJE.ipqVbU==j and self.DigkJE.gMQjtG==i:
     sys.stdout.write(" B ")
    elif self.JReXWh.ipqVbU==j and self.JReXWh.gMQjtG==i:
     sys.stdout.write(" W ")
    else:
     sys.stdout.write("   ")
   sys.stdout.write("| %d"%(self.gPVHyw-i))
   if i==0:
    print("  black walls: %2d"%self.DigkJE.WkhYlB)
   elif i==1:
    print("  white walls: %2d"%self.JReXWh.WkhYlB)
   else:
    print("")
  sys.stdout.write("   ")
  for j in range(0,self.gPVHyw):
   sys.stdout.write("+---")
  sys.stdout.write("+\n     ")
  for j in range(0,self.gPVHyw):
   sys.stdout.write("%c   "%(ord('A')+j))
  print("\n")
 def gENxzU(self,kHahDp,KCcXvc,ipqVbU,gMQjtG):
  if kHahDp==ipqVbU:
   m=min(KCcXvc,gMQjtG)
   M=max(KCcXvc,gMQjtG)
   for i in range(m,M):
    if self.gdlHUU(kHahDp,i,fqMXOa)or(kHahDp>0 and self.gdlHUU(kHahDp-1,i,fqMXOa)):
     return True
  elif KCcXvc==gMQjtG:
   m=min(kHahDp,ipqVbU)
   M=max(kHahDp,ipqVbU)
   for i in range(m,M):
    if self.gdlHUU(i,KCcXvc,iUHDEw)or(KCcXvc>0 and self.gdlHUU(i,KCcXvc-1,iUHDEw)):
     return True
  else:
   return True
  return False
 def sgGkwU(self,ipqVbU,gMQjtG,OLmzwf):
  if ipqVbU<0 or gMQjtG<0 or ipqVbU>=self.gPVHyw or gMQjtG>=self.gPVHyw:
   return False
  if(self.DigkJE.ipqVbU==ipqVbU and self.DigkJE.gMQjtG==gMQjtG)or(self.JReXWh.ipqVbU==ipqVbU and self.JReXWh.gMQjtG==gMQjtG):
   return False
  qZvMUM=abs(OLmzwf.ipqVbU-ipqVbU)+abs(OLmzwf.gMQjtG-gMQjtG)
  if qZvMUM==1:
   if self.gENxzU(OLmzwf.ipqVbU,OLmzwf.gMQjtG,ipqVbU,gMQjtG):
    return False
   return True
  elif qZvMUM==2 and(OLmzwf.ipqVbU==ipqVbU or OLmzwf.gMQjtG==gMQjtG):
   XalOFV=(OLmzwf.ipqVbU+ipqVbU)/2
   lWNYZI=(OLmzwf.gMQjtG+gMQjtG)/2
   if not((self.DigkJE.ipqVbU==XalOFV and self.DigkJE.gMQjtG==lWNYZI)or(self.JReXWh.ipqVbU==XalOFV and self.JReXWh.gMQjtG==lWNYZI)):
    return False
   if self.gENxzU(OLmzwf.ipqVbU,OLmzwf.gMQjtG,ipqVbU,gMQjtG):
    return False
   return True
  elif qZvMUM==2:
   if OLmzwf.LvnKSq==QFltAr:
    wTcotp=self.JReXWh
   else:
    wTcotp=self.DigkJE
   if(abs(OLmzwf.ipqVbU-wTcotp.ipqVbU)+abs(OLmzwf.gMQjtG-wTcotp.gMQjtG))!=1:
    return False
   RgXGCH=OLmzwf.ipqVbU
   KELBFN=OLmzwf.gMQjtG
   if OLmzwf.ipqVbU+1==wTcotp.ipqVbU:
    RgXGCH=OLmzwf.ipqVbU+2
   elif OLmzwf.ipqVbU-1==wTcotp.ipqVbU:
    RgXGCH=OLmzwf.ipqVbU-2
   elif OLmzwf.gMQjtG+1==wTcotp.gMQjtG:
    KELBFN=OLmzwf.gMQjtG+2
   elif OLmzwf.gMQjtG-1==wTcotp.gMQjtG:
    KELBFN=OLmzwf.gMQjtG-2
   else:
    return False
   if(RgXGCH<0 or RgXGCH>=self.gPVHyw or KELBFN<0 or KELBFN>=self.gPVHyw or self.gENxzU(wTcotp.ipqVbU,wTcotp.gMQjtG,RgXGCH,KELBFN))and not self.gENxzU(OLmzwf.ipqVbU,OLmzwf.gMQjtG,wTcotp.ipqVbU,wTcotp.gMQjtG)and not self.gENxzU(wTcotp.ipqVbU,wTcotp.gMQjtG,ipqVbU,gMQjtG):
    return True
  return False
 def aWAFmq(self,ipqVbU,gMQjtG,OLmzwf):
  if self.sgGkwU(ipqVbU,gMQjtG,OLmzwf)!=1:
   return False
  OLmzwf.ipqVbU=ipqVbU
  OLmzwf.gMQjtG=gMQjtG
  return True
 def LKeUDO(self,OLmzwf,JOLkLJ):
  if OLmzwf.winner():
   return True
  ipqVbU=OLmzwf.ipqVbU
  gMQjtG=OLmzwf.gMQjtG
  JOLkLJ[ipqVbU][gMQjtG]=1
  if OLmzwf.LvnKSq==QFltAr:
   JRQVhA=1
  else:
   JRQVhA=-1
  if self.aWAFmq(ipqVbU,gMQjtG+JRQVhA,OLmzwf):
   if not JOLkLJ[ipqVbU][gMQjtG+JRQVhA]and self.LKeUDO(OLmzwf,JOLkLJ):
    return True
  OLmzwf.gMQjtG=gMQjtG
  if self.aWAFmq(ipqVbU+1,gMQjtG,OLmzwf):
   if not JOLkLJ[ipqVbU+1][gMQjtG]and self.LKeUDO(OLmzwf,JOLkLJ):
    return True
  OLmzwf.ipqVbU=ipqVbU
  if self.aWAFmq(ipqVbU-1,gMQjtG,OLmzwf):
   if not JOLkLJ[ipqVbU-1][gMQjtG]and self.LKeUDO(OLmzwf,JOLkLJ):
    return True
  OLmzwf.ipqVbU=ipqVbU
  if self.aWAFmq(ipqVbU,gMQjtG-JRQVhA,OLmzwf):
   if not JOLkLJ[ipqVbU][gMQjtG-JRQVhA]and self.LKeUDO(OLmzwf,JOLkLJ):
    return True
  OLmzwf.gMQjtG=gMQjtG
  return False
 def fKMJLA(self):
  JOLkLJ=[[0 for i in range(self.gPVHyw)]for j in range(self.gPVHyw)]
  XsYs=self.DigkJE.ipqVbU,self.DigkJE.gMQjtG,self.JReXWh.ipqVbU,self.JReXWh.gMQjtG
  self.JReXWh.ipqVbU=-1
  self.JReXWh.gMQjtG=-1
  if not self.LKeUDO(self.DigkJE,JOLkLJ):
   self.DigkJE.ipqVbU,self.DigkJE.gMQjtG,self.JReXWh.ipqVbU,self.JReXWh.gMQjtG=XsYs
   return False
  JOLkLJ=[[0 for i in range(self.gPVHyw)]for j in range(self.gPVHyw)]
  _,_,self.JReXWh.ipqVbU,self.JReXWh.gMQjtG=XsYs
  self.DigkJE.ipqVbU=-1
  self.DigkJE.gMQjtG=-1
  if not self.LKeUDO(self.JReXWh,JOLkLJ):
   self.DigkJE.ipqVbU,self.DigkJE.gMQjtG,self.JReXWh.ipqVbU,self.JReXWh.gMQjtG=XsYs
   return False
  self.DigkJE.ipqVbU,self.DigkJE.gMQjtG,self.JReXWh.ipqVbU,self.JReXWh.gMQjtG=XsYs
  return True
 def dhFkAJ(self,ipqVbU,gMQjtG,ozospI):
  if ipqVbU<0 or gMQjtG<0 or ipqVbU>self.gPVHyw-2 or gMQjtG>self.gPVHyw-2:
   return False
  for jiRSVU in self.WkhYlB:
   if((jiRSVU.ipqVbU==ipqVbU and jiRSVU.gMQjtG==gMQjtG)or(jiRSVU.ipqVbU-1==ipqVbU and jiRSVU.gMQjtG==gMQjtG and jiRSVU.ozospI==ozospI and ozospI==fqMXOa)or(jiRSVU.ipqVbU+1==ipqVbU and jiRSVU.gMQjtG==gMQjtG and jiRSVU.ozospI==ozospI and ozospI==fqMXOa)or(jiRSVU.ipqVbU==ipqVbU and jiRSVU.gMQjtG-1==gMQjtG and jiRSVU.ozospI==ozospI and ozospI==iUHDEw)or(jiRSVU.ipqVbU==ipqVbU and jiRSVU.gMQjtG+1==gMQjtG and jiRSVU.ozospI==ozospI and ozospI==iUHDEw)):
    return False
  return True
 def XcWyCx(self,ipqVbU,gMQjtG,ozospI,OLmzwf):
  if OLmzwf.WkhYlB<=0 or not self.dhFkAJ(ipqVbU,gMQjtG,ozospI):
   return False
  self.WkhYlB.append(QfefNy(ipqVbU,gMQjtG,ozospI))
  if self.fKMJLA():
   OLmzwf.WkhYlB-=1
   return True
  else:
   self.WkhYlB.pop()
  return False
move_time=0
verbose=0
games=1
gameCounter=0
seed=int(time())
starting_walls=10
maximum_time=0
memory_limit=0
helpstring="""
Run with:
quoridor_referee.py --white \'<path to program 1>\' \                    --black \'<path to program 2>\' \
Possible quoridor_referee options:
  --verbose 1 (to list moves) or --verbose 2 (to draw board)
  --size <board size>               (default 9)
  --walls <number of walls>         (default 10)
  --games <number of games to play> (default 1)
  --maximum_time <time(in seconds)> (default not checking time)
  --move_time <time(in seconds)>    (default not checking time)
  --memory_limit <memory(in MB)>    (default not checking memory usage)
  --seed <seed>                     (default current unix timestamp)
"""
def usage():
 print(helpstring)
 sys.exit(2)
mdiVZe=HgbQxn()
def notResponding(OLmzwf):
 print("\n%s is not responding, quiting..."%OLmzwf.getTitle())
 sys.exit(6)
def invalidMove(LvnKSq,ipqVbU,gMQjtG,ozospI):
 if LvnKSq==QFltAr:
  winner=mdiVZe.JReXWh
  loser=mdiVZe.DigkJE
 else:
  winner=mdiVZe.DigkJE
  loser=mdiVZe.JReXWh
 if ozospI:
  move="%s %s"%(mdiVZe.coordsToString(ipqVbU,gMQjtG),mdiVZe.orientationToString(ozospI))
 else:
  move="%s"%mdiVZe.coordsToString(ipqVbU,gMQjtG)
 print("\n%s tried an invalid move: %s"%(loser.getTitle(),move))
 print("%s wins game %d\n"%(winner.getTitle(),gameCounter+1))
 print("--------------------")
def memoryExceed(LvnKSq):
 if LvnKSq==QFltAr:
  winner=mdiVZe.JReXWh
  loser=mdiVZe.DigkJE
 else:
  winner=mdiVZe.DigkJE
  loser=mdiVZe.JReXWh
 print("\n%s exceeded the memory limit"%loser.getTitle())
 print("%s wins game %d\n"%(winner.getTitle(),gameCounter+1))
 print("--------------------")
def timeOut(LvnKSq):
 if LvnKSq==QFltAr:
  winner=mdiVZe.JReXWh
  loser=mdiVZe.DigkJE
 else:
  winner=mdiVZe.DigkJE
  loser=mdiVZe.JReXWh
 print("\n%s ran out of time"%loser.getTitle())
 print("%s wins game %d\n"%(winner.getTitle(),gameCounter+1))
 loser.kill()
def unexpectedOutput(OLmzwf,s):
 if(verbose>0):
  print("unexpected output from %s: \"%s\" after command: \"%s\""%(OLmzwf.getTitle(),s,OLmzwf.last_command))
def winner(OLmzwf):
 print("\n%s wins game %d"%(OLmzwf.getTitle(),gameCounter+1))
 mdiVZe.DigkJE.write("winner")
 w1=mdiVZe.DigkJE.readWinner()
 mdiVZe.JReXWh.write("winner")
 w2=mdiVZe.JReXWh.readWinner()
 if w1==w2==OLmzwf.LvnKSq:
  print("both players agree")
 else:
  if w1!=OLmzwf.LvnKSq:
   print("%s disagrees"%mdiVZe.DigkJE.getTitle())
  else:
   print("%s agrees"%mdiVZe.DigkJE.getTitle())
  if w2!=OLmzwf.LvnKSq:
   print("%s disagrees"%mdiVZe.JReXWh.getTitle())
  else:
   print("%s agrees"%mdiVZe.JReXWh.getTitle())
 print("%s took %.2fs to decide its moves"%(mdiVZe.DigkJE.getTitle(),maximum_time-mdiVZe.DigkJE.time_left))
 print("%s took %.2fs to decide its moves"%(mdiVZe.JReXWh.getTitle(),maximum_time-mdiVZe.JReXWh.time_left))
 print("\n--------------------")
def initialize_game():
 if not mdiVZe.DigkJE.running:
  mdiVZe.DigkJE.run()
 if not mdiVZe.JReXWh.running:
  mdiVZe.JReXWh.run()
 mdiVZe.WkhYlB=[]
 mdiVZe.DigkJE.WkhYlB=starting_walls
 mdiVZe.JReXWh.WkhYlB=starting_walls
 mdiVZe.DigkJE.time_left=maximum_time
 mdiVZe.JReXWh.time_left=maximum_time
 mdiVZe.DigkJE.gMQjtG=int(0)
 mdiVZe.DigkJE.ipqVbU=int(mdiVZe.gPVHyw/2)
 mdiVZe.JReXWh.gMQjtG=int(mdiVZe.gPVHyw-1)
 mdiVZe.JReXWh.ipqVbU=int(mdiVZe.gPVHyw/2)
 mdiVZe.DigkJE.write("boardsize %d"%mdiVZe.gPVHyw)
 mdiVZe.DigkJE.readOK()
 mdiVZe.DigkJE.write("clear_board")
 mdiVZe.DigkJE.readOK()
 mdiVZe.DigkJE.write("walls %d"%starting_walls)
 mdiVZe.DigkJE.readOK()
 mdiVZe.JReXWh.write("boardsize %d"%mdiVZe.gPVHyw)
 mdiVZe.JReXWh.readOK()
 mdiVZe.JReXWh.write("clear_board")
 mdiVZe.JReXWh.readOK()
 mdiVZe.JReXWh.write("walls %d"%starting_walls)
 mdiVZe.JReXWh.readOK()
def playGame():
 initialize_game()
 print("\n\nGame %d starting now!\n"%(1+gameCounter))
 if verbose>1:
  mdiVZe.NjqeRR()
 while True:
  if memory_limit and mdiVZe.JReXWh.memory()>memory_limit*1024:
   memoryExceed(oiOZFx)
   return QFltAr
  mdiVZe.DigkJE.write("genmove black")
  start_time=time()
  move=mdiVZe.DigkJE.readMove(min(move_time,mdiVZe.DigkJE.time_left))
  mdiVZe.DigkJE.time_left-=time()-start_time
  if move:
   if move[0]:
    if not mdiVZe.XcWyCx(move[1],move[2],move[0],mdiVZe.DigkJE):
     invalidMove(QFltAr,move[1],move[2],move[0])
     return oiOZFx
    mdiVZe.JReXWh.write("playwall black %s %s"%(mdiVZe.coordsToString(move[1],move[2]),mdiVZe.orientationToString(move[0])))
    if verbose>0:
     print("%s places %s wall at %s"%(mdiVZe.DigkJE.getTitle(),mdiVZe.orientationToString(move[0]),mdiVZe.coordsToString(move[1],move[2])))
   else:
    if not mdiVZe.aWAFmq(move[1],move[2],mdiVZe.DigkJE):
     invalidMove(QFltAr,move[1],move[2],move[0])
     return oiOZFx
    mdiVZe.JReXWh.write("playmove black %s"%mdiVZe.coordsToString(move[1],move[2]))
    if verbose>0:
     print("%s moves to %s"%(mdiVZe.DigkJE.getTitle(),mdiVZe.coordsToString(move[1],move[2])))
   mdiVZe.JReXWh.readOK()
   if verbose>1:
    mdiVZe.NjqeRR()
   if mdiVZe.DigkJE.winner():
    winner(mdiVZe.DigkJE)
    return QFltAr
  else:
   timeOut(QFltAr)
   return oiOZFx
  if memory_limit and mdiVZe.DigkJE.memory()>memory_limit*1024:
   memoryExceed(QFltAr)
   return oiOZFx
  mdiVZe.JReXWh.write("genmove white")
  start_time=time()
  move=mdiVZe.JReXWh.readMove(min(move_time,mdiVZe.JReXWh.time_left))
  mdiVZe.JReXWh.time_left-=time()-start_time
  if move:
   if move[0]:
    if not mdiVZe.XcWyCx(move[1],move[2],move[0],mdiVZe.JReXWh):
     invalidMove(oiOZFx,move[1],move[2],move[0])
     return QFltAr
    mdiVZe.DigkJE.write("playwall white %s %s"%(mdiVZe.coordsToString(move[1],move[2]),mdiVZe.orientationToString(move[0])))
    if verbose>0:
     print("%s places %s wall at %s"%(mdiVZe.JReXWh.getTitle(),mdiVZe.orientationToString(move[0]),mdiVZe.coordsToString(move[1],move[2])))
   else:
    if not mdiVZe.aWAFmq(move[1],move[2],mdiVZe.JReXWh):
     invalidMove(oiOZFx,move[1],move[2],move[0])
     return QFltAr
    mdiVZe.DigkJE.write("playmove white %s"%mdiVZe.coordsToString(move[1],move[2]))
    if verbose>0:
     print("%s moves to %s"%(mdiVZe.JReXWh.getTitle(),mdiVZe.coordsToString(move[1],move[2])))
   mdiVZe.DigkJE.readOK()
   if(verbose>1):
    mdiVZe.NjqeRR()
   if mdiVZe.JReXWh.winner():
    winner(mdiVZe.JReXWh)
    return oiOZFx
  else:
   timeOut(oiOZFx)
   return QFltAr
print("Welcome to the Quoridor Tournament! I'm going to be your referee for this game")
print("Created by Teo Georgiou for the Introduction to Programming course, UoA, 2011")
print("Updated by John Vlachopoulos and Sotirios-Efstathios Maneas for the Introduction to Programming course, UoA, 2012-2013")
print("Updated by Spyros Avlonitis and Giannos Chatziagapis for the Introduction to Programming course, UoA, 2015")
print("\n--------------------\n\n")
try:
 (opts,params)=getopt(sys.argv[1:],"",["black=","white=","size=","walls=","verbose=","games=","maximum_time=","move_time=","memory_limit=","seed="])
 for opt,value in opts:
  if opt=="--black":
   mdiVZe.DigkJE.path=value
  elif opt=="--white":
   mdiVZe.JReXWh.path=value
  elif opt=="--size":
   mdiVZe.gPVHyw=int(value)
  elif opt=="--walls":
   starting_walls=int(value)
  elif opt=="--verbose":
   verbose=int(value)
  elif opt=="--games":
   games=int(value)
  elif opt=="--maximum_time":
   maximum_time=int(value)
  elif opt=="--move_time":
   move_time=float(value)
  elif opt=="--memory_limit":
   memory_limit=int(value)
  elif opt=="--seed":
   seed=int(value)
except:
 usage()
if mdiVZe.DigkJE.path=="" or mdiVZe.JReXWh.path=="":
 usage()
print("boardsize set to %d"%mdiVZe.gPVHyw)
print("walls set to %d"%starting_walls)
print("verbose set to %d"%verbose)
print("games set to %d"%games)
if maximum_time:
 print("maximum_time set to %d"%maximum_time)
else:
 maximum_time=31556926
if(move_time):
 print("move_time set to %.1f"%move_time)
else:
 move_time=31556926
print("seed set to %d"%seed)
if memory_limit:
 print("memory_limit set to %d"%memory_limit)
while not os.path.exists(mdiVZe.DigkJE.path):
 print("File %s does not exist, please specify the filename correctly"%mdiVZe.DigkJE.path)
 mdiVZe.DigkJE.path=input('> ')
if not os.access(mdiVZe.DigkJE.path,os.X_OK):
 print("File %s is not executable, quiting..."%mdiVZe.DigkJE.path)
 sys.exit(3)
while not os.path.exists(mdiVZe.JReXWh.path):
 print("File %s does not exist, please specify the filename correctly"%mdiVZe.JReXWh.path)
 mdiVZe.JReXWh.path=input('> ')
if not os.access(mdiVZe.JReXWh.path,os.X_OK):
 print("File %s is not executable, quiting..."%mdiVZe.JReXWh.path)
 sys.exit(3)
mdiVZe.DigkJE.run()
mdiVZe.JReXWh.run()
def cleanup():
 mdiVZe.DigkJE.kill()
 mdiVZe.JReXWh.kill()
atexit.register(cleanup)
f=open("last_game.sh","w")
f.write("#!/bin/bash\n\n")
if "--seed" not in sys.argv:
 sys.argv.append("--seed %d"%seed)
f.write(" ".join(sys.argv))
f.write("\n")
f.close()
mode=os.stat("last_game.sh").st_mode
mode|=(mode&0o444)>>2
os.chmod("last_game.sh",mode)
print("\n--------------------")
print("%s vs %s"%(mdiVZe.DigkJE.getTitle(),mdiVZe.JReXWh.getTitle()))
print("----------------------")
while gameCounter<games:
 i=playGame()
 if i==QFltAr:
  mdiVZe.DigkJE.gamesWon+=1
 else:
  mdiVZe.JReXWh.gamesWon+=1
 gameCounter+=1
if games>1:
 print("%s won %d games"%(mdiVZe.DigkJE.getTitle(),mdiVZe.DigkJE.gamesWon))
 print("%s won %d games"%(mdiVZe.JReXWh.getTitle(),mdiVZe.JReXWh.gamesWon))
 if mdiVZe.DigkJE.gamesWon>mdiVZe.JReXWh.gamesWon:
  print("\n%s wins!!"%mdiVZe.DigkJE.getTitle())
 elif mdiVZe.DigkJE.gamesWon<mdiVZe.JReXWh.gamesWon:
  print("\n%s wins!!"%mdiVZe.JReXWh.getTitle())
 else:
  print("\nIt's a tie!!")
 print("--------------------\n")
# Created by pyminifier (https://github.com/liftoff/pyminifier)

