# Use the official Python base image
FROM python:3.12

# Copy the application code to the container
COPY app.py /app.py
COPY config.py /config.py
COPY scrapper.py /scrapper.py
COPY update_README.py /update_README.py
COPY requirements.txt /requirements.txt
COPY Driver/chromedriver.exe /Driver/chromedriver.exe

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Chromium and dependencies
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium

# Set environment variable to use the ChromeDriver from the Driver directory
ENV PATH="/Driver:${PATH}"
RUN chmod +x /Driver/chromedriver.exe

# Run the application
ENTRYPOINT ["python", "/app.py"]
