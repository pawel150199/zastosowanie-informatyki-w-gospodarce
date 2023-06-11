# stage 1
FROM node:16-alpine as builder

# workdir
WORKDIR /app

# copy packages
COPY ./package.json /app/

# install node modules
RUN npm install

# copy all context to container
COPY . /app/

ARG FRONTEND_ENV=production

# build react app
RUN npm run build

# stage 2
FROM nginx:1.15 as server

# workdir
WORKDIR /usr/share/nginx/html

# copy context from builder to server
COPY --from=builder /app/build/ .
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# start nginx server
ENTRYPOINT ["nginx", "-g", "daemon off;"]
