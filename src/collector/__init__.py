from bcs_oi_api import BCSOIAPI
from bcs_oi_api.models import (
    Device,
    Asset, 
    Contract
)
class BCSOICollector:
    def __init__(self, client_id, client_secret, region) -> None:
        self.bcs_sdk = BCSOIAPI(
            client_id = client_id,
            client_secret = client_secret,
            region = region
        )
        self.data: list[dict] = list()

    def collect_data(self) -> None:
        self.data.extend(self.get_devices())

    def get_devices(self) -> list[dict]:
        return [dict(device) for device in self.bcs_sdk.get_output(model = Device)]