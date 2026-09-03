from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
import random, csv, json

class SpaceStation(BaseModel):
    station_id: str = Field(min_length = 3, max_length = 10)
    name: str = Field(min_length = 1, max_length = 50)
    crew_size: int = Field(ge = 1, le = 20)
    power_level: float = Field(ge = 0.0, le = 100.0)
    oxygen_level: float = Field(ge = 0.0, le = 100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default = None, max_length = 200)

    def __str__(self):
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

def csv_plugin():
    try:
        with open("../generated_data/space_stations.csv") as dosya:
            reader = csv.DictReader(dosya)
            data = random.choices(list(reader), k=3)
    except FileNotFoundError as e:
        print(e)
    else:
        return data

def json_plugin():
    try:
        with open("../generated_data/space_stations.json") as dosya:
            reader = json.load(dosya)
            data = random.choices(reader, k=3)
    except FileNotFoundError as e:
        print(e)
    else:
        return data


if __name__ == "__main__":
    data = json_plugin() or csv_plugin()
    print("Space Station Data Validation")
    print("=======================================")
    for i in range(3):
        if not data:
            break
        print("Valid station created:")
        try:
            print(SpaceStation(
                station_id = data[i]["station_id"],
                name = data[i]["name"],
                crew_size = data[i]["crew_size"],
                power_level = data[i]["power_level"],
                oxygen_level = data[i]["oxygen_level"],
                last_maintenance = data[i]["last_maintenance"],
                is_operational = data[i]["is_operational"],
                notes = data[i]["notes"]
            ))
            print("=======================================")
        except ValidationError as e:
            error = e.errors()
            print("Expected validation error:\n", error[0]['msg'])
