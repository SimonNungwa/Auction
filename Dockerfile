# Use a Node.js base image for Tailwind and Python for Flask
FROM node:18 AS builder

# Set working directory
WORKDIR /app

# Copy package.json and install Node.js dependencies
COPY package.json ./
RUN npm install

# Copy Tailwind config and CSS source
COPY tailwind.config.js ./
COPY app/static/css/src ./app/static/css/src

# Build Tailwind CSS
RUN npm run build

# Final stage: Python/Flask environment
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the built CSS from the builder stage
COPY --from=builder /app/app/static/css/output.css ./app/static/css/output.css

# Copy the rest of the application
COPY . .

# Set environment variables
ENV FLASK_APP=auction/__main__.py
ENV FLASK_ENV=development

# Expose port 5000
EXPOSE 5000

# Command to run Flask
CMD ["flask", "run", "--host=0.0.0.0"]