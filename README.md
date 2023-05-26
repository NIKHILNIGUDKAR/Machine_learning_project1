# Start Machine_learning_project1
 ## Software and Account Requirements
 1. [Github Account](https://github.com)
 2. [Heroku Account](https://dashboard.heroku.com/login)
 3. [VS Code IDE](https://code.visualstudio.com/download)
 4. [GIT Cli](https://git-scm.com/download)


 Creating Conda environment
 ```
 conda create -p venv python=3.7 -y
 ```
Active virtual environment
```
conda activate venv
```
OR
```
conda activate venv/
```

Command To install flask
```
pip install -r requirements.txt
```

To add files to git 
```
git add .
```
>To ignore file/folder from git we can write name of file/folder in .gitignore file

To check status
```
git status
```
To check all versions maintained by git
```
git log
```
To create version commit all changes by git
```
git commit -m "some message"
```

To send versions/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tag_name> .
```
>Note: Image name for dcker must be lowercase

TO list docker image
```
docker images
```

To run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```

To check running contaniers in docker
```
docker ps
```

To stop docker container
```
docker stop container_id
```

```
python setup.py install
```