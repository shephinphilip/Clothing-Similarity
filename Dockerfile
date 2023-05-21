FROM python:3.9

WORKDIR /clothing

COPY . /clothing

RUN pip install --no-cache-dir pandas
RUN pip install scikit-learn

EXPOSE 8080

CMD ["python", "similarity_check.py"]
