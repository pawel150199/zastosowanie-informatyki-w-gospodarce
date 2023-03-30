# use node alpine version
FROM node:16-alpine

LABEL MAINTAINER=Pawel

# environmental variable
ENV NODE_ENV development
ENV NPM_CONFIG_LOGLEVEL warn

# all is in /frontend dir in docker container
WORKDIR /frontend

# copy all context to container
COPY . .

# use one run command to minimalize container size
RUN npm install

# start react app
CMD ["npm", "start"]


######################DEVELOPMENT#VERSION########################
## stage 1
#FROM node:16-alpine as builder
#
## workdir
#WORKDIR /app
#
## copy pacckages
#COPY package.json .
#COPY package-lock.json .
#
## install node modules
#RUN npm install
#
## copy all context to container
#COPY . .
#
## build react app
#RUN npm build
#
## stage 2
#FROM nginx:1.19.0 as server
#
## workdir
#WORKDIR /usr/share/nginx/html
#
## copy context from builder to  server
#COPY --from=builder /app/build .
#
## start react app
#ENTRYPOINT ["nginx", "-g", "daemon off;"]
