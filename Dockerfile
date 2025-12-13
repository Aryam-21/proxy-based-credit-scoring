# 1️⃣ Base image
FROM python:3.10-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy dependency file first
COPY requirements.txt .

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy the rest of the project files
COPY . .

# 6️⃣ Optional: expose ports for API or Jupyter
EXPOSE 5000 8888

# 7️⃣ Default command (can be overridden by docker-compose)
CMD ["python", "src/api/main.py"]


