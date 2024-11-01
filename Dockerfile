# Use an official Python runtime as a base image
FROM python:3.10-slim

#Set the working directory in the container
WORKDIR /app

#Copy the current directory contents into the container at /app
COPY . .

#Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Make port 5000 available to the world outside this container
EXPOSE 5000

#Define environment variable
ENV FLASK_ENV=production

#Run app.py when the container launches
CMD ["python", "app.py"]

####################################################################################

# FROM python:3.10-slim

# # Set working directory
# WORKDIR /app

# # Copy requirements
# COPY requirements.txt .

# # Install dependencies
# RUN pip install -r requirements.txt

# # Copy application code
# COPY . .

# # Expose port
# EXPOSE 5000

# # Run command
# CMD ["python", "app.py"]
