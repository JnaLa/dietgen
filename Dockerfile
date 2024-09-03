# Use an official Python runtime as a parent image
FROM python:3.8
#provide code for the image to test a app
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Make port 5000 available to the world outside this container
EXPOSE 5000
# Define environment variable

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
