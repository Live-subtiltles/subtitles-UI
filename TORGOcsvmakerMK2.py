import os
import csv
from num2words import num2words

torgopath = input('Enter the TORGO organised folder path:')
output = input('Enter the output CSV path:')

initialmat = ['wav_filesize', 'wav_filename', 'transcript']

with open(output, 'w', newline='') as outfile:
    csvout = csv.writer(outfile, delimiter=',')
    csvout.writerow(initialmat)
    outfile.close()

patients = os.listdir(torgopath)

for folder in patients:
    sessions = os.listdir(torgopath + '\\' + folder)
    for session in sessions:

        dirpathaudio = (torgopath + '\\' + folder + '\\' + session + '\\audio')
        dirpathtext = (torgopath + '\\' + folder+ '\\' + session + '\\text')

        filetranscripts = []
        filesizes = []
        filelocations = []

        filesaudiotemp = os.listdir(dirpathaudio)
        filesaudio = sorted(filesaudiotemp)
        filestexttemp = os.listdir(dirpathtext)
        filestext = sorted(filestexttemp)


        for filename in filestext:
            with open(dirpathtext + '\\' + filename) as afile:
                textfilecontents = afile.read().strip()
                
                if (len(textfilecontents.split()) > 1) and ('[' not in textfilecontents) and ('1' not in textfilecontents):
                    
                    # for char in textfilecontents:
                    #   if char.isdigit():
                    #    print("found digit",char)
                    #    integer = int(char)
                    #    chartemp = num2words(integer)
                    #    textfilecontents = textfilecontents.replace(char, chartemp)

                    for ch in ['\\', '`', '‘', '’', '*', '_', ',', '"', '{', '}', '[', ']', '(', ')', '>', '#', '+', '-', '.', '!', '$', ':', ';', '|', '~', '@', '*', '<', '?', '/',"'"]:
                        if ch in textfilecontents:
                            textfilecontents = textfilecontents.replace(ch, "")
                        elif ch == '&':
                            textfilecontents = textfilecontents.replace(ch, "and")
                                        
                    filetranscripts.append(textfilecontents.lower())
                    tempfilename = filename.replace('.txt', '.wav')
                    if tempfilename in filesaudio:
                        filesize = os.path.getsize(dirpathaudio + '\\' + tempfilename)
                        filesizes.append(filesize)
                        filelocationaudio = (dirpathaudio + '\\' + tempfilename)
                        filelocations.append(filelocationaudio)

                else:
                    continue

        mat = [p for p in zip(filelocations, filesizes, filetranscripts)]

        with open(output, 'a',newline='') as outfile:
            csvout = csv.writer(outfile)
            csvout.writerows(mat)
            outfile.close()
