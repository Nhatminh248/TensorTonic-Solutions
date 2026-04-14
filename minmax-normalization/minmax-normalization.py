import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.array(X, dtype=float)

    if X.ndim == 1:
        hi = X.max()
        lo = X.min()
    else:
        lo = X.min(axis = axis, keepdims=True)
        hi = X.max(axis = axis, keepdims=True)
    return (X - lo)/(hi - lo + eps)