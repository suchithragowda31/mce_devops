# Stage 1: Build the React app
FROM node:20 AS build

WORKDIR /app
COPY client/package.json client/package-lock.json ./
RUN npm install
COPY client ./
RUN npm run build

# Stage 2: Serve the built app with Node.js
FROM node:14

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY server.js ./
COPY --from=build /app/build ./client/build

EXPOSE 3000

CMD ["node", "server.js"]
