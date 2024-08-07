FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "./lun.ua/start_crawler.py" ]
#CMD jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
