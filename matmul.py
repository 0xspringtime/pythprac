import time
import numpy as np

N = 4096

if __name__ == "__main__":
    #N^2
    A = np.random.randn(N, N).astype(np.float32)
    #N^2
    B = np.random.randn(N, N).astype(np.float32)


    #N^2 output cells with 2N compute each
    flop = N*N*2*N #The first N*N term represents the number of elements in one matrix, and the second N term represents the number of operations required to multiply each element in one row of the first matrix by each element in one column of the second matrix. The 2 term represents the fact that there are two summations performed for each element in the resulting matrix.
    print(f"{flop / 1e9:.2f} GFLOP")

    st = time.monotonic()
    C = A @ B
    et = time.monotonic()
    s = et-st

    print(f"{flop/s * 1e-12:.2f} TFLOP/S") 
