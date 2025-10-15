from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.auth.routes import router as auth_router
from app.cases.routes import router as cases_router
from app.analytics.routes import router as analytics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Esolve DCOE Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(cases_router, prefix="/cases", tags=["Cases"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])

@app.get("/")
def root():
    return {"message": "Esolve DCOE API is running!"}
