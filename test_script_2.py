import pandas as pd
import numpy as np

fct = pd.read_csv('Fct.csv', encoding='utf-8')
conv = pd.read_csv('RetentionFactors.csv', encoding='utf-8')

<<<<<<< HEAD
output_values = weight*conv_row_np*fct_row_np
output = np.append(fct_row["C_DESCR"], output_values)
#print(output)
=======
weights = [100, 200, 300, 400, 500]
normalised_weights = [i/100 for i in weights]
fct_numbers = [174, 13, 14, 73, 84]
conv_numbers = [431, 431, 431, 431, 431]
>>>>>>> 9939b04ceee9bd1c369f6bf467ea891d60cebb3d

output = [['RICE RAW MILLED', 431.5, 68.5, 1725.0, 34.0, 2.5, 391.0, 20.0, 47.5, 3.15, 6.175, 0.0, 0.22499999999999998, 0.27, 9.025, 0.0, 24.0, 0.0, 24.0, 24.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
for i in range(len(weights)):

<<<<<<< HEAD
#print(output)
=======
    fct_row = fct[fct["C_CODE"] == fct_numbers[i]]
    fct_row_np = np.array(fct_row)[0][3:]

    conv_row = conv[conv["R_Code"]==conv_numbers[i]]
    conv_row_np = np.array(conv_row)[0][2:]
>>>>>>> 9939b04ceee9bd1c369f6bf467ea891d60cebb3d

    output_value = normalised_weights[i]*conv_row_np*fct_row_np
    output_value = np.append(fct_row["C_DESCR"], output_value)
    print(output_value)
    output = np.append(output, [output_value], axis = 0)

<<<<<<< HEAD
s=tuple(var)

print(s)
=======
print(output)
print(pd.DataFrame(output))
>>>>>>> 9939b04ceee9bd1c369f6bf467ea891d60cebb3d
