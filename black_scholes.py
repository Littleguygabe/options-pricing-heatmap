import math
from scipy.stats import norm
def put(S, K, T, R, sd):
    d1 = (math.log(S/K) + (R  + 0.5 * sd**2) * T) / (sd * math.sqrt(T))
    d2 = d1 - sd * math.sqrt(T)

    put_price = K * math.exp(-R * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return put_price

def call(S, K, T, R, sd):
    d1 = (math.log(S/K) + (R + 0.5 * sd**2) * T) / (sd * math.sqrt(T))
    d2 = d1 - sd * math.sqrt(T)

    call_price = S * norm.cdf(d1) - K * math.exp(-R * T) * norm.cdf(d2)
   
    return call_price


