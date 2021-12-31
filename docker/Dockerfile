FROM python:3.10

WORKDIR /var/www/html

RUN python -m pip install --upgrade pip
RUN pip install fastapi uvicorn
RUN pip install sqlalchemy
RUN pip install wheel
RUN pip install psycopg2
RUN pip install psycopg2-binary

RUN apt-get -y update && \                                                                                           
    apt-get install -y --no-install-recommends \                                                                     
    build-essential \                                                                                                
    openssl libssl-dev \                                                                                             
    && apt-get clean \                                                                                               
    && rm -rf /var/lib/apt/lists/*     