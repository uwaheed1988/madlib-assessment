# madlib-assessment
madlib Assessment

## Create a virtual environment

virtualenv -p python3.9 venv-madlib-assessment

source venv-madlib-assessment/bin/activate

pip install -r requirements.txt

## How to run tests?

source venv-madlib-assessment/bin/activate

python test.py

## How to build docker image and run docker container?

cd madlib-assessment

docker build -t madlib-assessment .
docker run -p 5001:5000 -d madlib-assessment:latest

Visit http://127.0.0.1:5001/madlib to check the API.
