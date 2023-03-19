ARG NODE_VERSION=16.16.0-alpine

FROM node:${NODE_VERSION} as base

RUN npm i -g pnpm

# Use an official node runtime as a parent image - Build stage
FROM base as build-image

WORKDIR /app/frontend

COPY package.json pnpm-lock.yaml ./

RUN pnpm install

# Use an official node runtime as a parent image - Runtime
FROM base as runtime

WORKDIR /app/frontend

# copy rest of source code
COPY . .

# copy node_modules from build stage
COPY --from=build-image /app/frontend/node_modules /app/frontend/node_modules

RUN apk add bash

ENV HOST=0.0.0.0
EXPOSE 35730

CMD ["pnpm", "dev"]
