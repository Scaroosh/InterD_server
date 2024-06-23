WORKDIR /workdir
COPY requirements.txt requirements.txt
RUN yes | conda install -c conda-forge ta-lib
RUN pip3 install -r requirements.txt
ENV PYTHONPATH=${PYTHONPATH}:/workdir/appdir
COPY . .
EXPOSE 8080
ENTRYPOINT FLASK_APP=/server.py flask run --host=0.0.0.0