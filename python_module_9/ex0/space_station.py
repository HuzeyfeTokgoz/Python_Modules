from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
import random
import csv
import json
from typing import Any


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)

    def __str__(self) -> str:
        person: str = ""
        operation_value: str = ""
        if self.crew_size == 1:
            person = "person"
        else:
            person = "people"

        if self.is_operational:
            operation_value = "Operational"
        else:
            operation_value = "Non-operational"

        return "\n".join([
                f"ID: {self.station_id}",
                f"Name: {self.name}",
                f"Crew: {self.crew_size} {person}",
                f"Power: {self.power_level:.1f}%",
                f"Oxygen: {self.oxygen_level:.1f}%",
                f"Date: {self.last_maintenance:%Y-%m-%d}",
                f"Status: {operation_value}",
                f"Notes: {self.notes}"
        ])


def csv_plugin() -> list[dict[str, Any]]:
    try:
        with open("generated_data/space_stations.csv") as dosya:
            reader = csv.DictReader(dosya)
            data = random.choices(list(reader), k=3)
    except FileNotFoundError as e:
        print(e)
        return []
    else:
        return data


def json_plugin() -> list[dict[str, Any]]:
    try:
        with open("generated_data/space_stations.json") as dosya:
            reader = json.load(dosya)
            data = random.choices(reader, k=3)
    except FileNotFoundError as e:
        print(e)
        return []
    else:
        return data


def invalid_plugin() -> list[dict[str, Any]]:
    try:
        with open("generated_data/invalid_stations.json") as dosya:
            reader = json.load(dosya)
            data = random.choices(reader, k=3)
    except FileNotFoundError as e:
        print(e)
        return []
    else:
        return data


def main() -> None:
    plugin = json_plugin() + csv_plugin() + invalid_plugin()
    data = random.choices(plugin, k=3)

    if not data:
        print("Data not found")

    print("Space Station Data Validation")
    print("=======================================")
    for i in data:
        print("Valid station created:")
        try:
            print(SpaceStation(
                station_id=i["station_id"],
                name=i["name"],
                crew_size=i["crew_size"],
                power_level=i["power_level"],
                oxygen_level=i["oxygen_level"],
                last_maintenance=i["last_maintenance"],
                is_operational=i["is_operational"],
            ))
        except ValidationError as e:
            error = e.errors()
            print("Expected validation error:\n", error[0]['msg'])
        print("\n=======================================")


if __name__ == "__main__":
    main()
