import numpy as np

def calculate(list):
    arr = np.array(list)
    arr = arr.reshape(3,3)
    calculations = {
       'mean': [np.mean(arr, axis=0).tolist(),np.mean(arr, axis=1).tolist(),np.mean(arr).tolist()],
       'var' : [np.var(arr, axis=0).tolist(),np.var(arr, axis=1).tolist(),np.var(arr).tolist()],
       'std' : [np.std(arr, axis=0).tolist(),np.std(arr, axis=1).tolist(),np.std(arr).tolist()],
       'max' : [np.max(arr, axis=0).tolist(),np.max(arr, axis=1).tolist(),np.max(arr).tolist()],
       'max' : [np.min(arr, axis=0).tolist(),np.min(arr, axis=1).tolist(),np.min(arr).tolist()],
      'sum' : [np.sum(arr, axis=0).tolist(),np.sum(arr, axis=1).tolist(),np.sum(arr).tolist()]
       }
    return calculations
