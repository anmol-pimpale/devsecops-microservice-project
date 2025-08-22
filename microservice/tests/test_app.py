import io
import pytest
from PIL import Image
from microservice.src.app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def create_test_image(format="PNG"):
    """Helper to create an in-memory image file."""
    img = Image.new("RGB", (50, 50), color="red")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format=format)
    img_bytes.seek(0)
    return img_bytes

def test_homepage_loads(client):
    """GET / should return 200 and render HTML"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"<html" in response.data.lower()

def test_upload_valid_image(client):
    """POST / with a valid PNG should return processed image"""
    img_bytes = create_test_image("PNG")
    data = {
        "file": (img_bytes, "test.png")
    }
    response = client.post("/", data=data, content_type="multipart/form-data")
    assert response.status_code == 200
    assert response.mimetype == "image/png"

def test_upload_without_file(client):
    """POST / without file should redirect with flash"""
    response = client.post("/", data={}, content_type="multipart/form-data", follow_redirects=True)
    assert response.status_code == 200
    assert b"No file part" in response.data or b"No file selected" in response.data

def test_upload_invalid_extension(client):
    """POST / with invalid file type should redirect with flash"""
    fake_file = io.BytesIO(b"hello world")
    data = {
        "file": (fake_file, "test.txt")
    }
    response = client.post("/", data=data, content_type="multipart/form-data", follow_redirects=True)
    assert response.status_code == 200
    assert b"Invalid file format" in response.data
