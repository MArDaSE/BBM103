import sys


#Gets input file from txt file.
def get_input_file():
    with open(sys.argv[1], "r") as input_file:
        lines = input_file.readlines()
    return lines


#Transfers the rows from input to the list.
def get_row(lines):
    row = list()

    for i in lines:
        i = i.strip()
        numbers = list()
        for j in i.split():
            numbers.append(int(j))
        row.append(numbers)
    return row


#Transfers the cols to the list.
def get_col(row):
    col = list()

    for i in range(9):
        col_1 = list()
        for j in range(9):
            col_1.append(row[j][i])
        col.append(col_1)
    return col


#Finds the position of the spaces in sudoku
def find_zeros(row):
    zero_nums = list()
    for i in range(9):
        for j in range(9):
            if row[i][j] == 0:
                zero_nums.append([i,j])
    return zero_nums


#Transfers the 3x3 sudoku regions to the list
def get_zones(row):
    zones = list()

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            zone = list()
            for m in range(i, i+3):
                for n in range(j, j+3):
                    zone.append(row[m][n])
            zones.append(zone)
    return zones


#Determines the region of the space found.
def control_zone(m):
    if (m[0] in [0,1,2]):
        if (m[1] in [0,1,2]):
            zone_num = 0
        elif (m[1] in [3,4,5]):
            zone_num = 1
        else:
            zone_num = 2
    elif (m[0] in [3,4,5]):
        if (m[1] in [0,1,2]):
            zone_num = 3
        elif (m[1] in [3,4,5]):
            zone_num = 4
        else:
            zone_num = 5
    else:
        if (m[1] in [0,1,2]):
            zone_num = 6
        elif (m[1] in [3,4,5]):
            zone_num = 7
        else:
            zone_num = 8
    return zone_num


#Solves the sudoku step by step.
def sudoku_solver(row,col,zero_nums,zones):
    stepnum = 0
    while True:    #If the gap is filled, it causes the function to return to the beginning to check the possible possibilities that may have occurred in the previous gaps.
        for m in zero_nums:    #In order to find the only possible gap, it tries the numbers that can fit into the gaps from the beginning.
            numbers_found = list()
            for i in range(1,10):
                if not (i in row[m[0]]):
                    if not (i in col[m[1]]):
                        zone_num = control_zone(m)
                        if not (i in zones[zone_num] ):
                            numbers_found.append(i)    #If it finds a gap with possibilities, it puts that possibilities on the list.
            if len(numbers_found) == 1:    #If it finds a space with a single possibility, it places it and updates the sudoku board.
                stepnum += 1

                zero_nums.remove([m[0],m[1]])    #Removes the filled space from the list of spaces
                row[m[0]][m[1]] = numbers_found[0]    #Puts the number in the row.
                col[m[1]][m[0]] = numbers_found[0]    #Puts the number in the col.
                
                zones = get_zones(row)    #Updates the zones.

                a = str(m[0]+1) 
                b = str(m[1]+1)
                c = str(numbers_found[0])
                
                write_output(stepnum,a,b,c,row)
                    
                break
        if len(zero_nums) == 0:
            with open(sys.argv[2],"a+") as fileo:
                    fileo.write("-"*18)
                    fileo.write("\n")
            break
    return None


#Writes the solved sudoku steps to the txt file.
def write_output(stepnum,a,b,c,row):
    with open(sys.argv[2],"a+") as fileo:
        fileo.write("-"*18 + "\n")
        fileo.write("Step" +" "+ str(stepnum)+" "+ "-" +" "+c +" "+ "@" +" "+ "R"+a + "C" + b + "\n")
        fileo.write("-"*18 + "\n")
        for element_2 in row:    #Writes the updated board to txt file.
            counter = 0
            for i in element_2:
                fileo.write(str(i))
                counter += 1
                if not(counter == 9):
                    fileo.write(" ")
            fileo.write("\n")
    return None


def main():
    lines = get_input_file()

    row = get_row(lines)

    col = get_col(row)

    zero_nums = find_zeros(row)

    zones = get_zones(row)

    sudoku_solver(row,col,zero_nums,zones)


if __name__ == "__main__":
    main()
