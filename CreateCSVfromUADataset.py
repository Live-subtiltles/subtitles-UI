+import os
import csv

audiofolderpath = ''
output = ''
textfolderpath = ''

audiofolders = os.listdir(audiofolderpath)
textfolders = os.listdir(textfolderpath)

filesizes = []
filelocations=[]
filetranscripts =[]
print("stage 1....")
for foldername in audiofolders:
    tempaudiofiles = os.listdir(audiofolderpath+'/'+foldername)
    if foldername in textfolders:
        textmlf = (textfolderpath+foldername+'/'+foldername+'_word.mlf')
    print("stage 2....")
    for filename in tempaudiofiles:
        size = len(filename)
        check = filename[size-6]+filename[size-5]
       
        if check == 'M3':
            filesizes.append(os.path.getsize(audiofolderpath+'/'+foldername+'/'+filename))
            filelocations.append(audiofolderpath+'/'+foldername+'/'+filename)

            substring = filename[0:(size-4)]
            with open(textmlf, 'r') as f:
                lines = iter(f.readlines())
                for item in lines:
                    if substring in item:
                        transcript = next(lines)
                        transcript = transcript.strip()
                        filetranscripts.append(transcript.lower())
        

mat = [p for p in zip(filelocations,filesizes,filetranscripts)]
with open(output, 'a', newline='') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerows(mat)
    outfile.close()
