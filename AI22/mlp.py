# mlp.py
# -------------

# mlp implementation
import util
from pprint import pprint
import random
import numpy as np
from nn import*
PRINT = True

net = network([784,20,10])
class MLPClassifier:
  """
  mlp classifier
  """
  def __init__( self, legalLabels, max_iterations):
    self.legalLabels = legalLabels
    self.type = "mlp"
    self.max_iterations = max_iterations



  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~testtttt
  # inpp = [1,0]
  # inppp = [{(0,1):1, (1,1):0, (1,2): 1}, {(0,1):0, (1,1):0, (1,2): 1}]
  # outpp = [5,2]
  # backprop(inppp, outpp)
  # print forwardPass(Network, inpp)
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~testtttt

  def train( self, trainingData, trainingLabels, validationData, validationLabels ):
    global net
    for iteration in range(self.max_iterations):
      print "Starting iteration ", iteration, "..."
      for i in range(len(trainingData)):
          "*** YOUR CODE HERE ***"
          datumVals = trainingData[i].values()
          correct = trainingLabels[i]
          guess = getPredictedOutput(forwardPass(net, datumVals))
          # print "GUESS:",guess
          # print "CORRECT:", correct
          if(guess != correct):
            net = backprop(trainingData, trainingLabels, i, net)
            # continue
    
  def classify(self, data):
    guesses = []
    for datum in data:
      # fill predictions in the guesses list
      "*** YOUR CODE HERE ***"
      datumVals = datum.values()
      guess = getPredictedOutput(forwardPass(net, datumVals))
      guesses.append(guess)
    return guesses