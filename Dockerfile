FROM python:3.6

ADD requirements.txt /app/
WORKDIR /app
RUN pip install --upgrade pip && pip install gunicorn==19.9.0
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 8082

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8082", "api.app:create_app('settings')"]
