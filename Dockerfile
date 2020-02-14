FROM python:3.7
ENV WORKDIR /usr/src/app/
ENV PYTHONUNBUFFERED 1
RUN mkdir ${WORKDIR}
WORKDIR ${WORKDIR}
COPY ./requirements.txt ${WORKDIR}
RUN pip install -r requirements.txt
COPY . ${WORKDIR}