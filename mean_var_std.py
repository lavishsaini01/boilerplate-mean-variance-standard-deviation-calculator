import numpy as np

def calculate(list):
    arr = np.array(list)
    arr = arr.reshape(3,3)
    calculations = {
       'mean': [np.mean(arr, axis=0),np.mean(arr, axis=1),np.mean(arr)],
       'var' : [np.var(arr, axis=0),np.var(arr, axis=1),np.var(arr)],
       'std' : [np.std(arr, axis=0),np.std(arr, axis=1),np.std(arr)],
       'max' : [np.max(arr, axis=0),np.max(arr, axis=1),np.max(arr)],
       'max' : [np.min(arr, axis=0),np.min(arr, axis=1),np.min(arr)],
       'sum' : [np.sum(arr, axis=0),np.sum(arr, axis=1),np.sum(arr)]
       }
    return calculations
