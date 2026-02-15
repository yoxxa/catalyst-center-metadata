import polars as pl
from bcs_oi_api import BCSOIAPI
from bcs_oi_api.models import (
    Device,
    Asset, 
    Contract,
    PINDetails,
    RiskMitigationDetails,
)
class BCSOICollector:
    def __init__(self, client_id, client_secret, region) -> None:
        self.bcs_sdk = BCSOIAPI(
            client_id = client_id,
            client_secret = client_secret,
            region = region
        )
        self.devices: pl.DataFrame = None
        self.assets: pl.DataFrame = None
        self.contracts: pl.DataFrame = None
        self.place_in_network: pl.DataFrame = None
        self.risk_mitigations: pl.DataFrame = None

    def collect_data(self) -> None:
        #self.get_devices()
        ##self.get_assets()
        #self.get_contracts()
        #self.get_place_in_network()
        self.get_risk_mitigations()

    def get_devices(self) -> list[dict]:
        self.devices = pl.DataFrame(
            [dict(device) for device in self.bcs_sdk.get_output(model = Device)]
        )

    def get_assets(self) -> None:
        self.assets = pl.DataFrame(
            [dict(asset) for asset in self.bcs_sdk.get_output(model=Asset)]
        )

    def get_contracts(self) -> None:
        contracts = [dict(contract) for contract in self.bcs_sdk.get_output(model=Contract)]
        # Transform nested data into valid dict's
        for row in contracts:
            row.update({
                "base_product_id_list": [dict(base_product) for base_product in row["base_product_id_list"]],
                "orderable_product_id_list": [dict(orderable_product) for orderable_product in row["orderable_product_id_list"]]
            })
        self.contracts = pl.DataFrame(
            contracts
        )
    
    def get_place_in_network(self) -> None:
        self.place_in_network = pl.DataFrame(
            [dict(pin) for pin in self.bcs_sdk.get_output(model=PINDetails)]
        )
    
    def get_risk_mitigations(self) -> None:
        self.risk_mitigations = pl.DataFrame(
            [dict(risk_mitigation) for risk_mitigation in self.bcs_sdk.get_output(model=RiskMitigationDetails)]
        )