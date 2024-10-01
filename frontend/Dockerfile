FROM alpine:latest

RUN apk add --update nginx

# Copy nginx.conf in /etc/nginx/http.d
COPY ./conf/nginx.conf /etc/nginx/http.d


EXPOSE 8080

# Start NGINX in the foreground
ENTRYPOINT ["nginx", "-g", "daemon off;"]
