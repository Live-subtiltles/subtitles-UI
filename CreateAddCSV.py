import os
import csv

def newcsv(dirpathaudio,dirpathtext,output):

        filesaudiotemp = os.listdir(dirpathaudio)  #function that puts every file name in the folder into a list
        filesaudio = sorted(filesaudiotemp)
        filestexttemp = os.listdir(dirpathtext)
        filestext = sorted(filestexttemp)

        filesizes = ['wav_filesize']           #the different 1D arrays that get put into the csv, with the first space in each being filled with the column name
        file_locations_audio=['wav_filename']   
        filestextcontents=['transcript']


        for filename in filesaudio:                                            #iterates for each file in the folder ('filename' I think comes from the 'os' library)
                string = list(filename)


                
                filesize = os.path.getsize(dirpathaudio + '/' + filename)      #returns the size of the file in bytes
                filesizes.append(filesize)                                     #adds that value to the end of the list of filesizes
                filelocationaudio = (dirpathaudio + '/' + filename)            #creates string of the full location of each file by appending the folder location and the file name
                file_locations_audio.append(filelocationaudio)                 #adds the location to the list



        for filename in filestext:                                             
                with open(dirpathtext + '/' + filename) as afile:                  #opens the file, and allows it to be referenced by 'afile' for simplicity
                        textfilecontents = afile.read()                                #Puts the entire contents of the file into one string variable

                        for ch in ['\\','`','‘','’','*','_',',','"','{','}','[',']','(',')','>','#','+','-','.','!','$',':',';','|','~','@','*','<','?','/']:          #This just filters out characters that aren't recognised by deepspeech
                                if ch in textfilecontents:
                                        textfilecontents = textfilecontents.replace(ch,"")
                                elif ch == '&':
                                        textfilecontents = textfilecontents.replace(ch,"and")

                        filestextcontents.append(textfilecontents)                    #Appends content of each file to list

        mat = [p for p in zip(file_locations_audio,filesizes,filestextcontents)]           #creates matrix by adding each list together 'side by side' kind of (I found this on a forum, not entirely sure how it works but it does)

        with open(output, 'w', newline='') as outfile:                              #The code that writes to the csv. It writes the whole matrix at once, automatically putting each element in a different cell.
                    csvout = csv.writer(outfile)
                    csvout.writerows(mat)
                    outfile.close()

createnew = input('Create a new CSV? Y/N')
if createnew == 'Y':
        dirpathaudio = input('Enter the audio folder path:')
        dirpathtext = input('Enter the transcript folder path:')
        output = input('Enter the output CSV path:')

        newcsv(dirpathaudio,dirpathtext,output)

finish = input('Would you like to add more files to current/other csv? Y/N')

while finish == 'Y':
        dirpathaudio = input('Enter the audio folder path:')
        dirpathtext = input('Enter the transcript folder path:')
        output = input('Enter the output CSV path:')

        filesaudiotemp = os.listdir(dirpathaudio)
        filesaudio = sorted(filesaudiotemp)
        filestexttemp = os.listdir(dirpathtext)
        filestext = sorted(filestexttemp)

        filesizes = []
        file_locations_audio=[]   
        filestextcontents=[]

        for filename in filesaudio:
                print(filename)
                filesize = os.path.getsize(dirpathaudio + '/' + filename)      
                filesizes.append(filesize)                                     
                filelocationaudio = (dirpathaudio + '/' + filename)            
                file_locations_audio.append(filelocationaudio)                 


        for filename in filestext:                                             
                with open(dirpathtext + '/' + filename) as afile:                  
                        textfilecontents = afile.read()                                

                        for ch in ['\\','`','‘','’','*','_',',','"','{','}','[',']','(',')','>','#','+','-','.','!','$',':',';','|','~','@','*','<','?','/']:          
                                if ch in textfilecontents:
                                        textfilecontents = textfilecontents.replace(ch,"")
                                elif ch == '&':
                                        textfilecontents = textfilecontents.replace(ch,"and")

                        filestextcontents.append(textfilecontents)                    

        mat = [p for p in zip(file_locations_audio,filesizes,filestextcontents)]           

        with open(output, 'a', newline='') as outfile:                              
                    csvout = csv.writer(outfile)
                    csvout.writerows(mat)
                    outfile.close()
        finish = input('Would you like to add more files to current/other csv? Y/N')





