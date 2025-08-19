from pydantic import BaseModel


class Task(BaseModel):
    """
    Entité représentant une tâche associée à une série (relation auteur-série-métier).
    """
    id: str
    job_id: str
    series_id: str
    author_id: str

    def __repr__(self):
        return f"Task(id={self.id}, job_id={self.job_id}, author_id={self.author_id})"