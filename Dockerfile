# official python3 runtimes on lightweight alpine
FROM python:3.6-alpine

# set working directory and copy contents to container
WORDIR /app
COPY . /app

# install packages from requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# expose port 80 on the container to external connections
EXPOSE 80

# run application when container launches
CMD ["python3", "application.py"]
