import numpy as np
inputs = [[1.2,3.4,5.5],
          [9.9, 8.44, 7.989],
          [543487,846657,776465773]]
weights =[[1.5, 7.4, 8.6],
             [6.0, 7.6, 86.6],
             [1.55, 77.74, 88.6]]
bias = [3, 6,7]

"""output =  [inputs[0]*weights[0] +  inputs[1]*weights[1] + inputs[2]*weights[2] +bias,
           inputs[0]*weights1[0] +  inputs[1]*weights1[1] + inputs[2]*weights1[2] +bias1,
           inputs[0]*weights2[0] +  inputs[1]*weights2[1] + inputs[2]*weights2[2] +bias2]"""

outputS = np.dot(inputs,np.array(weights).T)+bias      
output2 = np.dot(outputS,np.array(weights).T)+bias
output3 = np.dot(output2,np.array(weights).T)+bias
output4= np.dot(output3,np.array(weights).T)+bias
output5 = np.dot(output4,np.array(weights).T)+bias
output6 = np.dot(output5,np.array(weights).T)+bias
output7 = np.dot(output6,np.array(weights).T)+bias
output8 = np.dot(output7,np.array(weights).T)+bias
output9 = np.dot(output8,np.array(weights).T)+bias
output10 = np.dot(output9,np.array(weights).T)+bias
output11 = np.dot(output10,np.array(weights).T)+bias
output12 = np.dot(output11,np.array(weights).T)+bias
output13 = np.dot(output12,np.array(weights).T)+bias
output14 = np.dot(output13,np.array(weights).T)+bias
output15 = np.dot(output14,np.array(weights).T)+bias
output16 = np.dot(output15,np.array(weights).T)+bias

print(output16)