import sys

#reads the lines of the input file
def get_input_file():
    with open(sys.argv[1], "r") as input_file:
        lines = input_file.readlines()
    return lines

#gets the limits, indexes and list I need to use 
def get_row(lines):
    row = []
    for i in lines:
        i = i.strip()
        numbers = list()
        for j in i.split():
            numbers.append(j)
        row.append(numbers)

    limits = []
    for i in range(4):
        limits2 = []
        for j in row[i]:
            limits2.append(int(j))
        limits.append(limits2)
    
    mylist = row[4:]

    #i need the indexes of the tiles to do backtracking 
    indexs = []
    for i in range(len(mylist)):
        for j in range(len(mylist[0])):
            if mylist[i][j] == "L":
                indexs.append([[i, j], [i, j+1]])
            elif mylist[i][j] == "U":
                indexs.append([[i, j], [i+1, j]])

    return limits, mylist, indexs


def get_list(lines):
    row = []
    for i in lines:
        i = i.strip()
        numbers = list()
        for j in i.split():
            numbers.append(j)
        row.append(numbers)
    
    mylist2 = row[4:]
    return mylist2


lines = get_input_file()
limits, listem3, indexes = get_row(lines)
listem = get_list(lines)


#checks the right neighbour
def right_control(i,j,k,m):
    #Right
    if j != len(listem[0])-1:
        if k[i][j+1] == m:
            return False
        else:
            return True
    else: 
        return True
            

#checks the left neighbour
def left_control(i,j,k,m):             
    #Left
    if j != 0:
        if k[i][j-1] == m:
            return False
        else:
            return True
    else:
        return True


#checks the upper neighbour
def up_control(i,j,k,m):            
    #up
    if i != len(k)-1:
        if k[i+1][j] == m:
            return False
        else:
            return True
    else:
        return True


#checks the under neighbour
def under_control(i,j,k,m):              
    #Under
    if i != 0:
        if k[i-1][j] == m:
            return False
        else:
            return True
    else:
        return True


#fills with HB, BH or NN to prepare the tiles for backtracking
def first_tiling(listem3,indexes,myindex2):
    if myindex2 == len(indexes):
        return listem3
    elif listem3[indexes[myindex2][0][0]][indexes[myindex2][0][1]] == "L" or listem3[indexes[myindex2][0][0]][indexes[myindex2][0][1]] == "U":
        m = "H"
        if (right_control(indexes[myindex2][0][0],indexes[myindex2][0][1],listem3,m) and left_control(indexes[myindex2][0][0],indexes[myindex2][0][1],listem3,m) and up_control(indexes[myindex2][0][0],indexes[myindex2][0][1],listem3,m) and under_control(indexes[myindex2][0][0],indexes[myindex2][0][1],listem3,m)):
            m = "B"
            if (right_control(indexes[myindex2][1][0],indexes[myindex2][1][1],listem3,m) and left_control(indexes[myindex2][1][0],indexes[myindex2][1][1],listem3,m) and up_control(indexes[myindex2][1][0],indexes[myindex2][1][1],listem3,m) and under_control(indexes[myindex2][1][0],indexes[myindex2][1][1],listem3,m)):
                listem3[indexes[myindex2][0][0]][indexes[myindex2][0][1]] = "H"
                listem3[indexes[myindex2][1][0]][indexes[myindex2][1][1]] = "B"
                return first_tiling(listem3,indexes,myindex2+1)
        elif not (right_control(indexes[myindex2][0][0],indexes[myindex2][0][1],listem3,m) and left_control(indexes[myindex2][0][0],indexes[myindex2][0][1],listem3,m) and up_control(indexes[myindex2][0][0],indexes[myindex2][0][1],listem3,m) and under_control(indexes[myindex2][0][0],indexes[myindex2][0][1],listem3,m)):
            m = "B"
            if (right_control(indexes[myindex2][0][0],indexes[myindex2][0][1],listem3,m) and left_control(indexes[myindex2][0][0],indexes[myindex2][0][1],listem3,m) and up_control(indexes[myindex2][0][0],indexes[myindex2][0][1],listem3,m) and under_control(indexes[myindex2][0][0],indexes[myindex2][0][1],listem3,m)):
                m = "H"
                if (right_control(indexes[myindex2][1][0],indexes[myindex2][1][1],listem3,m) and left_control(indexes[myindex2][1][0],indexes[myindex2][1][1],listem3,m) and up_control(indexes[myindex2][1][0],indexes[myindex2][1][1],listem3,m) and under_control(indexes[myindex2][1][0],indexes[myindex2][1][1],listem3,m)):
                    listem3[indexes[myindex2][0][0]][indexes[myindex2][0][1]] = "B"
                    listem3[indexes[myindex2][1][0]][indexes[myindex2][1][1]] = "H"
                    return first_tiling(listem3,indexes,myindex2+1)
        else:
            listem3[indexes[myindex2][0][0]][indexes[myindex2][0][1]] = "N"
            listem3[indexes[myindex2][1][0]][indexes[myindex2][1][1]] = "N"
            return first_tiling(listem3,indexes,myindex2+1)
        

#cheks the row limits
def limitsrow(limits,number):
    for i in range(len(number)):
        if limits[0][i] != -1:
            if number[i].count("H") != limits[0][i]:
                return False
    for i in range(len(number)):
        if limits[1][i] != -1:
            if number[i].count("B") != limits[1][i]:
                return False
    return True            


#cheks the col limits
def limitscol(limits,number):
    for i in range(len(number[0])):
        collist = []
        if limits[2][i] != -1:
            for j in range(len(number)):
                collist.append(number[j][i])
            if collist.count("H") != limits[2][i]:
                return False
    for i in range(len(number[0])):
        collist = []
        if limits[3][i] != -1:
            for j in range(len(number)):
                collist.append(number[j][i])
            if collist.count("B") != limits[3][i]:
                return False
    return True


#checks the right neighbour
def right_kontrol(i,j,no,m):
    #Right
    if j != len(listem[0])-1:
        if no[i][j+1] == m:
            return False
        else:
            return True
    else: 
        return True
            

#checks the left neighbour
def left_kontrol(i,j,no,m):             
    #Left
    if j != 0:
        if no[i][j-1] == m:
            return False
        else:
            return True
    else:
        return True


#checks the upper neighbour
def up_kontrol(i,j,no,m):            
    #Up
    if i != len(no)-1:
        if no[i+1][j] == m:
            return False
        else:
            return True
    else:
        return True

#checks the under neighbour
def under_kontrol(i,j,no,m):              
    #Under
    if i != 0:
        if no[i-1][j] == m:
            return False
        else:
            return True
    else:
        return True
    

#prints "no solution" to the file if the table has no solution
def no_solution():
    with open(sys.argv[2],"a+") as fileo:
        fileo.write("No solution!")
    return None


#prints the solution of the table to the file
def write_output(listem2):
    with open(sys.argv[2],"a+") as fileo:
        counter2 = 0
        for element_2 in listem2:    
            counter2 += 1
            counter = 0
            for i in element_2:
                fileo.write(str(i))
                counter += 1
                if not(counter == len(listem2[0])):
                    fileo.write(" ")
            if not(counter2 == len(listem2)):
                fileo.write("\n")
    return None


#solver function that finds the correct solution of the table by recursive and backtracking
def backtracking(listem2,listem3,indexes,myindex):
    #if I'm checking the last tile
    if myindex == len(indexes)-1:
        #if it's HB, try BH, if not, try NN 
        if listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] == "H":
            if limitsrow(limits,listem2) and limitscol(limits,listem2):
                write_output(listem2)
                return listem2
            #returns false if there is no solution after trying NN
            else:
                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                m = "B"
                if (right_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and left_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and up_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and under_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m)):
                    m = "H"
                    if (right_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and left_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and up_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and under_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m)):
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "B"
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "H"
                        if limitsrow(limits,listem2) and limitscol(limits,listem2):
                            write_output(listem2)
                            return listem2
                        elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                            if limitsrow(limits,listem2) and limitscol(limits,listem2):
                                write_output(listem2)
                                return listem2
                            elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                                return False   
                    else:
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                        if limitsrow(limits,listem2) and limitscol(limits,listem2):
                            write_output(listem2)
                            return listem2
                        elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                            return False     
                else:
                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                    if limitsrow(limits,listem2) and limitscol(limits,listem2):
                        write_output(listem2)
                        return listem2
                    elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                        return False

        #if it's BH, try NN
        #returns false if there is no solution after trying NN
        elif listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] == "B":
            if limitsrow(limits,listem2) and limitscol(limits,listem2):
                write_output(listem2)
                return listem2
            else:
                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                if limitsrow(limits,listem2) and limitscol(limits,listem2):
                    write_output(listem2)
                    return listem2
                elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                    return False

        #if NN, it does LR or UD and returns false
        elif listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] == "N":
            if limitsrow(limits,listem2) and limitscol(limits,listem2):
                write_output(listem2)
                return listem2
            else:
                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                return False

        #if it's LR or UD, try HB, BH or NN
        #returns false if there is no solution after trying NN
        elif listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] == "L" or listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] == "U":
            m = "H"
            if (right_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and left_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and up_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and under_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m)):
                m = "B"
                if (right_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and left_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and up_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and under_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m)):
                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "H"
                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "B"
                    if limitsrow(limits,listem2) and limitscol(limits,listem2):
                        write_output(listem2)
                        return listem2
                    elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                        m = "B"
                        if (right_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and left_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and up_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and under_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m)):
                            m = "H"
                            if (right_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and left_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and up_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and under_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m)):
                                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "B"
                                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "H"
                                if limitsrow(limits,listem2) and limitscol(limits,listem2):
                                    write_output(listem2)
                                    return listem2
                                elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                                    if limitsrow(limits,listem2) and limitscol(limits,listem2):
                                        write_output(listem2)
                                        return listem2
                                    elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                                        return False
                            else:
                                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                                if limitsrow(limits,listem2) and limitscol(limits,listem2):
                                    write_output(listem2)
                                    return listem2
                                elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                                    return False        
                            
                        else:
                            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                            if limitsrow(limits,listem2) and limitscol(limits,listem2):
                                write_output(listem2)
                                return listem2
                            elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                                return False 
                else:
                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                    if limitsrow(limits,listem2) and limitscol(limits,listem2):
                        write_output(listem2)
                        return listem2
                    elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                        return False 

            else:
                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                m = "B"
                if (right_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and left_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and up_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and under_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m)):
                    m = "H"
                    if (right_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and left_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and up_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and under_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m)):
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "B"
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "H"
                        if limitsrow(limits,listem2) and limitscol(limits,listem2):
                            write_output(listem2)
                            return listem2
                        elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                            if limitsrow(limits,listem2) and limitscol(limits,listem2):
                                write_output(listem2)
                                return listem2
                            elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                                return False
                    else:
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                        if limitsrow(limits,listem2) and limitscol(limits,listem2):
                            write_output(listem2)
                            return listem2
                        elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                            return False        
                    
                else:
                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                    if limitsrow(limits,listem2) and limitscol(limits,listem2):
                        write_output(listem2)
                        return listem2
                    elif not (limitsrow(limits,listem2) and limitscol(limits,listem2)):
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                        return False
    #for trials, except for the last tile 
    elif type(myindex) == int:
        #if it's HB, try BH, if not, try NN
        #returns false if there is no solution after trying NN 
        if listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] == "H":
            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]                   
            m = "B"
            if (right_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and left_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and up_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and under_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m)):
                m = "H"
                if (right_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and left_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and up_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and under_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m)):
                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "B"
                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "H"
                    if backtracking(listem2,listem3,indexes,myindex+1) == False:
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                        if backtracking(listem2,listem3,indexes,myindex+1) == False:
                            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                            return False
                else:
                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                    if backtracking(listem2,listem3,indexes,myindex+1) == False:
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                        return False
                        
            else:
                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                if backtracking(listem2,listem3,indexes,myindex+1) == False:
                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                    return False
                

        #if it's BH, try NN
        #returns false if there is no solution after trying NN
        elif listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] == "B":
            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
            if backtracking(listem2,listem3,indexes,myindex+1) == False:
                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                return False
            

        #if NN, it does LR or UD and returns false
        elif listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] == "N":
            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
            return False
            

        #if it's LR or UD, try HB, BH or NN
        #returns false if there is no solution after trying NN
        elif listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] == "L" or listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] == "U":
            m = "H"
            if (right_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and left_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and up_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and under_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m)):
                m = "B"
                if (right_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and left_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and up_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and under_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m)):
                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "H"
                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "B"
                    if backtracking(listem2,listem3,indexes,myindex+1) == False:
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]           
                        m = "B"
                        if (right_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and left_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and up_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and under_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m)):
                            m = "H"
                            if (right_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and left_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and up_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and under_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m)):
                                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "B"
                                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "H"
                                if backtracking(listem2,listem3,indexes,myindex+1) == False:
                                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                                    if backtracking(listem2,listem3,indexes,myindex+1) == False:
                                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                                        return False
                            else:
                                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                                if backtracking(listem2,listem3,indexes,myindex+1) == False:
                                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                                    return False        
                            
                        else:
                            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                            if backtracking(listem2,listem3,indexes,myindex+1) == False:
                                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                                return False
                    
                else:
                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]           
                    m = "B"
                    if (right_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and left_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and up_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and under_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m)):
                        m = "H"
                        if (right_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and left_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and up_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and under_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m)):
                            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "B"
                            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "H"
                            if backtracking(listem2,listem3,indexes,myindex+1) == False:
                                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                                if backtracking(listem2,listem3,indexes,myindex+1) == False:
                                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                                    return False
                        else:
                            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                            if backtracking(listem2,listem3,indexes,myindex+1) == False:
                                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                                return False        
                        
                    else:
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                        if backtracking(listem2,listem3,indexes,myindex+1) == False:
                            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                            return False 

            else:
                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]           
                m = "B"
                if (right_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and left_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and up_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m) and under_kontrol(indexes[myindex][0][0],indexes[myindex][0][1],listem2,m)):
                    m = "H"
                    if (right_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and left_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and up_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m) and under_kontrol(indexes[myindex][1][0],indexes[myindex][1][1],listem2,m)):
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "B"
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "H"
                        if backtracking(listem2,listem3,indexes,myindex+1) == False:
                            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                            if backtracking(listem2,listem3,indexes,myindex+1) == False:
                                listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                                listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                                return False
                    else:
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                        if backtracking(listem2,listem3,indexes,myindex+1) == False:
                            listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                            listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                            return False        
                    
                else:
                    listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = "N"
                    listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = "N"
                    if backtracking(listem2,listem3,indexes,myindex+1) == False:
                        listem2[indexes[myindex][0][0]][indexes[myindex][0][1]] = listem3[indexes[myindex][0][0]][indexes[myindex][0][1]]
                        listem2[indexes[myindex][1][0]][indexes[myindex][1][1]] = listem3[indexes[myindex][1][0]][indexes[myindex][1][1]]
                        return False
    #recursion part
    else:
        #starts with the last tile, if it can't find a solution, it looks at the previous tile
        myindex = len(indexes)-1
        while True:
            if backtracking(listem2,listem3,indexes,myindex) == False:
                myindex -= 1
                #prints "no solution" if it cannot find a solution after checking the first tile
                if myindex == -1:
                    no_solution()
                    break
            else:
                break


def main():
    #starts the first insertion
    myindex2 = 0
    listem2 = first_tiling(listem,indexes,myindex2)
    #starts the function
    myindex = "BBM103"
    backtracking(listem2,listem3,indexes,myindex)

if __name__ == "__main__":
    main()