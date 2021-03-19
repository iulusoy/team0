import numpy as np
import statistical as sl

if __name__ == "__main__":
    test = np.array((1, 1, 1.2, 1.3, 3.5, 2.0))
    dist = sl.euclidean_distance([0,2,4],[1,3,5],test)
    print('Found distance {}'.format(dist))
