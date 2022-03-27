FROM python:3.8
RUN mkdir /app 
COPY /app /app
COPY pyproject.toml /app 
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0"]