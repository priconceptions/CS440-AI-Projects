# svm.py
# -------------

# svm implementation
import util
from sklearn import svm
PRINT = True

class SVMClassifier:
  """
  svm classifier
  """
  def __init__( self, legalLabels, max_iterations):
    self.legalLabels = legalLabels
    self.type = "svm"
    self.max_iterations = max_iterations
    self.svm = svm.LinearSVC()
      
  def train( self, trainingData, trainingLabels, validationData, validationLabels ):
    for i in range(self.max_iterations):
      print "Starting iteration ", iteration, "..."
      "*** YOUR CODE HERE ***"
      points = []
      for j in range(len(trainingData)):
        points.append(trainingData[j].values())
      self.svm.fit(points, trainingLabels)
        #util.raiseNotDefined()
    
  def classify(self, data ):
    guesses = []
    for datum in data:
      # fill predictions in the guesses list
      "*** YOUR CODE HERE ***"
      vector = util.Counter()
      for l in self.legalLabels:
        vector[l] = self.svm.predict(datum.values())
      #util.raiseNotDefined()
      
    return guesses

    guess = []
    for i in range(len(point)):
      guess.append(point[i].values())
    result = self.svm.predict(guess)
    return result
