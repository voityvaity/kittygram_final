#dockerfile frontend
FROM node:18
WORKDIR /app

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm ci

COPY . .
RUN npm run build
#RUN npm install --global http-server

#CMD ["npx", "-y", "http-server", "-p", "8000", "/app/build"]

# Просто копируем файлы, без запуска сервера
CMD ["cp", "-r", "/app/build/.", "/frontend_static/"]
