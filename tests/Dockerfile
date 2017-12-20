FROM python:3.6

RUN pip install pytest \
                pyYAML

COPY . /tests

CMD ["pytest", "tests"]