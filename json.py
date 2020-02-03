import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns

crew = ["Ed", "Kelly", "Alara", "Bortus", "John", "Claire"]

print(len(crew)) 
print("Captain {}.".format(crew[0]))
for member in crew[1:len(crew)-1]:
    print("{} reporting for duty, sir!".format(member))
print(crew[0])

