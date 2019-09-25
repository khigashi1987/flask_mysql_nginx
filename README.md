# flask_mysql_nginx

## Run
```
docker-compose up -d
```

## Files
```
.
├── data
│   ├── app
│   │   ├── requirements.txt
│   │   ├── src
│   │   │   ├── flask_sample.py
│   │   │   ├── static
│   │   │   │   ├── css
│   │   │   │   ├── fonts
│   │   │   │   └── js
│   │   │   │       ├── bootstrap.js
│   │   │   │       ├── bootstrap.min.js
│   │   │   │       └── npm.js
│   │   │   └── templates
│   │   │       ├── index.html
│   │   │       └── layout.html
│   │   └── uwsgi.ini
│   ├── conf
│   │   └── nginx.conf
│   └── mysql
│       ├── initdb.d
│       │   └── create_table.sql
│       └── my.cnf
├── docker
│   ├── app
│   │   └── Dockerfile
│   ├── mysql
│   │   └── Dockerfile
│   └── nginx
│       └── Dockerfile
└── docker-compose.yml
```
