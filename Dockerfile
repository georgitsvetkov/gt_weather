# set python base image
FROM python:3

# setting working directory
WORKDIR /usr/src/app

# copy the script to workdir
COPY main.py ./

# install required modules
RUN pip install requests; pip install schedule

# set entrypoint to start the script and force the stdout and stderr streams to be unbuffered -u, as it was not showing outputs without
ENTRYPOINT [ "python", "-u", "./main.py" ]
