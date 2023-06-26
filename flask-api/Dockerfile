FROM python:3.6-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 4000 available to the world outside this container
EXPOSE 4000

# Provide defaults for an executing container
CMD [ "flask","run","--host=0.0.0.0","--port=4000" ]
