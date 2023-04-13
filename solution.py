import pandas as pd
import numpy as np


chat_id = 532569024 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.09
    n1 = len(x)
    n2 = len(y)
    c_alpha = np.sqrt(-0.5*np.log(alpha/2))/np.sqrt(n1+n2)
    d = np.max(np.abs(np.sort(x)-np.sort(y)))
    return d > c_alpha
