import naive_bayes as nb
import csv
import performance_diagram_stuff as pds
import reliability_curve_stuff as rcs
import numpy
from decimal import *

filename = 'melanoma_normalized_data_16.csv'
splitRatio = 0.67
dataset = nb.loadCsv(filename)
trainingSet, testSet = nb.splitData(dataset, splitRatio)
print('Split {0} rows into train={1} and test={2} rows'.format(len(dataset), len(trainingSet), len(testSet)))
summaries = nb.summarizeByClass(trainingSet)
predictions = nb.getPredictions(summaries, testSet)
probabilities = nb.getProbabilities(summaries, testSet)

# test - invert predictions
inverted_p = []
for pred in predictions:
    inv = 0
    if pred == 0:
        inv = 1
    inverted_p.append(inv)

accuracy = nb.getAccuracy(testSet, predictions)
print('Accuracy: {0}%'.format(accuracy))

accuracy = nb.getAccuracy(testSet, inverted_p)
print('Inverted Accuracy: {0}%'.format(accuracy))

true_labels = []
with open('predictions.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=',')
    for true, pred, inv in zip(testSet,predictions,inverted_p):
        true_labels.append(int(true[-1]))
        out = str(int(true[-1]))
        out += str(',')
        out += str(int(pred))
        out += str(',')
        out += str(int(inv))
        writer.writerow(out)

# # invert true vals
# inv_true = []
# for val in true_labels:
#     inv = 0
#     if val == 0:
#         inv = 1
#     inv_true.append(inv)

# # getcontext().prec = 300
# with open('probabilities.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     for true, prob in zip(inv_true, probabilities):
#         out = [true]
#         out.append(prob)
#         writer.writerow(out)


# filename = 'melanoma_normalized_data_16.csv'
# splitRatio = 0.67
# dataset = nb.loadCsv(filename)

# avg_acc_list = []
# min_acc = 0
# max_acc = 0

# # create an average
# for x in range(0,50):
    
#     trainingSet, testSet = nb.splitData(dataset, splitRatio)
#     # print('Split {0} rows into train={1} and test={2} rows'.format(len(dataset), len(trainingSet), len(testSet)))
#     summaries = nb.summarizeByClass(trainingSet)
#     predictions = nb.getPredictions(summaries, testSet)
#     probabilities = nb.getProbabilities(summaries, testSet)

#     # test - invert predictions
#     inverted_p = []
#     for pred in predictions:
#         inv = 0
#         if pred == 0:
#             inv = 1
#         inverted_p.append(inv)

#     accuracy = nb.getAccuracy(testSet, predictions)
#     #print('Accuracy: {0}%'.format(accuracy))

#     inv_accuracy = nb.getAccuracy(testSet, inverted_p)
#     #print('Inverted Accuracy: {0}%'.format(inv_accuracy))

#     # update stats
#     avg_acc_list.append(accuracy)
#     if accuracy < min_acc or min_acc == 0:
#         min_acc = accuracy
#     if accuracy > max_acc:
#         max_acc = accuracy

# avg_acc = 0
# for acc in avg_acc_list:
#     avg_acc += acc

# avg_acc = avg_acc / 50

# print('Average Accuracy: {0}%'.format(avg_acc))
# print('Min Accuracy: {0}%'.format(min_acc))
# print('Max Accuracy: {0}%'.format(max_acc))

