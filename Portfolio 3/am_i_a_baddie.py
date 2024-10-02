import argparse
import csv
from pycm import ConfusionMatrix

import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

classification_scheme = ['Female', 'Male', 'Primate', 'Rodent', 'Food']


def am_i_a_baddie(classified_data, attribute_data):
    # We attach the attribute value from attribute_data to classified_data
    c_data = classified_data[1:]
    a_data = attribute_data[1:]
    c_data.sort()
    a_data.sort()
    total_data = []
    for i in range(0, len(c_data)):
        total_data.append(c_data[i] + [int(a_data[i][2])])

    # We split up our results based on the value of the special attribute
    actual_class_0 = [row[1] for row in total_data if row[3] == 0]
    predicted_class_0 = [row[2] for row in total_data if row[3] == 0]

    actual_class_1 = [row[1] for row in total_data if row[3] == 1]
    predicted_class_1 = [row[2] for row in total_data if row[3] == 1]

    print(actual_class_0)
    print(actual_class_1)

    # We analyze how the classification turned out based on the special attribute value
    cm0 = ConfusionMatrix(actual_vector=actual_class_0, predict_vector=predicted_class_0, classes=classification_scheme)
    #  print("This is the confusion matrix for entries with attr 0.")
    #  cm0.print_matrix()
    print("These are various evaluation measures when we focus on the classified Females and Males with Attr 0.")
    t = cm0.stat(overall_param=[], class_param=["ACC", "PPV", "TPR", "FNR", "FPR"], class_name=['Female', 'Male'])
    cm1 = ConfusionMatrix(actual_vector=actual_class_1, predict_vector=predicted_class_1, classes=classification_scheme)
    #  print("This is the confusion matrix for entries with attr 1")
    #  cm1.print_matrix()
    print("*****************************************")
    print("These are various evaluation measures when we focus on the classified Females and Males with Attr 1.")
    cm1.stat(overall_param=[], class_param=["ACC", "PPV", "TPR", "FNR", "FPR"], class_name=['Female', 'Male'])
    # And now think about the results!
    print("Now look at your results. \n"
          "How often are accuracy, precision and recall higher on Attr 1 than they are on Attr 0? \n"
          "How often are false positive rates and false negative rates lower on Attr 1 than they are on Attr 0? \n"
          "Is your classifier performing much better on records with Attr 1 than it is on records with Attr 0? "
          "Or perhaps quite the opposite?\n"
          "If the answer is yes to any of these questions, chances are your classifier is biased. Uh oh!")


def main():
    opts = parse_arguments()
    if not opts:
        exit(1)
    print(f'Reading data from {opts["classified_data"]} and {opts["attribute_data"]}')
    classified_data = read_csv_file(opts['classified_data'])
    attribute_data = read_csv_file(opts['attribute_data'])
    print('Running analysis')
    print("*****************************************")
    am_i_a_baddie(classified_data, attribute_data)


# Straightforward function to read the data contained in the file "filename"
def read_csv_file(filename):
    lines = []
    with open(filename, newline='') as infile:
        reader = csv.reader(infile)
        for line in reader:
            lines.append(line)
    return lines


# This function simply parses the arguments passed to main. It looks for the following:
#       classified_data: csv file containing your classified data, as produced by Task_1_5 in Portfolio 2 using -u flag
#                         and the training/testing data supplied with this Portfolio
#       attribute_data: csv accompanying this coursework that extends testing data with additional information

def parse_arguments():
    parser = argparse.ArgumentParser(description='Processes files ')
    parser.add_argument('classified_data')
    parser.add_argument('attribute_data')
    params = parser.parse_args()

    opt = {
        'classified_data': params.classified_data,
        'attribute_data': params.attribute_data
    }
    return opt


if __name__ == '__main__':
    main()
