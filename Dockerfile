FROM python:3.9.9-alpine3.14
RUN /usr/local/bin/python -m pip install --upgrade pip
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD pod_usage_info.py .
ADD config.yaml
CMD [ "sleep 1000" ]
# CMD [ "python3", "./pod_usage_info.py" ]