from fastapi import FastAPI
from core.config import settings
from db.session import engine
# from db.base_class import Base
from apis.base import api_router
from apps.base import app_router
from fastapi.staticfiles import StaticFiles

def include_router(app): # include routes within the app
    app.include_router(api_router)
    app.include_router(app_router)

def configure_static_files(app):
    app.mount("/static", StaticFiles(directory="static"),name="static")
# def create_tables():
#     Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)
    # create_tables() experiment to create tables without using alembic
    include_router(app) # include the routes  
    configure_static_files(app)
    return app

app = start_application()

# @app.get("/")
# def hello():
#     return {"msg":"Hello FastAPI"}