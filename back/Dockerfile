FROM continuumio/miniconda3:23.3.1-0
ENV PYTHONUNBUFFERED 1
WORKDIR /workdir
COPY requirements.txt requirements.txt
RUN yes | conda install -c conda-forge ta-lib
RUN pip3 install -r requirements.txt
ENV PYTHONPATH= ${PYTHONPATH}:/workdir/appdir
EXPOSE 8000
CMD [“gunicorn.sh”]