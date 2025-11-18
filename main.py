import subprocess
import time
import uuid

from keep_alive import keep_alive

keep_alive()

if not os.path.isfile("./prime.txt"):
  guid = uuid.uuid1()
  with open("./prime.txt", mode="w") as f:
    f.write('''
NumWorkers=1
WorkPreference=0
CoresPerTest=4
ComputerGUID={}
StressTester=0
UsePrimenet=1
V5UserID=t112358f
ComputerID=replit
WorkerDiskSpace=6
ProofResiduesDir=
ProofArchiveDir=
Memory=2048 during 7:30-23:30 else 2048
MaxEmergencyMemory=1024
CertDailyCPULimit=10
CertWork=1
PRPGerbiczCompareIntervalAdj=1
Priority=1
DaysOfWork=3
RunOnBattery=1

[Internals]
OldCpuSpeed=3392
NewCpuSpeedCount=0
NewCpuSpeed=0
V30OptionsConverted=1
WGUID_version=2
Pid=202
SrvrUID=257526171
SrvrComputerName=1085757463
SrvrPO1=0
SrvrPO2=1
SrvrPO3=3
SrvrPO4=2048
SrvrPO5=2048
SrvrPO6=450
SrvrPO7=1410
SrvrPO8=1
SrvrPO9=1
SrvrP00=3
LastEndDatesSent=1763386339
CertDailyRemainingLastUpdate=1763442544
CertDailyMBRemaining=40
CertDailyCPURemaining=10
RollingHash=1349642207
RollingStartTime=1763405985
RollingCompleteTime=753219
RollingAverage=1260

[PrimeNet]
DialUp=0
ProxyHost=
UploadRateLimit=1
UploadStartTime=00:00
UploadEndTime=24:00
DownloadDailyLimit=40
    '''.format(guid))

subprocess.run(["chmod", "777", "./mprime"])
p = subprocess.Popen(["./mprime", "-m"], stdin=subprocess.PIPE)
time.sleep(5)
p.stdin.write("4\n".encode())
p.stdin.flush()

while True:
  input()
