import numpy as np
import pandas as pd

inputfile = 'F:\TrainingData\M05.csv'

df0 = pd.read_csv(inputfile)
train_values = np.random.randint(0, 384, (304))
#384 is just the total number of audios in the torgo csv--I'm basically picking 80% of the total by random to put into the training file

for value in train_values:
    df1 = df0[df0['Numbers'] == train_values]
    file_name_1 = "train.csv"
    df1.to_csv(file_name_1, index=False)

for value in train_values:
    df2 = df0[df0['Numbers'] != train_values]
    file_name_2 = "inter.csv"
    df2.to_csv(file_name_2, index=False)


#repeating the above code to split the intermediate into test.csv and dev.csv

intermediate = "inter.csv"

df3 = pd.read_csv(intermediate)
inter_values = np.random.randint(0, 80, (40))

for value in train_values:
    df4 = df3[df3['Numbers'] == train_values]
    file_name_3 = "Train.csv"
    df4.to_csv(file_name_3, index=False)

for value in train_values:
    df5 = df3[df3['Numbers'] != train_values]
    file_name_4 = "Test.csv"
    df5.to_csv(file_name_4, index=False)
