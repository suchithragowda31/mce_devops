# Stage 1: Build the React app
FROM node:14 AS build

WORKDIR /app
# COPY client/package.json client/package-lock.json ./client/
COPY client ./client/
WORKDIR /app/client
RUN npm install
RUN npm run build
# RUN cd client && npm install
# RUN cd client && npm run build

# Stage 2: Serve the built app with Node.js
# FROM node:14

WORKDIR /app
# COPY package.json package-lock.json ./
COPY server.js ./
COPY package.json ./
RUN npm install

# COPY --from=build /app/client/build ./client/build

EXPOSE 3000

CMD ["node", "server.js"]
