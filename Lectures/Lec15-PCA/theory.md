# Principal Components Analysis (PCA) and Singular Vector Decomposition (SVD)
*From Ed's DAT course: (https://github.com/podopie/DAT18NYC/edit/master/examples/assignment1.md)*

Principal Components Analysis (PCA): creates new fewer composite attributes that represent all the attributes. Singular Vector Decomposition: established feature extraction method that has a wide range of applications.

PCA is commonly used in Dimensionality Reduction. We have a lot of variables that are correlated but we can reduce the number of variables by categorizing them, find the best matrix with fewer variables that still can explain the data. SVD deals with data compression.

SVD and PCA are commonly used to solve complex systems such as neuroscience, photoscience, meteorology and oceanography - the number of variables to measure can be unwieldy and at times even deceptive, but the underlying dynamics can often be quite simple.

#####Application 1:
We are trying to understand some phenomenon by measuring
various quantities (e.g. spectra, voltages, velocities,
etc.) in our system. But we cannot figure out what is happening because the data appears clouded, unclear and even redundant.

#####Application 2: Image processing (source: UCLA)
We can use SVD to compress and recreate images. For example, we read in a jpeg (pansy.jpg) and plots it, first in color (when the image is stored as three matrices--one red, one green, one blue) and then in gray-scale (when the image is stored as one matrix). Then, using SVD, we can essentially compress the image. We can also recover the image to varying degrees of detail as we recreate the image from different numbers of dimensions from our SVD matrices. We can see how many dimensions are needed before you have an image that cannot be differentiated from the original.

#####Application 3: neuroscience (source: wikipedia)
In neuroscience, PCA is also used to discern the identity of a neuron from the shape of its action potential. Spike sorting is an important procedure because extracellular recording techniques often pick up signals from more than one neuron. In spike sorting, one first uses PCA to reduce the dimensionality of the space of action potential waveforms, and then performs clustering analysis to associate specific action potentials with individual neurons.

The name of the Algorithm I read was Apriori It solves the problem of Association. the Algorithm basically looks at if and else conditions and stores the number of frequency the condition is met. once its done , It can calculate the probability of an item present just by looking at the antecedent. This algorithm can be widely usued in online marketing where recommendations can be made for purchase upon selecting an specified item. In a cosmetics facory setting , this algorithm can be applied to predict mechanic downtime issues with unique packiging. If there is a type of cap that causes issues on two or three pieces of equipment or a certain type of jar causing downtimes on other pieces of equipment. we can use this algorithm to calculate the probablity of equipment downtime based on packaging profile. Also in a factory setting , as assoication can be made in the tool crib where we can determing the tools that have a high probaility of being used at the same time to be stored in a close proximity to save time for the mechanics to be able to acquire tools in a timely fashion.
