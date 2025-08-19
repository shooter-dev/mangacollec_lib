from mangacollec.core.exception.exception import MangaCollecAPIError, NotFoundError


class JobNotFoundError(NotFoundError):
    """Exception levée quand un job n'est pas trouvé."""
    
    def __init__(self, job_id: str):
        super().__init__(f"Job with ID '{job_id}' not found")
        self.job_id = job_id


class JobAPIError(MangaCollecAPIError):
    """Exception levée lors d'erreurs API liées aux jobs."""
    pass