# nlp_sentiment_model_post
Train a basic NLP sentiment model & serve predictions using Tensorflow Serving

## Table of Contents

1. [Usage](#Usage)
1. [Requirements](#requirements)
1. [Development](#development)
    1. [Installing Dependencies](#installing-dependencies)
    1. [Download & Saving a Model](#download--save-a-trained-tensorflow-model)
    1. [Serving in Development](#serving-in-development)
    1. [Testing](#testing)

## Usage

>Serve a custom trained NLP sentiment model using FastAPI & Tensorflow Serving

## Requirements

- Python 3.8
- Poetry 1.1
- Docker

## Development

### Installing Dependencies

From within the root directory:

```
poetry install
```

### Download & Save a Trained Tensorflow Model

Before serving in development using docker compose, you must follow the setup steps documented here:

[Downloading & Saving a Trained Tensorflow Model README](./saved_models/README.md)

### Serving in Development

Included a minimal example from fastapi to get started with a production server.

To rebuild the api run
```
docker-compose build
```

To serve the api locally run
```
docker-compose up api
```

To serve the full stack locally run
```
docker-compose up
```

Once that runs, you can use the api by going to the following endpoints:
1. Main Api: `http://localhost:8000/`
1. Api Docs (Auto Generated from FastAPI): `http://localhost:8000/docs`
1. Tensorflow Serving: `http://localhost:8501/v1/models/sentiment_model/metadata`
1. Main Api endpoint returning model inference: `http://localhost:8000/text/`

## Testing

From within the root directory:
```
poetry run pytest tests
```
