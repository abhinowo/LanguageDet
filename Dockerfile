FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY ./requirements.txt LANGUAGEDET/requirements.txt

RUN pip install --no-cache-dir --upgrade -r LANGUAGEDET/requirements.txt

COPY ./notebooks /notebooks/app
