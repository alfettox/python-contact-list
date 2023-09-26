from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Configure CORS settings
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app = FastAPI()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define CORS settings
origins = ["*"]  # Replace "*" with your allowed origins as needed

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods if needed
    allow_headers=["Content-Type"],
)

class Contact(BaseModel):
    name: str
    numbers: List[str]

def load_contacts():
    try:
        with open("./data/contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open("./data/contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

@app.post("/add_contact")
async def add_contact(contact: Contact):
    contacts = load_contacts()
    contacts.append(contact.dict())
    save_contacts(contacts)
    return {"message": "Contact added"}

@app.delete("/remove_contact")
async def remove_contact(name: str = Query(..., title="Contact to be removed")):
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c["name"] != name]
    if len(new_contacts) == len(contacts):
        raise HTTPException(status_code=404, detail="Not found")
    save_contacts(new_contacts)
    return {"message": "Contact removed"}

@app.get("/") 
async def view_contacts():
    return load_contacts()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/test")
async def test_endpoint():
    return {"message": "This is a test response from FastAPI"}

