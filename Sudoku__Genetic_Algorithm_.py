
import random;
import copy;
import numpy
from random import randint
random_no = 1


sudoku_board = [[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],
                [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],
                [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]]

board_row_list = [[],[],[],[],[],[],[],[],[]]
board_col_list = [[],[],[],[],[],[],[],[],[]]
board_box_list = [[],[],[],[],[],[],[],[],[]]

def list_unique_box_check(_list):
    for box in _list:
        list_app = []
        for i in range(9):
            if(len(list_app) is 0 and box[i] is not -1):
                list_app.append(box[i]);
            else:
                for check_w in list_app:
                    if(box[i] == check_w and box[i] is not -1):
                        return False;
                    else:
                        if(box[i] is not -1):
                            list_app.append(box[i]);
                            break;
    return True;

def checkIfDuplicates_2(listt):
    ''' Check if given list contains any duplicates ''' 
    for i in range(0,8):
        for j in range(0,8):
            for k in range((j+1),8):
                if(listt[i][j]!=-1 and listt[i][k]!=-1 and listt[i][j]==listt[i][k]):
                    print('duplicate founddd ', listt[i]);
                    return True;
            
    return False

def row_list_changer(row_list, board):
    for box in row_list:
        box.clear();
    box = 0;
    row_box = 0;
    for r in range(9):
        if(r%3 is 0 and r is not 0):
            box += 3
            row_box = 0;
            
        row_list[r].append(board[box][row_box][0]);
        row_list[r].append(board[box][row_box][1]); 
        row_list[r].append(board[box][row_box][2]);
        
        row_list[r].append(board[box+1][row_box][0]); 
        row_list[r].append(board[box+1][row_box][1]);
        row_list[r].append(board[box+1][row_box][2]);
        
        row_list[r].append(board[box+2][row_box][0]);
        row_list[r].append(board[box+2][row_box][1]);
        row_list[r].append(board[box+2][row_box][2]);
        
        row_box += 1;

def col_list_changer(col_list, board):
    for box in col_list:
        box.clear();

    box = 0;
    col_box = 0;
    for c in range(9):
        if(c%3 is 0 and c is not 0):
            box += 1
            col_box = 0
        col_list[c].append(board[box][0][col_box]);
        col_list[c].append(board[box][1][col_box]);
        col_list[c].append(board[box][2][col_box]); 
        
        col_list[c].append(board[box+3][0][col_box]);
        col_list[c].append(board[box+3][1][col_box]);
        col_list[c].append(board[box+3][2][col_box]);
        
        col_list[c].append(board[box+6][0][col_box]);
        col_list[c].append(board[box+6][1][col_box]);
        col_list[c].append(board[box+6][2][col_box]);
        col_box += 1;

def box_list_changer(box_list, board):
    for box in box_list:
        box.clear();
    i = 0;
    for i in range(9):
        # for each row in the box, we have to include it inside for the indexes
        for j in range(3):
            box_list[i].append(board[i][j][0]); 
            box_list[i].append(board[i][j][1]);
            box_list[i].append(board[i][j][2]);

def list_modifier(board):
    row_list_changer(board_row_list, board);
    col_list_changer(board_col_list, board);
    box_list_changer(board_box_list, board);

def print_board(sudoku_board):
    list_modifier(sudoku_board)
    print("\n    | ", end = " ")
    for i in range(9):
        print(i, end=" |  ")
    print('\n')
    for i in range(9):
        
        if(i%3==0):
            print("    -------------------------------------------\n")
        print(i, end = "  ")

        for j in range(9):
            if(j%3==0):
                print(end = " |  ")
            if(board_row_list[i][j] is not -1):
                if((j+1)%3==0):
                    print(board_row_list[i][j], end = " ")
                else:
                    print(board_row_list[i][j], end = " : ")
                if(j==8):
                    print(end = " |")

            else:
                if((j+1)%3==0):
                    print(" ", end = " ")
                else:
                    print(" ", end = " : ")
                if(j==8):
                    print(end = " |")
                    
        print('\n')

    
def is_board_unique():

    if(checkIfDuplicates_2(board_box_list) is False and
       checkIfDuplicates_2(board_col_list) is False and
       checkIfDuplicates_2(board_row_list) is False):
        return True;
    return False; #returns True if Unique

def get_rand():
    global random_no
    if(random_no > 8):
        random_no = 0;
    random_no += 1;
    return random_no;

def all_board_filled():
    for i in range(9):
        for j in range(9):
            if(board_row_list[i][j] is -1 or board_col_list[i][j] is -1 or board_box_list[i][j] is -1):
                return False
    return True

def random_board_generator():
    i = 0;
    for i in range(9):
        # for each row in the box, we have to include it inside for the indexes
        # j can range from 0 - 2 /3
        # k can range from 0 - 2 /3
        # random number can range from 0 - 8 /9
        for l in range(3):
            j = random.randint(0, 2)
            k = random.randint(0, 2)
            sudoku_board[i][j][k] = get_rand() #change a value
            list_modifier(sudoku_board);

            while(is_board_unique() is False):
                # run a loop to change the value till it is unique
                sudoku_board[i][j][k] = get_rand() # keep changing
                list_modifier(sudoku_board);

def input_set(x, y, val):
    b_row = 0;
    b_col = 0;

    if(x is 0 or x is 3 or x is 6):
        b_row = 0;
    else:
        b_row = x%3;

    if(y is 0 or y is 3 or y is 6):
        b_col = 0;
    else:
        b_col = y%3;

    #get the box now
    b_i = 0;
    if(x is 0 or x is 1 or x is 2):
        b_i = 0;
    elif(x is 3 or x is 4 or x is 5):
        b_i = 3;
    else:
        b_i = 6;

    b_j = 0;
    if(y is 0 or y is 1 or y is 2):
        b_j = 0;
    elif(y is 3 or y is 4 or y is 5):
        b_j = 1;
    else:
        b_j = 2;
    
    box_index = b_i + b_j;

    sudoku_board[box_index][b_row][b_col] = val;

def game_play():
    while(all_board_filled() is False):
        x = int(input("Enter values for : x -> "))
        y = int(input("Enter values for : y -> "))
        value = int(input("Enter value between 0 to 9 : ->"))
        input_set(x, y, value);
        list_modifier();
        print_board(sudoku_board);
        print('\n', board_row_list);
        print('\n', board_col_list);
        print('\n', board_box_list);
        if(is_board_unique() is False):
            print("Invalid Move!")
            input("Terminate")
            break;
    if(is_board_unique() is True):
        print("You WIN!")


#CLASSES

class Population(object):
    
    def __init__(self):
        self.candidates = []    #will maintain an array of possible solutions
        return

    def populateRand(self, no_of_candidates):
        
        no_of_candidates= no_of_candidates;
        
        for l in range(0,no_of_candidates):
            c = Candidate()
        
            i = 0
           
            c.sudoku_board=list(sudoku_board);
            for i in range(9):
                for j in range(0,3):
                    for k in range(0,3):
                        if(sudoku_board[i][j][k] is not -1):
                            c.board[i][j][k]=sudoku_board[i][j][k]
                        else:       
                            c.board[i][j][k] = get_rand() #change a value
                            c.list_modifier()
                    
                        """
                        while(c.is_board_unique() is False):
                            # run a loop to change the value till it is unique
                            c.sudoku_board[i][j][k] = get_rand() # keep changing
                            c.list_modifier()
                        """
            #calculate fitness function
            c.list_modifier()
            c.update_fitness();
            print_board(c.board);
            print('\n')
            print('FITNESS VALUE CANDIDATE ',l,' =', c.fitness_value)
            self.candidates.append(c);
            
                
    #make fitness function
    def update_fitness(candidate):
        candidate.update_fitness()
    
    #make sort function
    def sort_fitness(self):    
        self.candidates.sort(key=lambda x: x.fitness_value)
        
class Tournament(object):
    """ The crossover function requires two parents to be selected from the population pool. The Tournament class is used to do this.
    
    Two individuals are selected from the population pool and a random number in [0, 1] is chosen. If this number is less than the 'selection rate' (e.g. 0.85), then the fitter individual is selected; otherwise, the weaker one is selected.
    """

    def __init__(self):
        return
        
    def compete(self, candidates):
        """ take two randome candidiaates and make them copmete """
        c1 = candidates[random.randint(0, len(candidates)-1)]
        c2 = candidates[random.randint(0, len(candidates)-1)]
        f1 = c1.fitness_value
        f2 = c2.fitness_value

        # Find the fittest and the weakest.
        if(f1 > f2):
            fittest = c1
            weakest = c2
        else:
            fittest = c2
            weakest = c1

        selection_rate = 0.85
        r = random.uniform(0, 1.1)
        while(r > 1):  # Outside [0, 1] boundary. Choose another.
            r = random.uniform(0, 1.1)
        if(r < selection_rate):
            return fittest
        else:
            return weakest
    


class Candidate(object):
    def __init__(self):
        self.board = [[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],
                        [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],
                        [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]]

        self.board_row_list = [[],[],[],[],[],[],[],[],[]]
        self.board_col_list = [[],[],[],[],[],[],[],[],[]]
        self.board_box_list = [[],[],[],[],[],[],[],[],[]]
        
        self.fitness_value = None
        
        return

    def list_modifier(self):
        row_list_changer(self.board_row_list, self.board);
        col_list_changer(self.board_col_list, self.board);
        box_list_changer(self.board_box_list, self.board);
        
    def occurences(self, row_duplicate_sum, list_count, listt ):
        row_duplicate_sum=0
        count = [0,0,0,0,0,0,0,0,0,0]
        for i in range(0, 9):  # For each row...
            for j in range(0, 9):  # For each element in a row
                list_count[listt[i][j]] = list_count[listt[i][j]]+1   

                #list_sum += (1.0/len(set(list_count)))/9
            for j in range(0,10):
                if(list_count[j]>1):
                    row_duplicate_sum= row_duplicate_sum+1
            #store the suplicate number in the row index of count
            count[i]=row_duplicate_sum
            row_duplicate_sum=0
                    
            list_count = [0,0,0,0,0,0,0,0,0,0]
        list_count=count
        return count


    def update_fitness(self):
        row_count = [0,0,0,0,0,0,0,0,0,0] #this will keep the count of duplicates
        col_count = [0,0,0,0,0,0,0,0,0,0]
        box_count = [0,0,0,0,0,0,0,0,0,0]
        row_sum = 0
        col_sum = 0
        box_sum = 0

        #for each row
        row_count = self.occurences(row_sum, row_count, self.board_row_list);
        for i in range(0,10):
            if(row_count[i]>1):
                row_sum= row_sum+1
        
        #for each column
        col_count=self.occurences(col_sum, col_count, self.board_col_list);
        for i in range(0,9):
            if(col_count[i]>1):
                col_sum = col_sum+1
        
        #for each box
        box_count=self.occurences(box_sum, box_count, self.board_box_list);
        for i in range(0,9):
            if(box_count[i]>1):
                box_sum= box_sum+1
        
        self.fitness_value= row_sum + col_sum + box_sum
        

    def all_board_filled(self):
        for i in range(0,9):
            for j in range(0,9):
                if(self.board_row_list[i][j] is -1 or self.board_col_list[i][j] is -1 or self.board_box_list[i][j] is -1):
                    return False
        return True
    
    
    def is_board_unique(self):

        if(checkIfDuplicates_2(self.board_box_list) is False and
           checkIfDuplicates_2(self.board_col_list) is False and
           checkIfDuplicates_2(self.board_row_list) is False):
            return True
        return False; 
     

def replace_box_parent(p1, p2, c):
    """ Takes parent candidates p1 and p2 create a child by randomly giving 2 of it's
        boxes to the child, keeping the original positioned game cells.
    """
    #first randomly generate a solution then replace some of it's box with parent
    i = 0       
    c.sudoku_board=list(sudoku_board)
    for i in range(9): #box number
        for j in range(0,3):    #
            for k in range(0,3):
                    if(sudoku_board[i][j][k] is not -1):
                        c.board[i][j][k]=sudoku_board[i][j][k]
                    else:       
                        c.board[i][j][k] = get_rand()
    
    
    #calculate fitness function
    c.list_modifier()
    c.update_fitness()
    
    for i in range(0,2):
        #randomly selecting the parents box
        choose= randint(0, 8)
        c.board[choose]=p1.board[choose]  #replaces the parent box with random game board box
    
    for i in range(0,2):
        #randomly selecting the parents box
        choose= randint(0, 8)
        c.board[choose]=p2.board[choose]

    
    #keeping the orignal sudoku cells in place
    for i in range(9):
        for j in range(0,3):
            for k in range(0,3):
                #not empty cell in orginal was on not -1 position
                if(sudoku_board[i][j][k] is not -1):
                    c.board[i][j][k]=sudoku_board[i][j][k]
    
    c.list_modifier()
    c.update_fitness()

#crossover function
def cross_over( p):
    """Randomly choose various rows from two parents,
        which creates one child
    """
    t=Tournament()
    p1=t.compete(p.candidates)
    p2=t.compete(p.candidates)
    
    while(p1 is p2):
        p2=t.compete(p.candidates)
    child1= Candidate()
    child2= Candidate()  
    
    #first randomly generate a solution then replace some of it's box with parent
    replace_box_parent(p1, p2, child1)
    replace_box_parent(p1, p2, child2)

    
    #removing parents
    p.candidates.remove(p1)
    p.candidates.remove(p2)
    
    p.candidates.append(child1)
    p.candidates.append(child2)
    


def mutation(candidate):
    """a mutation to randomize the entire row makes the performance better.
    """
    box= get_rand()
    
    for i in range(4):
        box=randint(0,8)
        row= randint(0,2)  #get random row position
        col= 0
        for col in range(0,3):
            #if it is not the orginal position    
            if(sudoku_board[box][row][col] is -1):
                candidate.board[box][row][col]=randint(0,9)
    
    candidate.list_modifier()
    candidate.update_fitness()
    
    
    
#randomly choose arrayCrossover: Randomly choose various rows from two parents,
       # which creates one child. (I've also implemented a crossover 
        #that randomly chooses 3 rows at a time from
        #the two parents - in an effort to preserve good mini-grids).
        
        #Mutation: also tried a mutation where it chose a random box and then chose
        #two random (non-given) positions in the box and swapped them, but
        #this made the performance much worse as well. (Unlike the swapping
        #of the two random locations, I don't understand why this mutation
        #would make the performance so much worse, yet a mutation to 
        #randomize the entire row makes the performance better.
        #"""

def print_best_solutions(p, number):
    for i in range(0,number):
        print_board(p.candidates[i].board)
        print("\nFITNESS VALUE= ")
        print(p.candidates[i].fitness_value)
        print('\n')

#-------------------------------------------------------
# MAIN
#this will print a generate a board with random game values
random_board_generator();
print_board(sudoku_board);


p = Population();   #creates a population object
p.populateRand(40)  #generate population rndomly of 20 candidates
p.sort_fitness()    #calculates the fitness of the 

#print first 5 best solutions
print("5 BEST SOLUTIONS AFTER GENERATING RANDOM POPULTATION \n")
print_best_solutions(p, 5)


#performs cross over first 5 population
for i in range(0,5):
    cross_over(p)

p.sort_fitness()
print("5 BEST SOLUTIONS AFTER COSS-OVER \n")
print_best_solutions(p, 5)

#performs mutation over the first 5
i=0
for i in range(0,5):
    mutation(p.candidates[i])

p.sort_fitness()
print("\n5 BEST SOLUTIONS AFTER COSS-OVER \n")
print_best_solutions(p, 5)


game_play();

