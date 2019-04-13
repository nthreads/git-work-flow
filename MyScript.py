# cd <directory> // go to directory of your project
# git init  // This will initialize 
# git add . // Add all files of current directory to git staging (temporary storage)
# git commit -m "This is your first commit"

# git branch // check all your branches and selected branch with sterik
# git branch develop // create 'develop' branch
# git checkout develop // select develop branch
# git commit -am "Add all changes to stagging and write message altogather"

# git checkout -b feature/new-feature // create and select new branch 'feature/new-feature'
# git commit -am "Now we are commiting everything on 'feature/new-feature' branch"

# git checkout develop // select develop branch for merging new-feature
# git merge feature/new-feature // this will merge 'feature/new-feature' into 'develop' branch

# git flow init -d // init flow with default settings