from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.user_model import User

from app.schemas.memory_schema import (
    MemoryCreate,
    MemoryUpdate,
    MemoryResponse
)

from app.schemas.search_schema import SearchRequest

from app.utils.dependencies import current_user

from app.services.memory_service import (
    save_memory,
    get_all_memories,
    get_memory_by_id,
    delete_memory,
    toggle_favorite,
    get_favorite_memories,
    update_memory
)

from app.services.ai_service import semantic_search

router = APIRouter(
    prefix="/memory",
    tags=["Memory"]
)


@router.post(
    "/save",
    response_model=MemoryResponse
)
def save_page(
    request: MemoryCreate,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    return save_memory(
        db=db,
        user_id=user.id,
        title=request.title,
        url=request.url,
        favicon=request.favicon,
        raw_content=request.raw_content
    )


@router.post("/search")
def search_memories(
    request: SearchRequest,
    user: User = Depends(current_user)
):

    results = semantic_search(request.query)

    response = []

    for i in range(len(results["ids"][0])):
        response.append(
            {
                "memory_id": results["ids"][0][i],
                "title": results["metadatas"][0][i]["title"],
                "content": results["documents"][0][i],
                "distance": results["distances"][0][i],
            }
        )

    return response


@router.get(
    "/all",
    response_model=list[MemoryResponse]
)
def all_memories(
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    return get_all_memories(
        db,
        user.id
    )


@router.get(
    "/favorites",
    response_model=list[MemoryResponse]
)
def favorite_memories(
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    return get_favorite_memories(
        db,
        user.id
    )


@router.get(
    "/{memory_id}",
    response_model=MemoryResponse
)
def one_memory(
    memory_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    memory = get_memory_by_id(
        db,
        user.id,
        memory_id
    )

    if not memory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Memory not found."
        )

    return memory


@router.patch(
    "/favorite/{memory_id}",
    response_model=MemoryResponse
)
def favorite_memory(
    memory_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    memory = get_memory_by_id(
        db,
        user.id,
        memory_id
    )

    if not memory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Memory not found."
        )

    return toggle_favorite(
        db,
        memory
    )


@router.patch(
    "/update/{memory_id}",
    response_model=MemoryResponse
)
def update_memory_api(
    memory_id: int,
    request: MemoryUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    memory = get_memory_by_id(
        db,
        user.id,
        memory_id
    )

    if not memory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Memory not found."
        )

    return update_memory(
        db,
        memory,
        tags=request.tags
    )


@router.delete(
    "/delete/{memory_id}"
)
def remove_memory(
    memory_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):

    memory = get_memory_by_id(
        db,
        user.id,
        memory_id
    )

    if not memory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Memory not found."
        )

    delete_memory(
        db,
        memory
    )

    return {
        "message": "Memory deleted successfully."
    }