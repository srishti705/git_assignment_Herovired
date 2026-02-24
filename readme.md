# Ques1. Q1----You are part of a development team working on a Python application called "CalculatorPlus....
### Step1Created Repo , Clone the Repository (git clone https://github.com/your-username/git_assignment_HeroVired.git
cd git_assignment_HeroVired)

Step 2. Created dev baranch , add initial code calculator .py file , merge dev to main after creating version1.0.

<img width="1160" height="755" alt="image" src="https://github.com/user-attachments/assets/9d3a0215-200b-4354-ae92-29b0b49a344f" />







<img width="953" height="529" alt="image" src="https://github.com/user-attachments/assets/fc6f5418-cf8d-4108-922b-daba25b73134" />


Step 4: Add Collaborator - reviewing code

Step 5: Changing branch feature/sqrt , implementing squareroot , commit it , merge it in main.


<img width="1798" height="500" alt="image" src="https://github.com/user-attachments/assets/1a57edc6-0501-4842-b7db-4fa90c1ac2b2" />


# Q2 . Dealing with Large Storage file in git 

## Steps winget install Git.GitLFS

cd git_assignment_HeroVired

using macOs - brew install lfs

git lfs install

git checkout -b lfs

git lfs track "*.zip"

git add .gitattributes

git commit -m "Configure Git LFS for large files"

git add xyz.zip

git commit -m "Add 200MB+ large file tracked by Git LFS"

git push origin lfs

git clone https://github.com//git_assignment_HeroVired.git

cd git_assignment_HeroVired

git checkout lfs

ls -lh


<img width="2738" height="1216" alt="image" src="https://github.com/user-attachments/assets/ef99a9e8-3982-486d-94f0-1da37158606f" />


# Ques 3 geometry_calculator 

## Steps Create base branch git checkout -b geometry-calculator

Work on Rectangle Feature git checkout geometry-calculator git checkout -b feature/rectangle-area edit code git stash push -m "rectangle-area-incomplete"

Work on Circle Feature git checkout -b feature/circle-area # edit code git stash push -m "circle-area-incomplete"

Finish Circle Feature git checkout feature/circle-area git stash list--> in my case this command will give below stash@{0}: On feature/rectangle-area: rectangle-area-incomplete stash@{1}: On feature/circle-area: circle-area-incomplete git stash apply "stash@{1}" git add . git commit -m "Completed circle area feature" git push origin feature/circle-area

Finish Rectangle Feature git checkout feature/rectangle-area git stash list--> in my case this command will give below stash@{0}: On feature/rectangle-area: rectangle-area-incomplete stash@{1}: On feature/circle-area: circle-area-incomplete git stash apply "stash@{0}" // "stash@{0}" in your case may be vary git add . git commit -m "Completed rectangle area feature" git push origin feature/rectangle-area

Create Pull Requests PR 1 → feature/circle-area → dev PR 2 → feature/rectangle-area → dev

Merge After Review Did final testing in dev branch Merge PRs after approval → then merge dev into main


<img width="2224" height="980" alt="image" src="https://github.com/user-attachments/assets/76692c69-3e90-4fb7-a274-cc4c0ba0e568" />













