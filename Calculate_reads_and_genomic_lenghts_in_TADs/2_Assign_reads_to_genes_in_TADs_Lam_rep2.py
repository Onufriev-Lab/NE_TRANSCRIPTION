#Assign reads to the genes in TADs


import os


ori_file = "TAD5.12.txt"
convert_file = "GSM3449351_RNA_Lam_rep2.txt"


dict = {} 
with open(convert_file) as fp:
    #first line is label
    line = fp.readline()
    line = fp.readline()
    while line:
        values = line.split()
        #print(values)
        dict[values[0]] = values[1]
        line = fp.readline()
        #line_count = line_count + 1

f= open("Genes_Reads_Lam_rep2.txt","w+")
with open(ori_file) as fp:
    #First line is label
    line = fp.readline()
    f.write(line)
    line = fp.readline()
    while line:
        values = line.split()
        if(values[0].startswith("TAD")): #or values[0].startswith("END")):
            f.write(line)
            line = fp.readline()
            values = line.split()
        if(values[0].startswith("END")):
            f.write(line)
            line = fp.readline()
            f.write(line)
            line = fp.readline()
            f.write(line)
            line = fp.readline()
            values = line.split()
        if (len(values) == 0):
            break
        #print(values[0])
        f.write("\t%s\t%s\n" % (values[0],  dict.get(values[0]))) 
        line = fp.readline()
