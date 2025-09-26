# Use official Node.js LTS on Alpine for small image
FROM node:20-alpine

# Create app directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --omit=dev

# Bundle app source
COPY src ./src

# Expose port
EXPOSE 3000
ENV NODE_ENV=production

# Start the app
CMD ["node", "src/server.js"]
