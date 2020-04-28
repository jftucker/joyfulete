# Pull base image
FROM node:10

# Set environment variables

# Set work directory
WORKDIR /app/

# Install dependencies
COPY package.json package-lock.json /app/
RUN npm install
RUN npm install pm2 -g

# Copy project
COPY . /app/

EXPOSE 3000

CMD ["pm2-runtime", "ecosystem.config.js"]