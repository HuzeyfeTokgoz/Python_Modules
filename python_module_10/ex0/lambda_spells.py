artifact_sorter = lambda artifacts: sorted(artifacts, key=lambda x: x["power"], reverse=True)

power_filter = lambda mages, min_power: list(filter(lambda x: x["power"] >= min_power, mages))

spell_transformer = lambda spells: list(map(lambda s: f"* {s} *", spells))

mage_stats = lambda mages: {
	"max_power": max(mages, key=lambda m: m["power"])["power"],
	"min_power": min(mages, key=lambda m: m["power"])["power"],
	"avg_power": round(sum(map(lambda m: m["power"], mages)) / len(mages), 2)
}

if __name__ == "__main__":
	spells = ["Air", "Fire", "Water"]
	artifacts = [{"name": "Huzeyfe", "power": 100}, {"name": "Eren", "power": 90}]
	mages = [
			{"name": "Air", "power": 95},
			{"name": "Fire", "power": 70},
			{"name": "Water", "power": 85}
		]

	print("Testing Artifact Sorter:", artifact_sorter(artifacts))
	print("\nTesting Power Filter:", power_filter(mages, 80))
	print("\nTesting Spell Transformer:", spell_transformer(spells))
	print("\nTesting Mage Stats:", mage_stats(mages))

