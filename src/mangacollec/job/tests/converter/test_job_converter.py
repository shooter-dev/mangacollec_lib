import pytest
from mangacollec.job.converter.job_converter import JobConverter
from mangacollec.job.entity.job import Job


class TestJobConverter:
    
    def setup_method(self):
        self.converter = JobConverter()
        self.sample_job = Job(
            id="job-123",
            title="Scenarist",
            tasks_count=42
        )
        self.sample_data = {
            "id": "job-123",
            "title": "Scenarist",
            "tasks_count": 42
        }

    def test_serialize(self):
        result = self.converter.serialize(self.sample_job)
        
        assert result == self.sample_data
        assert isinstance(result, dict)

    def test_deserialize(self):
        result = self.converter.deserialize(self.sample_data)
        
        assert isinstance(result, Job)
        assert result.id == "job-123"
        assert result.title == "Scenarist"
        assert result.tasks_count == 42

    def test_serialize_deserialize_roundtrip(self):
        serialized = self.converter.serialize(self.sample_job)
        deserialized = self.converter.deserialize(serialized)
        
        assert deserialized.id == self.sample_job.id
        assert deserialized.title == self.sample_job.title
        assert deserialized.tasks_count == self.sample_job.tasks_count