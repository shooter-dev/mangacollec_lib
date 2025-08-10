from mangacollec.auth.entity.payload_client_abstract import PayloadClientAbstract


class PayloadClientPassword(PayloadClientAbstract):
    grant_type: str = "password"
    username: str
    password: str
    client_id: str
    client_secret: str
    
    def to_dict(self) -> dict:
        return {
            "grant_type": self.grant_type,
            "username": self.username,
            "password": self.password,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }