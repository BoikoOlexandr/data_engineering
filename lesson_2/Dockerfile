# Use an official Python runtime as a parent image
FROM python:3.12-rc-slim

# Set the working directory in the container
RUN mkdir /src

WORKDIR /src
COPY ./requirements.txt ./requirements.txt

# Install Jupyter Notebook
RUN pip install --upgrade pip && pip install -r requirements.txt

# Make port 8888 available to the world outside this container
EXPOSE 8888

# Run Jupyter Notebook when the container launches
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
