FROM python:3
RUN /usr/local/bin/python -m pip install --upgrade pip
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD pod_usage_info.py .
CMD [ "python3", "./pod_usage_info.py" ]
