#Calculate sums of reads in each TAD

import os

ori_file = "TAD5.12.txt"
convert_file = "GSM3449349_RNA_LacZ_rep2.txt"


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

f= open("TADs_Reads_LacZ_rep2.txt","w+")
with open(ori_file) as fp:
    #First line is label
    line = fp.readline()
    #f.write(line)
    line = fp.readline()
    tad_count = 1
    tad_gene_count = 0
    tad_total = 0
    while line:
        values = line.split()
        if(values[0].startswith("TAD")): #or values[0].startswith("END")):
            #f.write(tad_count)
            line = fp.readline()
            values = line.split()
        if(values[0].startswith("END")):
            f.write("%d" % tad_count)
            if (tad_gene_count == 0):
                f.write("\t0\n")
            if (not tad_gene_count == 0):
                f.write("\t%d\n" % (tad_total))
            

            tad_gene_count = 0
            tad_total = 0
            #f.write(tad_count)
            tad_count = tad_count + 1
            #f.write(line)
            line = fp.readline()
            #f.write(line)
            line = fp.readline()
            #f.write(line)
            line = fp.readline()
            values = line.split()
        if (len(values) == 0):
            break
        #print(values[0])
        
        #f.write("\t%s\t%s\n" % (values[0],  dict.get(values[0])))
        if (dict.get(values[0]) is not None and dict.get(values[0]).isdigit()):
            tad_total = tad_total + float(dict.get(values[0]))
            tad_gene_count += 1
        #print(dict[values[1]])
        line = fp.readline()
