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
        self.get_devices()
        self.get_assets()

    def get_devices(self) -> list[dict]:
        self.data.extend(
            [dict(device) for device in self.bcs_sdk.get_output(model = Device)]
        )

    # TODO - improve time space complexity of this call
    def get_assets(self) -> None:
        assets = [dict(asset) for asset in self.bcs_sdk.get_output(model=Asset)]
        for row in self.data:
            row.update({
               "assets": [dict(asset) for asset in assets if asset["device_id"] == row["device_id"]]
            })
            print(row)