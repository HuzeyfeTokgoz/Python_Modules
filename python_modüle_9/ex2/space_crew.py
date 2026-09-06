from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Any
import random
import json


class RankEnum(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankEnum
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=5, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        rank_error: bool = False
        years_error: bool = False
        for member in self.crew:
            if member.rank in [RankEnum.captain, RankEnum.commander]:
                rank_error = True
            if not member.years_experience >= 5:
                years_error = True

        if not rank_error:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365 and years_error:
            raise ValueError("Long missions (> 365 days) "
                             "need 50% experienced crew (5+ years)")

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self

    def __str__(self) -> str:
        detail_list = []
        for member in self.crew:
            detail_list.append(f"- {member.name} ({member.rank.value}) "
                               f"- {member.specialization}")

        return "\n".join([
            f"Mission: {self.mission_name}",
            f"ID: {self.mission_id}",
            f"Destination: {self.destination}",
            f"Duration: {self.duration_days}",
            f"Budget: {self.budget_millions}",
            f"Crew size: {len(self.crew)}",
            "Crew members:\n" + "\n".join(detail_list)
        ])


def json_plugin() -> list[Any] | None:
    try:
        with open("../generated_data/space_missions.json") as dosya:
            reader = json.load(dosya)
            data = random.choices(reader, k=3)
    except FileNotFoundError as e:
        print(e)
        return None
    else:
        return data


if __name__ == "__main__":
    data = json_plugin()
    if not data:
        raise ValueError("Data found")

    print("\nSpace Mission Crew Validation")
    print("==============================================\n")

    for i in range(len(data)):
        try:
            crew_list = []
            for j in range(len(data[i]["crew"])):
                crew_obj = CrewMember(
                    member_id=data[i]["crew"][j]["member_id"],
                    name=data[i]["crew"][j]["name"],
                    rank=data[i]["crew"][j]["rank"],
                    age=data[i]["crew"][j]["age"],
                    specialization=data[i]["crew"][j]["specialization"],
                    years_experience=data[i]["crew"][j]["years_experience"],
                    is_active=data[i]["crew"][j]["is_active"]
                )
                crew_list.append(crew_obj)

            mission = SpaceMission(
                    mission_id=data[i]["mission_id"],
                    mission_name=data[i]["mission_name"],
                    destination=data[i]["destination"],
                    launch_date=data[i]["launch_date"],
                    duration_days=data[i]["duration_days"],
                    crew=crew_list,
                    mission_status=data[i]["mission_status"],
                    budget_millions=data[i]["budget_millions"]
                )

            print("Valid mission created:")
            print(mission)

        except ValidationError as e:
            error = e.errors()
            print("Expected validation error:\n", error[0]['msg'])
        print("\n==============================================")
