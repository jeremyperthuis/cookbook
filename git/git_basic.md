# Git
---

#### 1. Config
```bash
# Persist credentials
git config credentials.helper store
# -> Then do a push or pull, type password/token and its good.
```

#### 2. Stash
```bash
# List Stash
git stash Lists
# Delete all stashs
git stash clear
# Apply stash
git stash apply {id}
```


#### 3. Undo things
```bash
# Remove last commit
git reset --hard HEAD~1
# Unstage file
git reset HEAD file
# Override local files
git reset --hard origin/<branch_name>
```
