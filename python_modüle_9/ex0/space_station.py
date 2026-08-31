from pydantic import BaseModel

class space(BaseModel):
	station_id: str
	name: str
	crew_size: int
# 	power_level: float
# 	oxygen_level: float
#	last_maintenance: datetime
# 	is_operational: bool = True
# 	notes: str | any

data = {"station_id":"aaa", "name": "huzefe", "crew_size": "32"}

print(data)