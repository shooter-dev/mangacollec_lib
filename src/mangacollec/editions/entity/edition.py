from pydantic import BaseModel


class Edition(BaseModel):
    id: str
    title: str | None
    series_id: str
    publisher_id: str
    parent_edition_id: str | None
    volumes_count: int
    last_volume_number: int | None
    commercial_stop: bool
    not_finished: bool
    follow_editions_count: int

    def __str__(self):
        return self.title if self.title else self.id

    def __repr__(self):
        return self.id