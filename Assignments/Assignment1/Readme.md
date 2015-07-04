#####Due before class on Tuesday 3/17/15

---

##I. Before you start:

Make sure you've completed the course prework if you haven't already! We
want to make sure that everyone is able to use the necessary tools on
their computer so we can use our time effectively in class. You received
this document in the GA welcome email from Dan, but I've included it in
this email as well.
Make sure you're able to able to access your terminal/command line
(Terminal.app on mac, run -> cmd on Windows)
Make sure you're able to run the following commands from your
terminal/command line:


  ```
   python --version  (should start with 2.7)
   git --version
   ipython --version
```

The following tutorial from Github/Codeschool is strongly recommended if
you're new to git: https://try.github.io/levels/1/challenges/1


##II. The Assignment

####1. clone the class repository using git if you haven't already:

We did this at the end of class on Thursday, but I wanted to include
specific directions here as well. 

First, navigate to a folder you'd like to clone the class repository and
run the following command:

```
git clone https://github.com/ga-students/DAT_20_NYC.git
```

`git clone` is a lot like a simple download, it just retrieves the git
repository as a folder from the specified URL into a folder on your
local machine.

If you've already cloned the repository following the lecture on
Thursday: be sure to pull the latest updates by navigating to the folder
in your terminal where you cloned the repository using cd
path/to/directory then calling running the command git pull. The git
pull command tells git to fetch the latest changes from the remote
repository on Github and merge the changes with your local repository
(the folder where you originally cloned the remote repository using the
above URL).

If you don't have access to the repository please let Deepti, Josh, or
myself know ASAP, their emails are CCed to this email. Also be sure to
let us know If you can't access the terminal or the `git` command in
your terminal.


####2. Read and run the SimpleDemo.py file within the repository

Navigate to Assignments/Assignment1 within the repository and run:

```
python SimpleDemo.py
```


####3. Email me with the output of SimpleDemo.py

As an example, my terminal output looks like this:

```
Python installation:
2.7.9 (default, Feb 10 2015, 01:55:35)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)]

Scientific python modules
Pandas version:  0.15.2
Numpy version:  1.9.1
Scikit learn version:  0.15.2
Matplotlib version:  1.4.2
Scipy version 0.15.1
Bokeh version:  0.8.1
Statsmodels version:  0.6.1
IPython version:  2.4.1
```

Also include the output of the following commands when run from your
terminal:

```
python --version
git --version 
ipython --version
```

Your version numbers may differ slightly depending on when the above
modules were installed.

*If you've done the prework, the above assignment should take less than
20 minutes!!* If it's taking longer please reach out to me or the TAs
and we'll help you out.

Also, feel free to reach out with any questions or concerns you may
have.

