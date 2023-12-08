
#chromatin_Dros_melanogaster - input folder

import pandas

'''
Parse and Print Functions
'''
def combineChromoAndTad(chromo_df, tad_df, fileName):
    file = open(fileName, "a")
    for tRow in tad_df.itertuples(index=True): #itertuples is fast
        tStart = tRow.StartLoc
        tEnd = tRow.EndLoc
        printList = []
        #Now we comsume the chromo_df until we reach a range above our bounds
        for cRow in chromo_df.itertuples(index=True):   
            #1 and 2 correspond to indicies for chromosome start and end location
            cStart = cRow[1]
            cEnd = cRow[2]
            #swap if backwards
            if cStart > cEnd:
                cStart,cEnd = cEnd,cStart 
            #elif (cStart>= tStart and cEnd<tEnd) or (cEnd>=tStart and cStart<=tStart) or (cStart<=tEnd and cEnd>=tEnd):
            elif (cStart>= tStart and cEnd<tEnd) or (cStart<=tEnd and cEnd>=tEnd):
                #add to list to print
                printList.append(cRow)
                chromo_df.drop(cRow[0],inplace=True)
            elif cStart>tEnd:
                break
        #Now we print stuff from printList
        printToDatabaseFile(printList,tRow,file)
    return


def printToDatabaseFile(printList, tRow, file):
    file.write("TAD "+str(tRow[1])+"\tChr: "+str(tRow[2])+"\tEpiClass: "+str(tRow[6])+"\n")
    if (len(printList)==0):
        file.write("-"+"\n")
    for i in printList:
         file.write(""+str(i[4])+"\n")
    file.write("END\n\n")

'''
Main section

Required file structure:
    All files to be parsed (X.txt, 2R.txt, etc.) must be under the specified directory. By default, ./chromatin_Dros_melanogaster is the directory.
    The AlberModel.txt must also be under this directory.
'''

#Make pandas dataframe the TAD mapping and each chromosome
#dataFolderPath = input("What is the path to the directory that contains AlberModel.txt, X.txt, 2R.txt, etc?\n./chromatin_Dros_melanogaster by default if no path entered\n")
#if dataFolderPath is None or dataFolderPath is "":
dataFolderPath = "./chromatin_Dros_melanogaster"
tadRange = pandas.read_csv(dataFolderPath+"/AlberModel.txt", sep='\t')
#fileName = input("Enter desired name for database file: \n")
fileName='TAD5.12.txt'
#fileName+="TAD5.12_start_position.txt"
print("Working")
for chromo, tad_df in tadRange.groupby("Chr"):
    #chromo contains the names of each chromosome
    #tad_df is a dataframe of the TAD mapping for each chromosome
    chromo_df = pandas.read_csv("./chromatin_Dros_melanogaster/"+chromo+".txt", sep=',')
    #Now we step through chromo_df and tad_df and build our output
    combineChromoAndTad(chromo_df,tad_df,fileName)
    print(chromo+ " loaded")
print("Completed, check "+fileName)
