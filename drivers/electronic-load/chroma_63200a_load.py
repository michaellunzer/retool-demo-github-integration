"""Chroma 63200A DC electronic load driver."""
import pyvisa


class Chroma63200A:
    def __init__(self, resource: str):
        self.inst = pyvisa.ResourceManager().open_resource(resource)

    def set_mode(self, mode: str = "CCL") -> None:
        self.inst.write(f"MODE {mode}")

    def set_current(self, amps: float) -> None:
        self.inst.write(f"CURR {amps}")

    def read_power(self) -> float:
        return float(self.inst.query("MEAS:POW?"))


    def check_alarms(self) -> dict:
        return {
            "ov": int(self.inst.query("STAT:QUES:OV?")),
            "ot": int(self.inst.query("STAT:QUES:OT?")),
        }
# pending software-team review before promotion
