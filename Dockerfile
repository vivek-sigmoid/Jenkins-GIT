FROM python:latest
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install psutil
ADD pod_usage_info.py .
CMD [ "python", "/pod_usage_info.py" ]