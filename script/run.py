import csv

with open('input.csv') as inputfile, open('output.csv','w',newline='') as outputfile:
    spamreader = csv.reader(inputfile)
    spamwriter = csv.writer(outputfile)

    inputdata = [row for row in spamreader]
    outputdata = [['연월일시','구간','종명','개체수'],]

    x = len(inputdata[0])
    y = len(inputdata)

    for i in range(2,y):
        for j in range(1,x):
            if inputdata[i][j] == '':
                continue
            else:
                outputdata.append([inputdata[0][j],inputdata[1][j],inputdata[i][0],inputdata[i][j]])

    spamwriter.writerows(outputdata)
