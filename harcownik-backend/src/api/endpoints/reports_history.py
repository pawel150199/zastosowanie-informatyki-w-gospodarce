from typing import Any

from fastapi import (APIRouter, Depends, File, Form, HTTPException, Response,
                     UploadFile)
from sqlalchemy.orm import Session
from src import crud, schemas
from src.api.helper import get_db

router = APIRouter()


# POST
@router.post("/report/pdf", response_model=schemas.PdfFile)
def create_pdf(
    name: str = Form(...),
    user_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
) -> Any:
    file_content = file.file.read()
    pdf = schemas.PdfFileCreate(name=name, user_id=user_id, file_content=file_content)
    return crud.create_file(db=db, pdf_report=pdf)


# GET
@router.get("/reports", response_model=list[schemas.PdfFile])
def read_pdfs_data(db: Session = Depends(get_db)) -> Any:
    pdfs = crud.get_files_data(db)
    if pdfs is None or pdfs == []:
        raise HTTPException(status_code=404, detail="Files not found")
    return pdfs


@router.get("/report", response_model=schemas.PdfFile)
def read_pdf_data(pdf_id: int, db: Session = Depends(get_db)) -> Any:
    pdf = crud.get_file_data(db, pdf_id=pdf_id)
    if pdf is None:
        raise HTTPException(status_code=404, detail="File not found")
    return pdf


@router.get("/reports/{user_id}", response_model=list[schemas.PdfFile])
def read_pdfs_data(user_id: int, db: Session = Depends(get_db)) -> Any:
    pdfs = crud.get_files_data_by_user(db, user_id=user_id)
    if pdfs is None or pdfs == []:
        raise HTTPException(status_code=404, detail="Files not found")
    return pdfs


@router.get("/report/{pdf_id}/file")
def read_pdf(pdf_id: int, db: Session = Depends(get_db)) -> Any:
    pdf = crud.get_file(db=db, pdf_id=pdf_id)
    if pdf is None:
        raise HTTPException(status_code=404, detail="File not found")

    if pdf.content is None:
        raise HTTPException(status_code=404, detail="File content not found")

    response = Response(content=pdf.content, media_type="application/pdf")
    response.headers["Content-Disposition"] = f"attachment; filename={pdf.name}"
    return response


# DELETE
@router.delete("/reports/delete/{pdf_id}", response_model=schemas.PdfFile)
def delete_pdf(pdf_id: int, db: Session = Depends(get_db)) -> Any:
    pdf = crud.get_file(db=db, pdf_id=pdf_id)
    if not pdf:
        raise HTTPException(status_code=404, detail="File not found")
    pdf_del = crud.delete_file(db=db, pdf_id=pdf_id)
    return pdf_del
