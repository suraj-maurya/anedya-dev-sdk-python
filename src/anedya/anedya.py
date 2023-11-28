from config import config
from data import batch
import requests

class AnedyaClient:
    def AnedyaInstance(self, config: config.AnedyaConfig):
        """
        Initialize the Anedya SDK.

        Args:
            config (AnedyaConfig): Anedya SDK configuration.
        """
        self._config = config
        # Create 
        

    def submit_data(self, d: batch):
        """
        Send data to Anedya Cloud
        """
        headers = {'Content-type': 'application/json'}
        r = requests.post("https://device." + self._config.region + ".anedya.io/v1/submitData", data=d.encodeJSON(), headers=headers)
        if r.status_code != 200:
            return False
        return True

    
