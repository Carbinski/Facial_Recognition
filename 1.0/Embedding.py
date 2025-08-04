import os
import numpy as np
from PIL import Image
import psycopg2
import torch
from torchvision import transforms
from transformers import CLIPProcessor, CLIPModel

# enter URI below
conn = psycopg2.connect("URI")
cur = conn.cursor()

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

for filename in os.listdir("stored-faces"):
    img = Image.open(os.path.join("stored-faces", filename)).convert("RGB")
    
    # Preprocess the image
    inputs = processor(images=img, return_tensors="pt")
    
    # Generate embeddings
    with torch.no_grad():
        image_features = model.get_image_features(**inputs)
    
    # Normalize and convert to numpy array
    embedding = image_features[0].cpu().numpy()
    
    # Save to PostgreSQL
    cur.execute("INSERT INTO pictures (filename, embedding) VALUES (%s, %s)", (filename, embedding.tolist()))
    print(f"Inserted {filename}")
    print(f"Inserted {filename}")

conn.commit()
conn.close()