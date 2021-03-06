import numpy as np
from problem5 import pagerank
import csv
import os

#-------------------------------------------------------------------------
'''
    Problem 6: use PageRank (implemented in Problem 5) to compute the ranked list of nodes in a real-world network.
    In this problem, we import a real-world network and use pagerank algorithm to rank the nodes in the network.
    File `network.csv` contains a network adjacency matrix.
    (1) import the network from the file
    (2) compute the pagerank scores for the network
    You could test the correctness of your code by typing `nosetests test6.py` in the terminal.
'''

#--------------------------
def import_A(filename ='network.csv'):
    '''
        import the addjacency matrix A from a CSV file
        Input:
                filename: the name of csv file, a string
        Output:
                A: the ajacency matrix, a numpy matrix of shape (n by n)
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    print()
    A=np.genfromtxt(os.path.dirname(os.path.abspath(__file__))+'/'+filename, delimiter=',',dtype=np.double)
    #########################################
    return np.asmatrix(A)


#--------------------------
def score2rank(x):
    '''
        compute a list of node IDs sorted by descending order of pagerank scores in x.
        Note the node IDs start from 0. So the IDs of the nodes are 0,1,2,3, ...
        Input:
                x: the numpy array of pagerank scores, shape (n by 1)
        Output:
                sorted_ids: a python list of node IDs (starting from 0) in descending order of their pagerank scores, a python list of integer values, such as [2,0,1,3].
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    A = x
    sorted_ids = [n for n in range(len(A))]
    for i in range(len(A)):
        for k in range( len(A) - 1, i, -1):
            if ( A[k] < A[k - 1] ):
                swap( A, k, k - 1 )
                swap1(sorted_ids, k, k-1)
    #########################################
    re = [n for n in range(len(A))]
    for i in range(len(A)):
        re[i] = sorted_ids[len(A)-i-1]
    return re

#--------------------------
def node_ranking(filename = 'network.csv', alpha = 0.95):
    '''
        Rank the nodes in the network imported from a CSV file.
        (1) import the adjacency matrix from `filename` file.
        (2) compute pagerank scores of all the nodes
        (3) return a list of node IDs sorted by descending order of pagerank scores

        Input:
                filename: the csv filename for the adjacency matrix, a string.
                alpha: a float scalar value, which is the probability of choosing option 1 (randomly follow a link on the node)

        Output:
                sorted_ids: the list of node IDs (starting from 0) in descending order of their pagerank scores, a python list of integer values, such as [2,0,1,3].

    '''

    A = import_A(filename)
    x = pagerank(A, alpha)
    sorted_ids = score2rank(x)
    return sorted_ids


#--------------------------
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
    tmp = A[i, 0]
    A[i, 0] = A[j, 0]
    A[j, 0] = tmp

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
