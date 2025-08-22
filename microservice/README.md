🖼️ Background Remover Microservice

This is a Flask-based microservice that removes image backgrounds using the rembg
 library.
It is part of the larger DevSecOps Microservice Project.

📌 Features

Upload an image (.png, .jpg, .jpeg) via a web form

Automatically remove the background

Download the processed image in PNG format

Input validation (file type, size limit: 10 MB)

Error handling and logging

🚀 Run Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the service
python src/app.py


App will be available at:
👉 http://localhost:5100

🐳 Run with Docker
1️⃣ Build the image
docker build -t background-remover-app .

2️⃣ Run the container
docker run -p 5100:5100 background-remover-app

🧪 Testing

Unit tests are available in tests/test_app.py.

pytest -v
