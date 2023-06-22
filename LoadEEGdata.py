
'''
Load EEG data 

'''
import scipy.io as sio
import numpy as np


class LoadEEGdata:
    def __init__(self):
        pass

    def load_data(self Æ¥Û,filename):
        data = sio.loadmat(filename)['data']
        return data
    
if __name__ == "__main__":
    LoadEEGData = LoadEEGdata()
    data = LoadEEGData.load_data('S1.mat')
    print(np.shape(data))
    njh hfhhhdasdasnbnbkk