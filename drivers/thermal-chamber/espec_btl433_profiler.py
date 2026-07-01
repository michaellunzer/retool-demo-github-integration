"""Espec BTL-433 chamber profiler (early dev build)."""
import socket


class EspecBTL433:
    def __init__(self, host: str, port: int = 57732):
        self.sock = socket.create_connection((host, port))

    def set_temp(self, celsius: float) -> None:
        self.sock.sendall(f"TEMP,S{celsius}\\\\r\\\\n".encode())
# WARNING: no over-temp interlock -- do not use for unattended runs


    def load_profile(self, steps: list) -> None:
        """steps: list of (temp_c, dwell_min). Still no interlock."""
        for temp, _dwell in steps:
            self.set_temp(temp)
## test comment