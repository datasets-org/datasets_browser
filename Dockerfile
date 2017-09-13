FROM python

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD python -m twisted web -p "tcp:5000" --wsgi web.app
