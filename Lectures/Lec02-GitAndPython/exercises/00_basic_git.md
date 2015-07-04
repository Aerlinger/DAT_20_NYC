# Basics of Maintaining a repostory

1. Create your own repository on Github with the 'New Repository' button
1. For the project name enter "yourinitials_DAT20" and click 'Create
   Repository'
1. Within your terminal create a new folder that you want to push

    ```bash
    $ cd    # navigates to my home directory (on Mac/Unix this is `/Users/Name` which is aliased as ~)
    $ mkdir DAT20  # Make a new empty directory called DAT20
    $ cd DAT20    # Navigate to the new folder (TIP: use tab to autocomplete!!)
    $ touch Readme.md   # Create an empty README file
    ```

1. Editing the readme:

   #### On mac:
   ```bash
   $ open . # Open the newly created folder (we can also do `open
   Readme.md`)
   $ Open the created readme in your text editor
   ```
   
   #### Unix:
   `$ vim Readme.md`
   OR 
   `$ nano Readme.md`
     
   #### Windows:
   Navigate to the file within Windows Explorer and open it with any text editor.

1. Add the following markdown to the Readme.:

   ```markdown
   # <Your name>'s General Assembly DAT 20 Repository
   
   ---
   
   <A short description: Whatever you'd like>
   
   [Link to Github Repository](<enter the repository url here>)
   
   ```
   
   Feel free to be creative. As a reminder, there's a very useful Markdown reference for Github here:
   https://help.github.com/articles/github-flavored-markdown/

1. Type `git status`. What do you see?
   ```
   fatal: Not a git repository (or any of the parent directories): .git
   ```

1. We'll need to initialize git within our directory before we can do
   anything else.
   ensure your working directory is within to your newly created folder (use `pwd`
to **p**rint **w**orking **d**irectory). Now initialize a new git repository using the command `git init`. 
  - Git creates a hidden folder named `.git` which it uses to take
snapshots (files starting with a '.' are hidden files by Unix convention
you can use `ls -la` to to **l**ist **a**ll files in your present
working directory).
1. Type `git status` again. What do you see?
   ```
   On branch master
   
   Initial commit
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
   
     Readme.md
   
   nothing added to commit but untracked files present (use "git add" to
   track)
   ```
  - *What git is telling you:* Git is now watching for changes in this directory and sees that you've added a file called `Readme.md` which it isn't yet tracking. Git doesn't track changes to files until you
explicitly tell git to do so using the command `git add`. The collection of directories and files being tracked by git is called the 'index'.
1. Let's add our readme to the index by run the command `git add readme.md` (*Again*: get familiar with
   tab-completion, it will save you time!)
1. Run `git status` again. What changed? (Look closely)
  - Git has "staged" our changes meaning that it's taken a *temporary*
snapshot of the state of the Readme file. The place where Git stores
these temporary snapshots is called the staging area.
  - What is the difference between the "index" and "staging area"
1. Again, make a minor edit to Readme.md and run `git status` What do
   you see now?

  It should look similar to the following: 

   ```
   On branch master
   Changes to be committed:
     (use "git reset HEAD <file>..." to unstage)
   
     modified:   Readme.md
   
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git checkout -- <file>..." to discard changes in working
   directory)
   
     modified:   Readme.md
   ```
  - Git took a snapshot of Readme.md when you ran `git add`. Now that you've changed the
Readme file after the snapshot was taken with `git add`, git is telling
you that you have some new changes your minor edits just now that are not yet being tracked by
git. This is what is meant by "Changes not staging for commit" you added
with `git add`.

1. Let's look at what changed. We can do this through the command `git diff`. What is git showing you?
1. It's always a good idea to review the code we've written before
   committing our changes. Type `git diff --cached` Briefly describe what this is showing and how
it differs from `git diff`.
1. Add your changes to the Readme again calling `git add .`
1. "Commit" the snapshot with a simple message. `git commit -m "First commit!"` 
  - What does `git status` show now?
1. View the git history: `git log`
1. Finish the rest of the instructions shown on github:
   ```
   git remote add origin https://github.com/<username>/<directory>.git
   git push -u origin master
   ```
1. You should now be able to access your repository.
2. Within the github project page click the `Readme.md` file and edit it by clicking the :pencil2: icon near the top right.
3. Again, make some edits, feel free to be creative. Add a commit message and click the "commit changes" button when you're done.
4. You should immediately see your changes
5. go back to your terminal and type `git pull` to retrieve the latest changes from github.
6. Again type `git log` to view the history. You should see your latest commit along with the original.
6. **Celebrate!** :clap: :clap: :+1: :beers:

---

## The most common commands

Git is a complex tool but 99% of the time you'll be using maybe 1% of git commands.

### The "1%" (in order of appearance):
   - `git init` *(telling git to track a new repository)*
     OR 
   - `git clone` *(Existing repository)*
   - `git add <filename(s)>` *add file changes to staging area. Also adds file to index if not yet tracked by git*
   - `git status`  *files added/changed or staged since last commit*
   - `git diff`  *"difference" of changes since last commit*
   - `git diff --cached` *to see diff of staged changes*
   - `git commit -m "<commit message>"`  *Commit our 'snapshot' to the git history*
   - `git log` *View git history*
   - `git remote add <remote name e.g. 'origin'> <remote url e.g. 'github.com...'>` *Where git pushes/pulls from*
   - `git push` *update remote from local changes*
   - `git pull` *update local from remote changes*

---

**Part of your homework will involve making basic edits to this repository
so be sure that you're comfortable with the above workflow**
