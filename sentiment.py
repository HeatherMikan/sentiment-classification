# to run: python sentiment.py training.csv test.csv

import sys
import csv
import numpy as np



def buildModel(trainingData):
	rawData = open(trainingData, 'r').readlines()
	print(rawData)
	for line in rawData:
		rowList = line.split(',', 1)[1]
#		commentList = rowList[1].split(' ')
#		print(rowList[0])
#		print(commentList)


def predict(model, predictData):
	break

def main(argv):
	trainingData = argv[0]
	predictData = argv[1]
	buildModel(trainingData)
    predict(model, predictData)


if __name__ == "__main__": main(sys.argv[1:])