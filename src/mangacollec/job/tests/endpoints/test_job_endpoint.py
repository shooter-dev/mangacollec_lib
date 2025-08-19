import pytest
from unittest.mock import Mock, MagicMock
from mangacollec.job.endpoint.job_endpoint import JobEndpoint
from mangacollec.job.entity.job import Job
from mangacollec.job.responses.job_response import JobEndpointResponse
from mangacollec.job.responses.jobs_response import JobsEndpointResponse


class TestJobEndpoint:
    
    def setup_method(self):
        self.mock_client = Mock()
        self.endpoint = JobEndpoint(self.mock_client)

    def test_get_all_jobs_v1(self):
        expected_response = {"jobs": [{"id": "job-1", "title": "Scenarist", "tasks_count": 5}]}
        self.mock_client.get.return_value = expected_response
        
        result = self.endpoint.get_all_jobs()
        
        self.mock_client.get.assert_called_once_with("/v1/jobs")
        assert result == expected_response

    def test_get_job_by_id_v1(self):
        job_id = "job-123"
        expected_response = {"job": {"id": job_id, "title": "Scenarist", "tasks_count": 10}}
        self.mock_client.get.return_value = expected_response
        
        result = self.endpoint.get_job_by_id(job_id)
        
        self.mock_client.get.assert_called_once_with("/v1/jobs/job-123")
        assert result == expected_response

    def test_get_all_jobs_v2(self):
        api_response = {
            "jobs": [
                {"id": "job-1", "title": "Scenarist", "tasks_count": 5},
                {"id": "job-2", "title": "Dessinateur", "tasks_count": 8}
            ]
        }
        self.mock_client.get.return_value = api_response
        
        result = self.endpoint.get_all_jobs_v2()
        
        self.mock_client.get.assert_called_once_with("/v2/jobs")
        assert isinstance(result, JobsEndpointResponse)
        assert len(result.jobs) == 2
        assert result.jobs[0].id == "job-1"
        assert result.jobs[0].title == "Scenarist"
        assert result.jobs[1].id == "job-2"
        assert result.jobs[1].title == "Dessinateur"

    def test_get_job_by_id_v2(self):
        job_id = "job-123"
        api_response = {
            "jobs": [{"id": job_id, "title": "Scenarist", "tasks_count": 10}]
        }
        self.mock_client.get.return_value = api_response
        
        result = self.endpoint.get_job_by_id_v2(job_id)
        
        self.mock_client.get.assert_called_once_with("/v2/jobs/job-123")
        assert isinstance(result, JobEndpointResponse)
        assert len(result.jobs) == 1
        assert result.jobs[0].id == job_id
        assert result.jobs[0].title == "Scenarist"

    def test_get_job_by_id_v2_no_jobs(self):
        job_id = "job-123"
        api_response = {}
        self.mock_client.get.return_value = api_response
        
        result = self.endpoint.get_job_by_id_v2(job_id)
        
        assert isinstance(result, JobEndpointResponse)
        assert len(result.jobs) == 0