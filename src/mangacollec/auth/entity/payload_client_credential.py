from mangacollec.auth.entity.payload_client_abstract import PayloadClientAbstract


class PayloadClientCredential(PayloadClientAbstract):
    grant_type: str = "client_credentials"
    client_id: str
    client_secret: str
    
    def to_dict(self) -> dict:
        return {
            "grant_type": self.grant_type,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }