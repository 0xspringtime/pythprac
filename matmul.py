import time
import numpy as np

N = 4096

if __name__ == "__main__":
    #N^2
    A = np.random.randn(N, N).astype(np.float32)
    #N^2
    B = np.random.randn(N, N).astype(np.float32)


    #N^2 output cells with 2N compute each
    flop = N*N*2*N
    print(f"{flop / 1e9:.2f} GFLOP")

    st = time.monotonic()
    C = A @ B
    et = time.monotonic()
    s = et-st

    print(f"{flop/s * 1e-12:.2f} GFLOPS") 
