# Pull base image
From ubuntu:18.04
LABEL maintainer="rajeevshirali@gmail.com"

# Install dependencies
RUN apt-get update -y
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -y vim
RUN python3.6 -m pip install pip --upgrade
RUN pip3 install pylint
RUN pip3 install requests
RUN pip3 install pytest pytest-cache

#install dos2unix
RUN apt-get update && \
    apt-get install dos2unix && \
    apt-get clean

# Create working directory
RUN mkdir /testsuite

# Copy project
COPY comments_categories_api  /testsuite/comments_categories_api/
COPY comments_posts_api  /testsuite/comments_posts_api/
COPY service_layer /testsuite/service_layer/
RUN chmod -R a+rwX testsuite/
# Set working directory

WORKDIR /testsuite
# Set Python version
RUN echo alias python='/usr/bin/python3' >> ~/.bashrc
# RUN echo cd testsuite/ >> ~/.bashrc

COPY ./docker-entrypoint.sh /testsuite/docker-entrypoint.sh
RUN dos2unix /testsuite/docker-entrypoint.sh && apt-get --purge remove -y dos2unix
# Define ENTRYPOINT
RUN ["chmod", "+x", "/testsuite/docker-entrypoint.sh"]
ENTRYPOINT ["sh", "docker-entrypoint.sh"] 
