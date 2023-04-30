FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server pnpm

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN pnpm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# set value to env variable
ENV VITE_API_URL=http://127.0.0.1:3000

# build app for production with minification
RUN pnpm build

EXPOSE 8080
CMD [ "http-server", "dist" ]