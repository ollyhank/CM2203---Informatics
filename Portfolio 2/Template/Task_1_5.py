import argparse
import csv
import os
from sewar.full_ref import mse, scc, uqi
import cv2
from PIL import Image

#
# In this file please complete the following tasks:
#
# Task 1 [10] My first not-so-pretty image classifier
# By using the kNN approach and three similarity measures, build image classifiers.
# You need to implement the kNN approach yourself, however, you can use libraries for any similarity measures.
# You can assume that k=100 (if the code takes too long to run, feel free to decrease it to as low as k=10).
# You are allowed to use libraries to read and write to files, and to perform image transformations if necessary.

# Task 5 [6] Similarities
# Independent inquiry time! In Task 1, you were allowed to use libraries for image similarity measures.
# Pick two of the three measures you have used and implement them yourself!


# Please replace with your student id!!!
student_id = 'C2040032'

# This is the classification scheme you should use for kNN
classification_scheme = ['Female','Male','Primate','Rodent','Food']


# In this function I expect you to implement the kNN classifier. You are free to define any number of helper functions
# you need for this!
#
# INPUT: training_data      : a list of lists that was read from the training data csv (see parse_arguments function)
#        k                  : the value of k neighbours
#        sim_id             : value from 1 to 5 which says what similarity should be used;
#                             values from 1, 2 and 3 denote similarities from Task 1 that can be called from libraries
#                             values from 4 and 5 denote similarities from Task 5 that you implement yourself
#        data_to_classify   : a list of lists that was read from the data to classify csv;
#                             this data is NOT be used for training the classifier, but for running and testing it
#                             (see parse_arguments function)
# OUTPUT: processed         : a list of lists which expands the data_to_classify with the results on how your
#                             classifier has classified a given image


def condition_image(image_name):
    #read 2 images in for similarity comparison
    image = cv2.imread(image_name)

    #convert the images to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #resize image
    image = Image.fromarray(image)
    image = image.resize((100,100))
    new_name = 'Images/Student_Train1/' + str(image_name.split('/')[-1])
    image.save(new_name)
    print('Saved: ' + str(new_name))

    #image.show()
    return image


def open_image(link):

    name_elements = link.split('/')
    img_name = name_elements[0] +'/'+ name_elements[1] + '1/' + name_elements[2]
    image = cv2.imread(img_name)

    return image


def calculate_similarities(training_data):
    #calculating the simialrities between images using different measure methods

    similarity_data = []
    i = 1
    for x in training_data:
        i2 = 1
        row_similiarities = []
        for y in training_data:
            print('Calculating similarities for image ' + str(i) + ' with image ' + str(i2))
            image1 = open_image(x[0])
            image2 = open_image(y[0])

            #calculating mean squared error
            result_mse = mse(image1, image2)
            #calculating universal quality index
            result_uqi = uqi(image1, image2)
            #calculating spatial correlation coefficient
            result_scc = scc(image1, image2)

            row_similiarities.append([result_mse, result_uqi, result_scc])
            i2+=1

        similarity_data.append(row_similiarities)
        i+=1


    return similarity_data


def normalise_similarities(data):
    #normalising data between 0-100 so that each simialrity score has the same value

    mse_results = []
    uqi_results = []
    scc_results = []

    row_len = len(data[0])

    #getting all the values of each similarity check in a list
    all_mse = [y[0] for x in data for y in x]
    all_uqi = [y[1] for x in data for y in x]
    all_scc = [y[2] for x in data for y in x]

    #calculating the maximums and minums for calculation
    mse_max = max(all_mse)
    mse_min = min(all_mse)
    uqi_max = max(all_uqi)
    uqi_min = min(all_uqi)
    scc_max = max(all_scc)
    scc_min = min(all_scc)

    for x in data:
        for y in x:
            y[0] = round(((y[0] - mse_min)/(mse_max-mse_min)) * 100, 2)
            y[1] = round(((y[1] - uqi_min)/(uqi_max-uqi_min)) * 100, 2)
            y[2] = round(((y[2] - scc_min)/(scc_max-scc_min)) * 100, 2)

   
    return data


def average_similarities(data):
    #creating an average value for each similarity for each image, thereby create a 3dimensional coordinate



    pass

def get_k_neighbours(k, point, data):
    #


    pass

def kNN(training_data, k, sim_id, data_to_classify):
    processed = [data_to_classify[0] + [student_id]]
    # Have fun!
    header = training_data.pop(0)
    #for image in training_data:
    #    condition_image(image[0])

    similarity_data = []

    
    data = calculate_similarities(training_data)
    indexed_data = index_similarities(data)

    for items in indexed_data:
        print(items)
    


    return processed






##########################################################################################
# You should not need to modify things below this line - it's mostly reading and writing #
# Be aware that error handling below is...limited.                                       #
##########################################################################################

# This function reads the necessary arguments (see parse_arguments function), and based on them executes
# the kNN classifier. If the "unseen" mode is on, the results are written to a file.
def main():
    opts = parse_arguments()
    if not opts:
        exit(1)
    print(f'Reading data from {opts["training_data"]} and {opts["data_to_classify"]}')
    training_data = read_csv_file(opts['training_data'])
    data_to_classify = read_csv_file(opts['data_to_classify'])
    unseen = opts['mode']
    print('Running kNN')
    result = kNN(training_data, opts['k'], opts['sim_id'], data_to_classify)
    if unseen:
        path = os.path.dirname(os.path.realpath(opts['data_to_classify']))
        out = f'{path}/{student_id}_classified_data.csv'
        print(f'Writing data to {out}')
        write_csv_file(out, result)


# Straightforward function to read the data contained in the file "filename"
def read_csv_file(filename):
    lines = []
    with open(filename, newline='') as infile:
        reader = csv.reader(infile)
        for line in reader:
            lines.append(line)
    return lines


# Straightforward function to write the data contained in "lines" to a file "filename"
def write_csv_file(filename, lines):
    with open(filename, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(lines)


# This function simply parses the arguments passed to main. It looks for the following:
#       -k              : the value of k neighbours
#                         (needed in Tasks 1, 2, 3 and 5)
#       -f              : the number of folds to be used for cross-validation
#                         (needed in Task 3)
#       -sim_id         : value from 1 to 5 which says what similarity should be used;
#                         values from 1, 2 and 3 denote similarities from Task 1 that can be called from libraries
#                         values from 4 and 5 denote similarities from Task 5 that you implement yourself
#                         (needed in Tasks 1, 2, 3 and 5)
#       -u              : flag for how to understand the data. If -u is used, it means data is "unseen" and
#                         the classification will be written to the file. If -u is not used, it means the data is
#                         for training purposes and no writing to files will happen.
#                         (needed in Tasks 1, 3 and 5)
#       training_data   : csv file to be used for training the classifier, contains two columns: "Path" that denotes
#                         the path to a given image file, and "Class" that gives the true class of the image
#                         according to the classification scheme defined at the start of this file.
#                         (needed in Tasks 1, 2, 3 and 5)
#       data_to_classify: csv file formatted the same way as training_data; it will NOT be used for training
#                         the classifier, but for running and testing it
#                         (needed in Tasks 1, 2, 3 and 5)
#
def parse_arguments():
    parser = argparse.ArgumentParser(description='Processes files ')
    parser.add_argument('-k', type=int)
    parser.add_argument('-f', type=int)
    parser.add_argument('-s', '--sim_id', nargs='?', type=int)
    parser.add_argument('-u', '--unseen', action='store_true')
    parser.add_argument('training_data')
    parser.add_argument('data_to_classify')
    params = parser.parse_args()

    if params.sim_id < 0 or params.sim_id > 5:
        print('Argument sim_id must be a number from 1 to 5')
        return None

    opt = {'k': params.k,
           'f': params.f,
           'sim_id': params.sim_id,
           'training_data': params.training_data,
           'data_to_classify': params.data_to_classify,
           'mode': params.unseen
           }
    return opt


if __name__ == '__main__':
    main()
