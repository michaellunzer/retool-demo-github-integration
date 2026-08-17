"""Arbin LBT-5V battery cycler control + logging interface."""
import requests


class ArbinLBT:
    def __init__(self, base_url: str):
        self.base = base_url.rstrip("/")

    def start_schedule(self, channel: int, schedule: str) -> None:
        requests.post(f"{self.base}/channel/{channel}/start", json={"schedule": schedule})

    def read_channel(self, channel: int) -> dict:
        return requests.get(f"{self.base}/channel/{channel}").json()
# TODO: verify cutoff voltages against cell spec
