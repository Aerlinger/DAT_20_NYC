# Class 5 Homework 
**Manipulating and Visualizing Data**
 
*Due before class on 4/2/2015*

## Part I. Reviewing Existing Code

Check out this excellent example of [data wrangling and exploration in Pandas](http://nbviewer.ipython.org/github/cs109/content/blob/master/lec_04_wrangling.ipynb).

### Goals:
  * Read through the **entire** IPython Notebook.
  * As you get to each code block, **copy it into your own Python script** and run the code yourself. Try to understand exactly how each line works. You will run into Python functions that you haven't seen before!
  * Explore the data on your own using Pandas. At the bottom of your script, write out (as comments) **two interesting facts** that you learned about the data, and show the code you used to find those facts.
  * Create **two new plots** that show something interesting about the data, and save those plots as files. Include the plotting code at the bottom of your script.
      
### Tips:
  * You can ignore everything in the first code block except the three `import` statements.
  * Rather than downloading the data, you can read the file directly from its URL.
  * You may get a warning message a few times when running the code. The code still worked, so you can ignore the message (or you can figure out how to rewrite the code to not trigger the warning).
  * The plotting code calls matplotlib directly instead of using Pandas plotting, but the effect is the same:
      * matplotlib: `plt.hist(data.year, bins=62)`
      * Pandas: `data.year.hist(bins=62)`
  * In the plotting code, don't run `remove_border()`.
  * Don't worry about running (or trying to understand) the code in the "Small Multiples" section.


## Part II. Exploring And Visualizing Data

In the `data` folder you'll find included the file `bikeshare.csv`. This file contains data related to number of riders (casual, members, and total) for each hour, compared to stats for that time, such as temperature, windspeed. the file `bikeshare.txt` will explain it in more detail.

### Goals:
  * Explore the data in both hourly and daily counts. You'll need to aggregate by day to generate the daily data.
  * Visualise the relationships between the ridership and different features.
  * Explain which features seem to be the strongest indicators for each type of ridership (casual and noncasual). Do certain features come off as better tells for one over the other?
  * Summarise your results.
  * **Extra**: Business application. Given this information, what suggestions could be made to improve the ridership program? Consider this open field, since we only have aggregated stats and not individual ridership here.

## What's due:
* **For part I:** Python scripts with comments and image files for plots 
* **For part II:** A notebook that goes through the data exploration model
    * acquires and imports the data
    * cleans it up (create the daily from the hourly)
    * explores the two data sets for patterns
    * summarises and explains the results
    * Please upload this notebook to your github (the `.ipynb` file), or copy and paste the file's contents into a gist.

Create a pull request in the DAT_20_Students repository just as we have in previous assignments. ** Make sure all changes in your pull request are within your own folder. In other words, your pull request should be scoped within `DAT_20_Students/<YourFolder>/Assignment04` **  

## What we're measuring
* **Visualisations vs explanation:** how accurately can you explain the visuals you generate? How well do they capture the story about the data?
* **Cleanliness and organization:** how approachable is this notebook? Is it something a colleague or classmate can easily follow?
