from vita.utils.base_producer import BaseProducer
from vita.utils.logger import logging

logger = logging.getLogger(__name__)


class BloodGlucoseProducer(BaseProducer):
    def __init__(self):
        super().__init__(topic="glucose")
        self.hostname = str.encode("glucose-device")

    def send_blood_glucose(self, blood_glucose: dict):
        logger.info(f"Sending data to topic {self.topic}: {blood_glucose}")
        self.producer.send(
            "glucose",
            key=self.hostname,
            value=blood_glucose,
        )
