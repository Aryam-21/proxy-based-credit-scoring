FROM python:3.12-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy dependency file first
COPY requirements.txt .

# 4️⃣ Install dependencies
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# 5️⃣ Copy the rest of the project files
COPY . .

# 6️⃣ Optional: expose ports for API or Jupyter
EXPOSE 8000

# 7️⃣ Default command (can be overridden by docker-compose)

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]


