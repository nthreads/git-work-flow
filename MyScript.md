# Initialize git and first commit

 cd <directory> // go to directory of your project
 git init  // This will initialize 
 git add . // Add all files of current directory to git staging (temporary storage)
 git commit -m "This is your first commit"

# Create develope branch

 git branch // check all your branches and selected branch with sterik
 git branch develop // create 'develop' branch
 git checkout develop // select develop branch
 git commit -am "Add all changes to stagging and write message altogather"

# Create new-feature branch

 git checkout -b feature/new-feature // create and select new branch 'feature/new-feature'
 git commit -am "Now we are commiting everything on 'feature/new-feature' branch"

# Merge 'feature' branch into 'develop' branch

 git checkout develop // select develop branch for merging new-feature
 git merge feature/new-feature // this will merge 'feature/new-feature' into 'develop' branch

# Installed and Initialize git flow
 brew install git-flow //Install git flow
 git flow init -d // init flow with default settings
 git flow feature finish new-feature // Merged feature/new-feature into develop, delete 'feature/new-feature' branch and selected develop branch

# new-feature using git flow command
 git flow feature start a-new-feature // A new branch 'feature/a-new-feature' was created, based on 'develop' - You are now on branch 'feature/a-new-feature'