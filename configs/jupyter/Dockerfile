FROM jupyter/base-notebook:x86_64-python-3.11.6

USER root

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y openjdk-11-jdk-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# To find the java directory: readlink -f $(which java)
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

RUN pip install pyspark SQLAlchemy pandas keras pymysql cryptography scikit-learn numpy matplotlib tensorflow
