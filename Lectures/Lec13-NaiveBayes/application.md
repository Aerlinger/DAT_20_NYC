Naive Bayes Classification
==========================
*From Ed's DAT course: (https://github.com/podopie/DAT18NYC/edit/master/examples/assignment1.md)*


Naive Bayes methods are a family of supervised learning algorithms used to solve classification problems in Data Science. They make use of Bayes theorem, assigning prior probabilities based on a set of training data. They are known as 'Naive' methods because they assume that all variables of the dataset are independent.

This is a very strong assumption, and therefore not an accurate predictor of the _probability_ of a test data point being in any given class. However, since the algorithm is only concerned with the classification of the data point - i.e. the _most likely_ class, this is not a problem. It turns out that in most cases, Naive Bayes algorithms do a good job of classifying the data.

The advantage of the 'Naive' assumption is that it makes the algorithm relatively simple, thereby allowing speedy processing. The number of parameters in the algorithm is linear in scale to the number of variables in the dataset, making it useful for dealing with LARGE samples or those with a large number of variables.

Uses
----

1. Naive Bayes algorithms perform particularly well with textual data. A common application is in spam email filters. Training data is used to identify a set of key words and phrases, which form the variables for the algorithm. New emails can then be run through the algorithm, and are classified as 'spam' or 'not spam' based on how often they contain these key words or phrases.

2. There are many other applications in which Naive Bayes methods can be used with textual data. For example, classifying a movie review as positive or negative based upon which words are contained within it.

3. Naive Bayes algorithms can be used in genomics to predict susceptibility to disease. Genomic datasets typically contain a very high number of features, so the dimensional scalability of Naive Bayes methods is important here.
e.g. http://www.ncbi.nlm.nih.gov/pubmed/21672907

