# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 20:36:25 2022

@author: sayan
"""

import numpy as np

def problem_1a (A, B):
    answer = A+B
    return answer

def problem_1b (A,B,C):
    answer = np.dot(A,B) - C
    return answer

def problem_1c (A,B,C):
    answer = A*B + C.T
    return answer

def problem_1d (x,y):
    answer = np.inner(x,y)
    return answer

def problem_1e (A, x):
    answer = np.linalg.solve(A,x)
    return answer

def problem_1f (A, x):
    answer = (np.linalg.solve(A.T, x.T)).T
    return answer

def problem_1g (A, i):
    answer = np.sum(A[i, ::2])
    return answer

def problem_1h (A, c, d):
    B = A[A>=c and A<=d]
    answer = np.mean(B)
    return ...

def problem_1i (A, k):
    eigen_value, eigen_vector = np.linalg.eig(A)
    descending_i = np.argsort(eigen_value)[::-1]
    answer = eigen_vector[:,descending_i[:k]]
    return answer

def problem_1j (x, k, m, s):
    answer = np.random.multivariatenormal(x+m, np.eye(x.shape[0]) * s, k).T
    return answer

def problem_1k (A):
    answer = np.random.permutation(A)
    return answer

def problem_1l (x):
    answer = (x - np.mean(x))/np.std(x)
    return answer

def problem_1m (x, k):
    answer = np.repeat(np.atleast_2d(x),k)
    return ...

def problem_1n (X):
    m, n = np.shape(X)
    three_dim_mat = np.repeat(np.atleast_3d(X), n, axis=2)
    swap_mat = np.swapaxes(three_dim_mat, 1, 2)
    answer = np.sqrt(np.square(three_dim_mat)-np.square(swap_mat))
    return answer
