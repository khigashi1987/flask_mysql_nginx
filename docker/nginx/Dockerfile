FROM nginx:1.17

COPY ./data/conf/nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;","-c","/etc/nginx/nginx.conf"]
