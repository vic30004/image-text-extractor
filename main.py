from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import pytesseract
import io

app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/extract-text")
async def extract_text_from_image(image: UploadFile = File(...)):
    allowed_content_types = ["image/jpeg", "image/png", "image/jpg", "image/gif", "image/bmp"]

    if image.content_type not in allowed_content_types:
        raise HTTPException(status_code=400, detail="Invalid file type. Please make sure the file is one of the following. jpeg, png, jpg, gif, bmp")
    try:
        contents = await image.read()
        img = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(img)
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
