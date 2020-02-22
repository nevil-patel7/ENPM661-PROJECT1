#importing the depandancies
import copy
import numpy as np

#Hard coding the Goal Node.
Goal_Node = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]

# StartNode =  [[1, 0, 3],
#               [4, 2, 5],
#               [7, 8, 6]]

#Defining the Data Structures
StartNode=[]
Node_stat = []
Parent_Node_Index_i = []
Back_Track = []
Nodes_Info = []
Nodes = []
Generate_Path = []
Node_Index = []
Merged_Node_Stat = []
Merged_Generate_Path = []
Merged_Nodes_Info = []
x=0

#Takes User input of Puzzle Matrix
def Start_Position():
    TempNode = []
    InitialNode = []
    TempNode = list(map(int, input("Enter the row-wise Initial Configuration separated by spaces\n").strip().split()))[:9]
    if len(TempNode) is not 9:
        GetInitialNode()
    InitialNode.append(TempNode[:3])
    InitialNode.append(TempNode[3:6])
    InitialNode.append(TempNode[6:9])
    return InitialNode

#Removes the nested list in a master list
def reemovNestings(Nessted,A):
    for i in Nessted:
        if type(i) == list:
            reemovNestings(i,A)
        else:
            A.append(i)

#Finds out the position of 0 in the Puzzle
def BlankTileLocation(Node):
    for i in range(0,3):
        for j in range(0,3):
            if Node[i][j] == 0:
                x = i
                y = j
                return x,y

#Checks whether the new Node explored is already present in the main Node_Stat file.
def Same_Puzzle(Node):
    if not(Node in Node_stat):
        return False
    else:
        return True

#Adds the Child and Parent Node that is Newly explored
def AddNode(Node):
    Check_Same = Same_Puzzle(Node)
    if Check_Same == False:
        Node_stat.append(Node)
        Parent_Node_Index_i.append(Node_stat.index(CurrentNode))
        return Check_Same
    else:
        return Check_Same

#Moves the 0 Position in Left direction if possible
def ActionMoveLeft(CurrentNode):
    Node = copy.deepcopy(CurrentNode)
    [x,y] = BlankTileLocation(Node)
    #if function to check Boundary:
    if y != 0:
        temp = Node[x][y-1]
        Node[x][y-1] = 0
        Node[x][y] = temp
        Stat = BlankTileLocation(Node)
        return Stat,Node
    else:
        return None,None

#Moves the 0 Position in Right direction if possible
def ActionMoveRight(CurrentNode):
    Node = copy.deepcopy(CurrentNode)
    [x,y] = BlankTileLocation(Node)
    #if function to check Boundary:
    if y != 2:
        temp = Node[x][y+1]
        Node[x][y+1] = 0
        Node[x][y] = temp
        Stat = BlankTileLocation(Node)
        return Stat,Node
    else:
        return None,None

#Moves the 0 Position in Up direction if possible
def ActionMoveUp(CurrentNode):
    Node = copy.deepcopy(CurrentNode)
    [x,y] = BlankTileLocation(Node)
    #if function to check Boundary:
    if x != 0:
        temp = Node[x-1][y]
        Node[x-1][y] = 0
        Node[x][y] = temp
        Stat = BlankTileLocation(Node)
        return Stat,Node
    else:
        return None,None

#Moves the 0 Position in Down direction if possible
def ActionMoveDown(CurrentNode):
    Node = copy.deepcopy(CurrentNode)
    [x,y] = BlankTileLocation(Node)
    #if function to check Boundary:
    if x != 2:
        temp = Node[x+1][y]
        Node[x+1][y] = 0
        Node[x][y] = temp
        Stat = BlankTileLocation(Node)
        return Stat,Node
    else:
        return None,None

#Backtracks the Path from Goal to Start within that Branch
def Track_Path(Node):
    Back_Track.append(Node_stat.index(Node))
    while(Back_Track[0] != 0):
        Back_Track.insert(0,Parent_Node_Index_i[Node_stat.index(Node)])
        Node = Node_stat[Back_Track[0]]

#Gets the path Nodes from Track_Path function
def Get_Path(Reverse_Node):
    for i in range(len(Reverse_Node)):
        Generate_Path.append(Node_stat[Reverse_Node[i]])

#Function for Printing the Puzzle from Start to Goal Position
def print_matrix(state):
    counter = 0
    for row in range(0, len(state), 3):
        if counter == 0 :
            print("-------------")
        for element in range(counter, len(state), 3):
            if element <= counter:
                print("|", end=" ")
            print(int(state[element]), "|", end=" ")
        counter = counter +1
        print("\n-------------")

#Doing the Initial Configuration
StartNode = Start_Position()
CurrentNode = copy.deepcopy(StartNode)
Node_stat.append(StartNode)
Parent_Node_Index_i.append(0)
Node_Index.append(0)

#Solving the puzzle by moving zero in all Four directions and by updating the List with Node infos
while (Goal_Node != CurrentNode):
    if (ActionMoveLeft(CurrentNode)[1]) != None:
        [Status,NewNode] = ActionMoveLeft(CurrentNode)
        Same_Status = AddNode(NewNode)
        if Same_Status == False:
            x=x+1
            Node_Index.append(x)


    if (ActionMoveRight(CurrentNode)[1]) != None:
        [Status,NewNode] = ActionMoveRight(CurrentNode)
        Same_Status = AddNode(NewNode)
        if Same_Status == False:
            x=x+1
            Node_Index.append(x)

    if (ActionMoveUp(CurrentNode)[1]) != None:
        [Status,NewNode] = ActionMoveUp(CurrentNode)
        Same_Status = AddNode(NewNode)
        if Same_Status == False:
            x=x+1
            Node_Index.append(x)

    if (ActionMoveDown(CurrentNode)[1]) != None:
        [Status,NewNode] = ActionMoveDown(CurrentNode)
        Same_Status = AddNode(NewNode)
        if Same_Status == False:
            x=x+1
            Node_Index.append(x)

    New_Node_stat = Node_stat.index(CurrentNode)+1
    CurrentNode = Node_stat[New_Node_stat]
    Nodes_Info.append([Node_stat.index(CurrentNode), Parent_Node_Index_i[Node_stat.index(CurrentNode)],0])
    print(Node_stat.index(CurrentNode),"CurrentNode",CurrentNode)

#Backtracking the Genrated Path
Track_Path(CurrentNode)
Get_Path(Back_Track)
print("NodeIndex--> ",Node_Index)
print("ParentNodeIndex-->",Parent_Node_Index_i)
print("BranchToGoal-->",Back_Track)
reemovNestings(Node_stat,Merged_Node_Stat)
reemovNestings(Generate_Path,Merged_Generate_Path)
reemovNestings(Nodes_Info,Merged_Nodes_Info)

#Creating the Text Files of explored Nodes and its path from Goal to start

with open('Nodes.txt', 'w') as fh:
        for x in range(0,len(Merged_Node_Stat),9):
            for i in range(0,9):
                fh.write(str(Merged_Node_Stat[x]) + ' ')
                x = x+1
            fh.write("\n")
            
with open('NodesInfo.txt', 'w') as fh:
        for x in range(0,len(Merged_Nodes_Info),3):
            fh.write(str(Merged_Nodes_Info[x]) + ' ')
            fh.write(str(Merged_Nodes_Info[x+1]) + ' ')
            fh.write(str(Merged_Nodes_Info[x+2]) + ' ')
            fh.write("\n")

with open('nodePath.txt', 'w') as fh:
        for x in range(0,len(Merged_Generate_Path),9):
            for i in range(0,9):
                fh.write(str(Merged_Generate_Path[x]) + ' ')
                x = x+1
            fh.write("\n")

#Printiing Path from Start to Goal Position
print("PRINTING THE PATH")
fname = 'nodePath.txt'
data = np.loadtxt(fname)
if len(data[1]) != 9:
    print("Format of the text file is incorrect, retry ")
else:
    for i in range(0, len(data)):
        if i == 0:
            print("Start Node")
        elif i == len(data)-1:
            print("Achieved Goal Node")
        else:
            print("Step ",i)
        print_matrix(data[i])
        print()
        print()
