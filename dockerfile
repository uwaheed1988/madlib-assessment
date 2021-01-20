FROM python:3.9.0
COPY . /madlib
WORKDIR /madlib
RUN pip3 install -r requirements.txt 
EXPOSE 5001 
ENTRYPOINT [ "python3.9" ] 
CMD [ "api.py" ] 