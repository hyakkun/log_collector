ARG python_env="python:3.10-slim"

FROM ${python_env} as builder

RUN apt-get update && apt-get install -y build-essential
RUN pip install -U pip poetry

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN poetry install
RUN poetry build

FROM ${python_env}
ARG app_version="0.1.0"

WORKDIR /root/
COPY --from=builder /app/dist/server-${app_version}-py3-none-any.whl .
RUN pip install server-${app_version}-py3-none-any.whl

EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "server.main:app"]