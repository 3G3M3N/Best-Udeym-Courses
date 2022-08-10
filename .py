import numpy as np
import pandas as pd

df = pd.read_csv("udemy_courses.csv")
df

df["level"].value_counts()

df["subject"].value_counts()

