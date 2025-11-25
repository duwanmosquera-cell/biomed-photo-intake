from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Biomed Photo Intake API is running"}

# from app.database import Base, engine
# from app.routes import router
# Base.metadata.create_all(bind=engine)
# app.include_router(router)
