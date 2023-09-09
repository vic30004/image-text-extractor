from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import pytesseract
import io

app = FastAPI()

origins = [
    "http://localhost:3000",
    "chrome-extension://*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract-text")
async def extract_text_from_image(image: UploadFile = File(...)):
    contents = await image.read()
    img = Image.open(io.BytesIO(contents))
    text = pytesseract.image_to_string(img)
    return {"text": text}