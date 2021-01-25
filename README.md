# madlib-assessment

First you need to clone this code locally and follow the steps
below.

## First step is to build a docker image.

## How to build docker image and run docker container?

cd madlib-assessment

docker build -t madlib-assessment .

docker run -p 5000:5000 -d madlib-assessment:latest

Visit http://127.0.0.1:5000/madlib to check the API.


## Create a virtual environment

virtualenv -p python3.9 venv-madlib-assessment

source venv-madlib-assessment/bin/activate

pip install -r requirements.txt

## How to run tests?

source venv-madlib-assessment/bin/activate

python test.py
