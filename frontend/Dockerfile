# Używamy oficjalnego obrazu Node.js w wersji 14
FROM node:14

# Ustawiamy katalog roboczy na /app
WORKDIR /app

# Kopiujemy pliki package.json i package-lock.json do kontenera
COPY ./package*.json ./

# Instalujemy zależności npm
RUN npm install
RUN npm install @vue/cli@3.7.0 -g

# Kopiujemy resztę plików do katalogu /app w kontenerze
COPY . /app

# Expose port 8080, na którym będzie działać serwer deweloperski Vue.js
EXPOSE 8080

# Komenda do uruchomienia serwera deweloperskiego
CMD ["npm", "run", "serve"]


# ##################

# FROM node:lts-alpine

# # install simple http server for serving static content
# RUN npm install -g http-server

# # make the 'app' folder the current working directory
# WORKDIR /app

# # copy both 'package.json' and 'package-lock.json' (if available)
# COPY package*.json ./

# # install project dependencies
# RUN npm install

# # copy project files and folders to the current working directory (i.e. 'app' folder)
# COPY . .

# # build app for production with minification
# RUN npm run build

# EXPOSE 8080
# CMD [ "http-server", "dist" ]
