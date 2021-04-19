import pandas as pd

def main():
    # Read in CSV result file with pandas
    df1 = pd.read_csv('responses.csv')

    # convert df into list of 3-tuples
    tuple_list = []
    for i, row in df1.iterrows():
      tuple_list.append((row['workerid'], row['response'], row['label']))

    # outputted EM algo results
    em_list = em_vote(tuple_list, 1000)

    # outputs CSV's of responses
    df2 = pd.DataFrame(em_list, columns=['response', 'label'])
    df2.to_csv('output.csv', index=False)

if __name__ == '__main__':
    main()

'''
=========================
Main Function for EM Algo
=========================
'''
def em_vote(rows, iter_num):
    confusion_matrix = initialize_workers(rows)

    # performs numerous iterations of EM algo based on iter_num
    for i in range(iter_num):
      results, matrix = em_iteration(rows, confusion_matrix)
      confusion_matrix = matrix

    # adds the final results into a tuple_list answer
    tuple_list = []
    for result in results:
      if results[result]['yes'] > results[result]['no']:
        tuple_list.append((result, 'yes'))
      else:
        tuple_list.append((result, 'no'))

    tuple_list.sort()
    return tuple_list

'''
=======================
EM Algorithm Components
NOTE: matrix boxes are represented by (x, y), 
      where x is the majority and y is the individual response
=======================
'''

def em_iteration(rows, worker_qual):
    labels = em_votes(rows, worker_qual)
    worker_qual = em_worker_quality(rows, labels)
    return labels, worker_qual


def em_votes(rows, worker_qual):
    labels = initialize_labels(rows)

    # compute labels
    for row in rows:
      matrix = worker_qual[row[0]]
      if row[2] == 'yes':
        labels[row[1]]['yes'] += matrix[('yes', 'yes')]
        labels[row[1]]['no'] += matrix[('no', 'yes')]
      else:
        labels[row[1]]['yes'] += matrix[('yes', 'no')]
        labels[row[1]]['no'] += matrix[('no', 'no')]

    # normalize labels
    for label in labels:
      if labels[label]['yes'] > labels[label]['no']:
        labels[label]['yes'] = 1
        labels[label]['no'] = 0
      else:
        labels[label]['yes'] = 0
        labels[label]['no'] = 1
    return labels


def em_worker_quality(rows, labels):
    workers = reset_workers(rows)

    # recompute worker matrices
    for row in rows:
      true_yes = labels[row[1]]['yes']
      if row[2] == 'yes' and true_yes == 1:
          workers[row[0]][('yes', 'yes')] += 1
      elif row[2] == 'yes' and true_yes != 1:
          workers[row[0]][('no', 'yes')] += 1
      elif row[2] != 'yes' and true_yes == 1:
          workers[row[0]][('yes', 'no')] += 1
      else:
          workers[row[0]][('no', 'no')] += 1

    # normalize matrices
    for row in rows:
        top_total = workers[row[0]][('yes', 'yes')] + workers[row[0]][('yes', 'no')]
        bottom_total = workers[row[0]][('no', 'yes')] + workers[row[0]][('no', 'no')]

        workers[row[0]][('yes', 'yes')] /= top_total
        workers[row[0]][('yes', 'no')] /= top_total
        workers[row[0]][('no', 'yes')] /= bottom_total
        workers[row[0]][('no', 'no')] /= bottom_total

    return workers

'''
Initialization and Reset Functions for each EM Iteration
'''

def initialize_workers(rows):
  d = {}
  for row in rows:
    if row[0] not in d:
      d[row[0]] = {('yes', 'yes'): 1, ('yes', 'no'): 0, ('no', 'yes'): 0, ('no', 'no'): 1}
  return d

def reset_workers(rows):
  d = {}
  for row in rows:
    if row[0] not in d:
      d[row[0]] = {('yes', 'yes'): 0, ('yes', 'no'): 0, ('no', 'yes'): 0, ('no', 'no'): 0}
  return d

def initialize_labels(rows):
  d = {}
  for row in rows:
    if row[1] not in d:
      d[row[1]] = {'yes': 0, 'no': 0}
  return d