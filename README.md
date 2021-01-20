# madlib-assessment
madlib Assessment

## Create a virtual environment

virtualenv -p python3.9 venv-madlib-assessment

source venv-madlib-assessment/bin/activate

pip install -r requirements.txt

## How to run tests?

Make sure that docker container is running. Activate your virtual environment.

source venv-madlib-assessment/bin/activate

python test.py

## How to build docker image and run docker container?

cd madlib-assessment

docker build -t madlib-assessment .
