from bcs_oi_api import BCSOIAPI

class BCSOICollector:
    def __init__(self, client_id, client_secret, region) -> None:
        self.bcs_sdk = bcs_oi_api = BCSOIAPI(
            client_id = client_id,
            client_secret = client_secret,
            region = region
        )
        self.data: list[dict] = list()