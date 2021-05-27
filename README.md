Create an Environment 

```bash
conda create -n wineq python=3.7 -y
```

Activate Environment
```bash
conda activate wineq
```


Install the requirements
```bash
pip install -r requirements.txt
```

Download the data from 

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

```bash
git init
```
```bash
dvc init 
```
For Data to be tracked
```bash
dvc add data_given/winequality.csv
```
For git to track 
```bash
git add .
```
```bash
git commit -m "first commit"
```

One-liner updates  for readme

```bash
git add . && git commit -m "update Readme.md"
```
```bash
git remote add origin https://github.com/<USER_ID>/<REPO_NAME>.git
git branch -M main
git push origin main
```

Tox command -
```bash
tox
```
For Updation -
```bash
tox -r 
```
Pytest command
```bash
pytest -v
```

Setup commands -
```bash
pip install -e . 
```

build your own package commands- 
```bash
python setup.py sdist bdist_wheel
```
