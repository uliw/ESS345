git pull

# Undo All Local Changes
git reset --hard HEAD

# Update Tracked Notebooks to Latest
git fetch; git reset --hard origin/master

# Nuke all Changes
git clean -qfdx; git fetch; git reset --hard origin/master
