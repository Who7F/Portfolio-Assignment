import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    # Lets get some data to work with
    np.random.seed(19680801)
    data = np.sort(np.random.rand(100))

    print(f"Mean avarage is: {np.mean(data)}")
    print(f"Median avarage is: {np.median(data)}")
    print(f"Mode avarage is: {stats.mode(data)}")
    print(f"The variance is: {np.var(data)}")
    print(f"The standard deviation is: {np.std(data)}")
    

    plt.plot(data)
    plt.ylabel('Highly important numbers')
    plt.xlabel('Label your axes')
    plt.show()
    

    
    

if __name__=='__main__':
    main()
