from problem1 import elo_rating
import numpy as np
import os
#-------------------------------------------------------------------------
'''
    Problem 2:
    In this problem, you will use the Elo rating algorithm in problem 1 to rank the NCAA teams.
    You could test the correctness of your code by typing `nosetests test2.py` in the terminal.
'''

#--------------------------
def import_W(filename ='ncaa_results.csv'):
    '''
        import the matrix W of game results from a CSV file
        Input:
                filename: the name of csv file, a string
        Output:
                W: the game result matrix, a numpy integer matrix of shape (n by 2)
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    W=np.genfromtxt(os.path.dirname(os.path.abspath(__file__))+'/'+filename, delimiter=',',dtype=np.integer)

    #########################################
    return W

#--------------------------
def import_team_names(filename ='ncaa_teams.txt'):
    '''
        import a list of team names from a txt file. Each line of text in the file is a team name.
        Input:
                filename: the name of txt file, a string
        Output:
                team_names: the list of team names, a python list of string values, such as ['team a', 'team b','team c'].
    '''
    #########################################
    ## INSERT YOUR CODE HERE

    tfile = open(os.path.dirname(os.path.abspath(__file__))+'/'+filename, 'r')
    team_names = [line[:-1] for line in tfile.readlines()]
    #########################################
    return team_names

#--------------------------
def team_rating(resultfile = 'ncaa_results.csv',
                teamfile='ncaa_teams.txt',
                K=16.):
    '''
        Rate the teams in the game results imported from a CSV file.
        (1) import the W matrix from `resultfile` file.
        (2) compute Elo ratings of all the teams
        (3) return a list of team names sorted by descending order of Elo ratings

        Input:
                resultfile: the csv filename for the game result matrix, a string.
                teamfile: the text filename for the team names, a string.
                K: a float scalar value, which is the k-factor of Elo rating system

        Output:
                top_teams: the list of team names in descending order of their Elo ratings, a python list of string values, such as ['team a', 'team b','team c'].
                top_ratings: the list of elo ratings in descending order, a python list of float values, such as ['600.', '500.','300.'].

    '''
    #########################################
    ## INSERT YOUR CODE HERE
    W = import_W(resultfile)
    team_names = import_team_names(teamfile)
    A = elo_rating(W, len(team_names), K)
    sorted_ids = team_names
    for i in range(len(A)):
        for k in range( len(A) - 1, i, -1):
            if ( A[k] > A[k - 1] ):
                swap( A, k, k - 1 )
                swap1(sorted_ids, k, k-1)
    #########################################
    return sorted_ids, A

def swap( A, i, j ):
    '''
        Swap the i-th element and j-th element in list A.
        Inputs:
            A:  a list, such as  [2,6,1,4]
            i:  an index integer for list A, such as  3
            j:  an index integer for list A, such as  0
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def swap1( A, i, j ):
    '''
        Swap the i-th element and j-th element in list A.
        Inputs:
            A:  a list, such as  [2,6,1,4]
            i:  an index integer for list A, such as  3
            j:  an index integer for list A, such as  0
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
