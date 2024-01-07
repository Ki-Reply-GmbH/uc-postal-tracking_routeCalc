from fastapi import FastAPI, Depends, HTTPException
from . import schemas, models
from sqlalchemy.orm import Session
from .dependencies import get_db
from .route.calculate import calculate_route

app = FastAPI()


@app.get("/status")
def read_status():
    return {"status": "Service is up and running"}


@app.post("/packages/{package_id}/calculate-route", response_model=schemas.Route)
def calculate_package_route(package_id: str, db: Session = Depends(get_db)):
    db_package = (
        db.query(models.Package).filter(models.Package.id == package_id).first()
    )
    if db_package is None:
        raise HTTPException(status_code=404, detail="Package not found")

    route_details = calculate_route(db_package.current_location, db_package.destination)
    # Save route details to the database and return them
    # ...
