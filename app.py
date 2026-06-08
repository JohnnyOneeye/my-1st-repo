print(\
Hello
World\)


Removed the incorrect line from the program and created a new commit:

git add .
git commit -m "Removed incorrect line from program"
Why is it better to fix with a new commit rather than delete history?

Fixing mistakes with a new commit preserves the project's history and provides a clear record of what changed and why.
This improves accountability, makes collaboration easier, and allows developers to review or restore previous versions if needed.
Deleting history can hide important information and make troubleshooting more difficult.

Git Commands Used in Visual Studio Code

git init
git status
git add .
git commit -m "Initial commit"
git commit -m "Refactor code"
git commit -m "Removed incorrect line from program"
git log --oneline
git reset --soft HEAD~1
git revert <commit-hash>
git push origin main
