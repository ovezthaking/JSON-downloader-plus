FROM python

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN python -m pip install --upgrade pip
RUN pip install pytest requests

COPY main.py .
COPY tests/ ./tests/

CMD ["python", "main.py"]