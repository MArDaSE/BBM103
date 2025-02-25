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
def get_col(rows):
    if len(rows) != 0:
        cols = list()
        
        for i in range(len(rows[0])):
            col_1 = list()
            for row in rows:
                col_1.append(row[i])
            cols.append(col_1)
        return cols


#Checks whether the entered row number is correct.
def isrowtrue(row,rows):
    if len(rows) != 0:
        if row > len(rows):
            return False
        else:
            return True


#Checks whether the entered column number is correct.
def iscoltrue(col,rows):
    if len(rows) != 0:
        if col > len(rows[0]):
            return False
        else:
            return True


#Gets row and column numbers from the user.
def enterinput(input_1):
    input_2 = input_1.split() 

    row = int(input_2[0]) 
    col = int(input_2[1])
    return [row,col]
    

#To decide the end of the game, it checks whether there are any neighboring cells.
def any_neighbors(rows,cols):
    if len(rows) != 0:
        for k in range(len(rows)):
            for j in range(len(rows[k])):
                neigh = list()
                if (rows[k][j] != " "):
                    neigh.append([k,j])
                    number = rows[k][j]
                    for i in neigh:
                        #Right
                        if i[1] != len(rows[0])-1:
                            if number == rows[i[0]][i[1]+1]:
                                if not ([i[0],i[1]+1] in neigh):
                                    neigh.append([i[0],i[1]+1])
                        #Left
                        if i[1] != 0:
                            if number == rows[i[0]][i[1]-1]:
                                if not ([i[0],i[1]-1] in neigh):
                                    neigh.append([i[0],i[1]-1])
                        #Under
                        if i[0] < len(cols[0])-1:
                            if number == rows[i[0]+1][i[1]]:
                                if not ([i[0]+1,i[1]] in neigh):
                                    neigh.append([i[0]+1,i[1]])
                        #Up
                        if i[0] != 0:
                            if number == rows[i[0]-1][i[1]]:
                                if not ([i[0]-1,i[1]] in neigh):
                                    neigh.append([i[0]-1,i[1]])
                if len(neigh) > 1:
                    return True
                if len(neigh) > 1:
                    break
                
            if len(neigh) > 1:
                    return True
            if len(neigh) > 1:
                break
        if len(neigh) <= 1:
            return False


#Checks the neighbors of the selected cell.
def get_neighbour(number,row,col,rows,cols):
    if len(rows) != 0:
        neighbours = list()
        neighbours.append([row-1,col-1])

        if number != " ":
            for i in neighbours:
                #Right neighbour.
                if i[1] != len(rows[0])-1:
                    if number == rows[i[0]][i[1]+1]:
                        if not ([i[0],i[1]+1] in neighbours):
                            neighbours.append([i[0],i[1]+1])

                #Left neighbour.
                if i[1] != 0:
                    if number == rows[i[0]][i[1]-1]:
                        if not ([i[0],i[1]-1] in neighbours):
                            neighbours.append([i[0],i[1]-1])

                #Under neighbour.
                if i[0] != len(cols[0])-1:
                    if number == rows[i[0]+1][i[1]]:
                        if not ([i[0]+1,i[1]] in neighbours):
                            neighbours.append([i[0]+1,i[1]])

                #Up neighbour.
                if i[0] != 0:
                    if number == rows[i[0]-1][i[1]]:
                        if not ([i[0]-1,i[1]] in neighbours):
                            neighbours.append([i[0]-1,i[1]])
        return neighbours


#It replaces the empty cell with the one above it.
def up_to_down(cols,rows):
    if len(rows) != 0:
        counter = 0
        while True:
            counter += 1
            for i in range(len(cols[0])):
                for j in range(len(rows[0])):
                    if i != 0:
                        if rows[i][j] == " ":
                            rows[i][j] = rows[i-1][j]
                            rows[i-1][j] = " "
            if counter == (len(rows) * len(cols)) or len(rows) == 0:
                break


#If a column is completely empty, it shifts the column to its right to the left.
def right_to_left(rows):
    if len(rows) != 0:
        counter = 0
        a = 0
        while True:
            counter += 1
            for i in range(len(rows[-1])+a):
                if rows[-1][i] == " ":
                    a -= 1
                    for j in range(len(rows)):
                        del rows[j][i]
                    break
            if counter >= len(rows[-1]) or len(rows) == 0:
                break
       

#If the first row is completely empty, it deletes the first row.
def remove_first_line(rows):
    if len(rows) != 0:
        counter = 0
        while True:
            counter += 1
            same_thing = all(x == " " for x in rows[0])        
            if same_thing:
                del rows[0]
            if counter >= len(rows) or len(rows) == 0:
                break


#When the game ends, the screen shows the final status score and the game is over.
def game_over(rows,score):
    print()
    for line in rows:
        count = ""
        for cell in line:
            count += str(cell) + " "
        print(count)
    print("\nYour score is: "+ str(score))
    print("\nGame over")


#It allows you to play the game correctly.
def playgame(rows,cols):
    score = 0
    for line in rows:
        count = ""
        for cell in line:
            count += str(cell) + " "
        print(count)
    print("\nYour score is: "+ str(score)+"\n")
    while True: 
        input_1 = input("Please enter a row and a column number: ")
        
        row = enterinput(input_1)[0]
        col = enterinput(input_1)[1]


        if isrowtrue(row,rows) and iscoltrue(col,rows):
            number = rows[row-1][col-1]

            neighbours = get_neighbour(number,row,col,rows,cols)

            if len(neighbours) != 1 : 
                score += number * len(neighbours)
                for j in neighbours:
                    rows[j[0]][j[1]] = " "          

                #Deletes the first row.
                remove_first_line(rows)

                cols = get_col(rows)

                #Scrolls from top to bottom.
                up_to_down(cols,rows)

                #Scrolls from right to left.
                right_to_left(rows)

                #Deletes the first row.
                remove_first_line(rows)

                #Game over
                cols = get_col(rows)
                if any_neighbors(rows,cols) == False or len(rows) == 0:
                    game_over(rows,score)
                    break
                else:
                    print()
                    for line in rows:
                        count = ""
                        for cell in line:
                            count += str(cell) + " "
                        print(count)
                    print("\nYour score is: "+ str(score)+"\n")
            
            else :
                print("\nNo movement happened try again\n")
                for line in rows:
                    count = ""
                    for cell in line:
                        count += str(cell) + " "
                    print(count)
                print("\nYour score is: "+ str(score)+"\n")

        else:
            print("\nPlease enter a correct size!\n")
        


def main():
    lines = get_input_file()
    rows = get_row(lines)
    cols = get_col(rows)
    any_neighbors(rows,cols)
    playgame(rows,cols)
    
    

if __name__ == "__main__":
    main()