# Assignment 5: Quantitative analysis of the bikeshare dataset using regression.
**Due Date: 4/9**

In this assignment we'll be exploring the bikeshare dataset in more depth using regression. 

## Part I. 
1. Read in the bikeshare data to a pandas dataframe just as you did for the previous assignment.
2. Split the dataframe horizontally into two separate dataframes each having N/2 rows. Call the dataframe with first N/2 rows `bikeshare_train`, and the latter half `bikeshare_test`  
3. Using the `bikeshare_train` dataframe run a regression with `cnt` as our target variable, and `temp`, `atemp`, `hum`, `workingday`, `hour`, `weathersit` as the feature variables. Specify the R^2 value.
We'll call this our **training model** The resulting model should have one more coefficient than the number of feature variables.
4. Describe the error (in terms of R^2) between the model you just calculated and the **bikeshare_test**. Is this higher or lower than the R^2 of the previous step? What's the reason for this difference?
5. Create a binary variable for rush hour defined by 6-9am & 4-6pm.
6. Run the regression again. Using a similar process used in steps 2 and 3, assert whether this improves the results or not. Why? (You should be able to explain this quantitatively) 

## Part II:

Provide answers to these questions in your own words:

1. The error you calculated in step 4 is called generalization error. Explain why it's called generalization error and why it's important when evaluating our regression model. 
2. Of the features you used for regression above, which one best explains `cnt`?
3. Which variables in the dataset are correlated and how do these affect your regression?
4. How would the p-value of our regression change as we took smaller subsets of the dataframe to build our training model?  

## Bonus:
- Experiment with using some of the other variables in the dataset to improve your model
- Try using polynomial regression to improve your model

# Things to pay attention to:
 
Weathersit is clearly a categorical variable: `plt.hist(bike_dat.weathersit)`
Not all variables are linearly independent.


# Additional resources

**Statsmodels documentation on linear regression:**
http://statsmodels.sourceforge.net/devel/regression.html

