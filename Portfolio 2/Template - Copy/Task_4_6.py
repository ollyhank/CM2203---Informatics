#
# In this file please complete the following tasks:
#
# Task 4 [3] The curse of k
# Independent inquiry time! Picking the right number of neighbours k in the kNN approach is tricky.
# Find a way you could approach this more rigorously.
# In comments, state the approach you could use, and provide a reference to it.
# The reference needs to be to a handbook or peer-reviewed publication; a link to an online tutorial
# will not be accepted.

'''
I used this articel: https://www.researchgate.net/publication/315344892_A_case_based_method_to_predict_optimal_k_value_for_k-NN_algorithm
from the Journal of Intelligent & Fuzzy fuzzy systems as well as 
as the base of my research

The proposed method of finding the most suitable value of K in this paper is based off getting the best
understanding of the data set and the structure and underlying properties of it before Knn is run.
This involves use statistical features of the dataset such as size, number of classes, number of features 
as well as creating a local complexity profile which is a 'measure which reflects the complexity of the envirnoment 
of an example'. Low complexity is indicative of a neighbourhood of other datapoints in the same class compared 
a high complexity which would indicate the datapoint is swarmed by other classes. From this complexity profile 
we analyse the curve created by finding multiple examples and creating their local profiles. we then analyse this 
curve getting information such as the mean, mode, median, interquartile range and sknewness of the curve. from this
grid search is used to find the optimum value of k for each of the different examples. 
when needed a new dataset where the optimum value of k is yet to be found, will have the local profile created  for it
and then a prediction algorithm (in the paper they use Random Forest decision tree method) to get an optimum value of 
K due to the relationship between the metadata (local complexity and dataset attributes) and previously calculated 
optimum values of K.

After experiments this paper found they were accurate to within a small magnitude of absolute error (MAE) 
which was stated as 4%, in 84% of the datasets tested. 



'''

# Task 6 [3] I can do better!
# Independent inquiry time! There are much better approaches out there for image classification.
# Your task is to find one, and using the comment section of your project, do the following:
# •	State the name of the approach, and a link to a resource in the Cardiff University library that describes it
# •	Briefly explain how the approach you found is better than kNN in image classification (2-3 sentences is enough).


'''
I propose the use of support vector machine(SVMs) as an alternative to K-Nearest Neighbour
Support vector machines data analysis, machine learning and applications by Boyle, Brandon H. - 
https://librarysearch.cardiff.ac.uk/permalink/44WHELF_CAR/1fseqj3/alma9911764269202420

whilst KNN and SVM have reasonably similar accuracy in simple datases, when the data becomes more complicated 
SVM becomes far more accurate than KNN. KNN also relies heavily on an optimal select of a K value. SVM also 
allows for the addition of a kernal to allow SVM to tackle higher dimension problems with a lower computational
cost. SVM has also proven to have less sensitivity to changes in the size of sample sizes for training data, 
showing it performas better in both smaller and larger training data sets.



'''





#########
#sd
dsds
##/