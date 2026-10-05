"""Smart Room CPS Simulator

A small Cyber-Physical System (CPS) project. A simulated temperature sensor
feeds a controller that switches a cooling fan on and off. The program logs
the physical state and plots it after the simulation.
"""

import csv
import random
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Room:
    """A simple physical model of a room."""

    temperature: float = 31.0
    outside_temperature: float = 35.0
    fan_on: bool = False

    def update(self) -> None:
        # Heat naturally moves toward the outside temperature.
        self.temperature += (self.outside_temperature - self.temperature) * 0.06
        # The fan removes heat when the controller turns it on.
        if self.fan_on:
            self.temperature -= 0.70
        # Small random variation represents people, sunlight and sensor noise.
        self.temperature += random.uniform(-0.12, 0.12)


class TemperatureSensor:
    def read(self, room: Room) -> float:
        return round(room.temperature + random.uniform(-0.20, 0.20), 2)


class CoolingController:
    """Uses hysteresis so the fan does not rapidly toggle."""

    ON_THRESHOLD = 30.0
    OFF_THRESHOLD = 27.0

    def decide(self, measured_temperature: float, fan_is_on: bool) -> bool:
        if measured_temperature >= self.ON_THRESHOLD:
            return True
        if measured_temperature <= self.OFF_THRESHOLD:
            return False
        return fan_is_on


def run_simulation(steps: int = 60) -> list[dict]:
    room = Room()
    sensor = TemperatureSensor()
    controller = CoolingController()
    readings = []

    for second in range(1, steps + 1):
        measured = sensor.read(room)
        room.fan_on = controller.decide(measured, room.fan_on)
        room.update()
        row = {
            "time_seconds": second,
            "temperature_c": round(room.temperature, 2),
            "sensor_reading_c": measured,
            "fan_status": "ON" if room.fan_on else "OFF",
        }
        readings.append(row)
        print(
            f"{second:02d}s | Sensor: {measured:5.2f} C | "
            f"Fan: {row['fan_status']:3} | Room: {row['temperature_c']:5.2f} C"
        )
    return readings


def save_results(readings: list[dict], output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)
    csv_file = output_dir / "temperature_log.csv"
    with csv_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=readings[0].keys())
        writer.writeheader()
        writer.writerows(readings)

    try:
        import matplotlib.pyplot as plt

        times = [row["time_seconds"] for row in readings]
        temperatures = [row["temperature_c"] for row in readings]
        fan_state = [30.4 if row["fan_status"] == "ON" else 26.6 for row in readings]
        plt.figure(figsize=(10, 5))
        plt.plot(times, temperatures, label="Room temperature", linewidth=2)
        plt.step(times, fan_state, where="post", label="Fan state (visual marker)", alpha=0.7)
        plt.axhline(30, color="red", linestyle="--", label="Fan ON: 30 C")
        plt.axhline(27, color="green", linestyle="--", label="Fan OFF: 27 C")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Temperature (C)")
        plt.title("Smart Room CPS: Temperature Control")
        plt.legend()
        plt.grid(alpha=0.25)
        plt.tight_layout()
        plt.savefig(output_dir / "temperature_graph.png", dpi=160)
        plt.close()
        print(f"\nSaved log and graph in: {output_dir.resolve()}")
    except ImportError:
        print(f"\nSaved log in: {output_dir.resolve()}")
        print("Install matplotlib to generate the graph: pip install matplotlib")


if __name__ == "__main__":
    print("SMART ROOM CPS SIMULATION")
    print(f"Started: {datetime.now():%Y-%m-%d %H:%M:%S}\n")
    project_dir = Path(__file__).parent
    data = run_simulation()
    save_results(data, project_dir)
