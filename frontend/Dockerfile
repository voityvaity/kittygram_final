#dockerfile frontend
FROM node:22-alpine
WORKDIR /app

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm ci

COPY . .
RUN npm run build
#RUN npm install --global http-server

CMD ["cp", "-r", "/app/dist/.", "/frontend_static/"]
