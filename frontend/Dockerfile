# Use official Node.js image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Build the Vue app
RUN npm run build

# Serve the app
CMD ["npm", "run", "dev", "--", "--host"]
