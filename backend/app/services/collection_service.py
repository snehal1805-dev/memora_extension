from sqlalchemy.orm import Session

from app.models.collection_model import Collection
from app.models.memory_model import Memory


def create_collection(
    db: Session,
    user_id: int,
    name: str
):

    collection = Collection(
        user_id=user_id,
        name=name
    )

    db.add(collection)
    db.commit()
    db.refresh(collection)

    return collection


def get_all_collections(
    db: Session,
    user_id: int
):

    return (
        db.query(Collection)
        .filter(Collection.user_id == user_id)
        .order_by(Collection.created_at.desc())
        .all()
    )


def get_collection_by_id(
    db: Session,
    collection_id: int,
    user_id: int
):

    return (
        db.query(Collection)
        .filter(
            Collection.id == collection_id,
            Collection.user_id == user_id
        )
        .first()
    )


def rename_collection(
    db: Session,
    collection: Collection,
    name: str
):

    collection.name = name

    db.commit()
    db.refresh(collection)

    return collection


def delete_collection(
    db: Session,
    collection: Collection
):

    db.delete(collection)
    db.commit()


def add_memory_to_collection(
    db: Session,
    memory: Memory,
    collection: Collection
):

    memory.collection_id = collection.id

    db.commit()
    db.refresh(memory)

    return memory


def remove_memory_from_collection(
    db: Session,
    memory: Memory
):

    memory.collection_id = None

    db.commit()
    db.refresh(memory)

    return memory


def get_collection_memories(
    db: Session,
    collection_id: int,
    user_id: int
):

    collection = get_collection_by_id(
        db,
        collection_id,
        user_id
    )

    if not collection:
        return None

    return collection.memories