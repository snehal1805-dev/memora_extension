from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.user_model import User
from app.models.memory_model import Memory

from app.schemas.collection_schema import (
    CollectionCreate,
    CollectionUpdate,
    CollectionResponse
)

from app.schemas.memory_schema import MemoryResponse

from app.services.collection_service import (
    create_collection,
    get_all_collections,
    get_collection_by_id,
    rename_collection,
    delete_collection,
    add_memory_to_collection,
    remove_memory_from_collection,
    get_collection_memories
)

from app.utils.dependencies import current_user


router = APIRouter(
    prefix="/collections",
    tags=["Collections"]
)


@router.post(
    "/",
    response_model=CollectionResponse
)
def create_collection_api(
    request: CollectionCreate,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    return create_collection(
        db=db,
        user_id=user.id,
        name=request.name
    )


@router.get(
    "/",
    response_model=list[CollectionResponse]
)
def all_collections(
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    return get_all_collections(
        db,
        user.id
    )


@router.patch(
    "/{collection_id}",
    response_model=CollectionResponse
)
def rename_collection_api(
    collection_id: int,
    request: CollectionUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    collection = get_collection_by_id(
        db,
        collection_id,
        user.id
    )

    if not collection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Collection not found."
        )

    return rename_collection(
        db,
        collection,
        request.name
    )


@router.delete(
    "/{collection_id}"
)
def delete_collection_api(
    collection_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    collection = get_collection_by_id(
        db,
        collection_id,
        user.id
    )

    if not collection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Collection not found."
        )

    delete_collection(
        db,
        collection
    )

    return {
        "message": "Collection deleted successfully."
    }


@router.patch(
    "/{collection_id}/add/{memory_id}"
)
def add_memory_api(
    collection_id: int,
    memory_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    collection = get_collection_by_id(
        db,
        collection_id,
        user.id
    )

    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found."
        )

    memory = (
        db.query(Memory)
        .filter(
            Memory.id == memory_id,
            Memory.user_id == user.id
        )
        .first()
    )

    if not memory:
        raise HTTPException(
            status_code=404,
            detail="Memory not found."
        )

    add_memory_to_collection(
        db,
        memory,
        collection
    )

    return {
        "message": "Memory added successfully."
    }


@router.patch(
    "/remove/{memory_id}"
)
def remove_memory_api(
    memory_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    memory = (
        db.query(Memory)
        .filter(
            Memory.id == memory_id,
            Memory.user_id == user.id
        )
        .first()
    )

    if not memory:
        raise HTTPException(
            status_code=404,
            detail="Memory not found."
        )

    remove_memory_from_collection(
        db,
        memory
    )

    return {
        "message": "Memory removed successfully."
    }


@router.get(
    "/{collection_id}/memories",
    response_model=list[MemoryResponse]
)
def collection_memories_api(
    collection_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    memories = get_collection_memories(
        db,
        collection_id,
        user.id
    )

    if memories is None:
        raise HTTPException(
            status_code=404,
            detail="Collection not found."
        )

    return memories