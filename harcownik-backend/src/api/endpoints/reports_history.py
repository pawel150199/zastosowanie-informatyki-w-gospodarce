from typing import Any

from fastapi import (APIRouter, Depends, File, Form, HTTPException, Response,
                     UploadFile)
from sqlalchemy.orm import Session
from src import crud, schemas, models
from src.api.helper import (get_current_teamadmin, get_current_user, get_db)

router = APIRouter()


# POST
@router.post("/report/pdf", response_model=schemas.PdfFile)
def create_pdf(
    name: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_teamadmin: models.User = Depends(get_current_teamadmin)
) -> Any:
    file_content = file.file.read()
    pdf = schemas.PdfFileCreate(name=name, user_id=current_teamadmin.id, content=file_content)
    return crud.create_file(db=db, pdf_report=pdf)


# GET
@router.get("/me/reports", response_model=list[schemas.PdfFile])
def read_pdfs_data(db: Session = Depends(get_db), current_teamadmin: models.User = Depends(get_current_user)) -> Any:
    pdfs = crud.get_files_by_user(db, user_id=current_teamadmin.id)
    if pdfs is None or pdfs == []:
        raise HTTPException(status_code=404, detail="Files not found")
    return pdfs


@router.get("/report/amount")
def read_amount_pdf_in_current_month(db: Session = Depends(get_db), _: models.User = Depends(get_current_user)) -> Any:
    number = crud.get_number_in_month(db)
    return {"Number of PDFs in current month": int(number)}



@router.get("/report/{pdf_id}/file")
def read_pdf(pdf_id: int, db: Session = Depends(get_db), _: models.User = Depends(get_current_teamadmin)) -> Any:
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
def delete_pdf(pdf_id: int, db: Session = Depends(get_db), _: models.User = Depends(get_current_teamadmin)) -> Any:
    pdf = crud.get_file(db=db, pdf_id=pdf_id)
    if not pdf:
        raise HTTPException(status_code=404, detail="File not found")
    pdf_del = crud.delete_file(db=db, pdf_id=pdf_id)
    return pdf_del