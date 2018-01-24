
import util
from pprint import pprint
import random
import numpy as np
from math import *
from decimal import Decimal
PRINT = True

class network(object):
   def __init__(self, nNeurons):
     self.nNeurons = nNeurons
     self.nLayers = len(nNeurons)
     self.biasWeights = [np.random.randn(i, 1) for i in nNeurons[1:]]
     self.weights = [np.random.randn(b,a) for a,b in zip(nNeurons[:-1], nNeurons[1:])]

# emulates sigmoidal function
def sigmoid(z):
  np.seterr(all='ignore')
  return 1.0/(1.0+ np.exp(-z))

# computes activation of one neuron'
def activate(weightArr, inputs, net, countBig, countSmall):
  np.seterr(all='ignore')
  bias = net.biasWeights[countBig][countSmall][0]
  return sigmoid(np.dot(inputs, weightArr) + bias)

# computes the activation of all the neurons in a layer and outputs an array of all the neurons in that layer
def activateLayer(weightArr, inputLayer, net, countBig):
  neuronsInLayer = []
  count = 0
  for w in weightArr:
    neuronActVal = activate(w, inputLayer, net, countBig, count)
    neuronsInLayer.append(neuronActVal)
    count = count + 1
  return neuronsInLayer

# do forward pass
def forwardPass(net, inputData):
  usableInputData = inputData
  allActivations = []
  allActivations.append(usableInputData)
  count = 0
  for w in net.weights:
    # print usableInputData
    usableInputData = activateLayer(w, usableInputData, net, count)
    allActivations.append(usableInputData)
    count = count + 1
  return allActivations

def getPredictedOutput(allActivations):
  indexOfAns = len(allActivations) - 1
  index = np.argmax(allActivations[indexOfAns])
  return index


def vectorizeActualOutput(z):
  yindex = z
  y = [0]*10
  y[yindex] = 1
  return y

def sigmoidDerivative(z):
  np.seterr(all='ignore')
  return ((sigmoid(z))*(1- sigmoid(z)))

def backprop(trainingData, trainingLabel, i, net):
  # print "ENTERS HERREE"
  # net = network([len(trainingData[0]), 15, 10])

  
  # for i in range(len(trainingData)):
  xvector = trainingData[i].values()
  y = trainingLabel[i]
  yvector = vectorizeActualOutput(y)

  # predictedArr = forwardPass(net, xvector) #the activations
  # predictedVal = getPredictedOutput(predictedArr)

  # while (predictedVal != y):
  #   print "y: ",y
  #   print "pred: ",predictedVal
#forward pass
  predictedArr = forwardPass(net, xvector) #the activations
  predictedVal = getPredictedOutput(predictedArr)
  prVect = vectorizeActualOutput(predictedVal)
  outputLayerWeightsIndex = net.nLayers - 1


  allErrorSignals = []
  deltaJ = []
  outputArr = predictedArr[outputLayerWeightsIndex]
  # print outputArr
  for a in range(len(outputArr)):
    vari = sigmoidDerivative(outputArr[a]) * (yvector[a] - outputArr[a])
    deltaJ.append(vari)
  allErrorSignals.append(deltaJ)

  deltaI = []
  numOfHiddenLayers = net.nLayers - 2
  for l in range(numOfHiddenLayers, 0, -1):
    layerWeights = net.weights[l]
    # print "HEREEEEEEEEEEEEE"
    # print layerWeights
    prevNNeurons = len(layerWeights[0])
    # print prevNNeurons
    nextNNeurons = len(layerWeights)
    prevActs = predictedArr[l]
    nextActs = predictedArr[l+1]
    for n in range(prevNNeurons):
      weightsToSum = (layerWeights[:,n])
      vari = sigmoidDerivative(prevActs[n]) * np.dot(weightsToSum, allErrorSignals[0])
      deltaI.append(vari)
    allErrorSignals.insert(0, deltaI)

  alph = 0.9
  aphdec = 0.01
  outct = 0
  for weightArr in net.weights:
    ct = 0
    for w in weightArr:
      alph = alph = aphdec
      multiplyVal = allErrorSignals[outct][ct] * predictedArr[outct+1][ct]
      multipVal = [multiplyVal* x for x in w]
      alphMult = [alph * i for i in multipVal]
      w = [sum(j) for j in zip(w, alphMult)]
      net.weights[outct][ct] = w
      ct = ct + 1
    outct = outct + 1

  # print net.weights
  return net

def costDeriv(outputArr, y):
  return [a - b for a,b in zip(outputArr, y)]

      
# def backprop(trainingData, trainingLabel, i, net):
#   nabla_b = [np.zeros(b.shape) for b in net.biasWeights]
#   nabla_w = [np.zeros(w.shape) for w in net.weights]

#   xvector = trainingData[i].values()
#   y = trainingLabel[i]
#   yvector = vectorizeActualOutput(y)

#   activation = xvector
#   activations = [xvector]

#   zs = []
#   for b, w in zip(net.biasWeights, net.weights):
#     z = np.dot(w, activation) + b
#     zs.append(z)
#     activation = sigmoid(z)
#     activations.append(activation)

#   deltaTemp = costDeriv(activations[-1], yvector)
#   delta = [sigmoidDerivative(zs[-1]) * x for x in deltaTemp]
#   nabla_b[-1] = delta
#   nabla_w[-1] = np.dot(delta, activations[-2].transpose())

  # #feed forward and get activations
  # activations = forwardPass(net, xvector)
  # zs = []
  # for layer in activations:
  #   for activation in layer:
  #     for b, w in zip(net.biasWeights, net.weights):
  #       z = np.dot(w, activation)+b
  #       zs.append(z)

  # deltaJ = costDeriv(activations[-1], yvector) * sigmoidDerivative(zs[-1])
  # nabla_b[-1] = deltaJ
  # nabla_w[-1] = np.dot(deltaJ, activations[-2])
  # print nabla_b
  # allErrorSignals.append(deltaJ)

  # for l in xrange(2, net.nLayers):
  #   z = zs[-l]
  #   deriv = sigmoidDerivative(z)
  #   deltaI = np.dot()







