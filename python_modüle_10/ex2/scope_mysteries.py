import random

mage_counter = lambda : (lambda x=[0]: x.append(x[-1] + 1) or x[-1])
spell_accumulator = lambda initial_power: (lambda added_power, x = [initial_power]: x.append(x[-1] + added_power) or x[-1])
enchantment_factory = lambda enchantment_type: lambda item_name: f"{enchantment_type} {item_name}"
memory_vault = lambda: (lambda storage: {
	'store': lambda key, value: storage.update({key:value}),
	'recall': lambda key: storage.get(key, "Memory not found")
	})({})


if __name__ == "__main__":
	initial_powers = [71, 51, 52]
	power_additions = [15, 19, 20, 5, 9]
	enchantment_types = ['Shocking', 'Earthen', 'Dark']
	items_to_enchant = ['Armor', 'Wand', 'Cloak', 'Sword']


	print("Testing mage counter...")
	sayac1 = mage_counter()
	sayac2 = mage_counter()
	for i in range(3):
		print(f"counter_a call {i}:", sayac1())
	print()
	for i in range(2):
		print(f"counter_b call {i}:", sayac2())

	print("\nTesting spell accumulator...")
	for _ in range(3):
		power = random.choice(initial_powers)
		add_power = random.choice(power_additions)

		added_value = spell_accumulator(power)
		new_power = added_value(add_power)
		print(f"Base {power}, add {add_power}: {new_power}")

	print("\nTesting enchantment factory...")
	for _ in range(3):
		enc_type = random.choice(enchantment_types)
		enc_name = random.choice(items_to_enchant)

		enchantment = enchantment_factory(enc_type)
		print(enchantment(enc_name))

	print("\nTesting memory vault...")
	memory = memory_vault()
	key1 = random.choice(items_to_enchant)
	value = random.choice(power_additions)

	memory['store'](key1, value)
	print(f"Store '{key1}' = {value}")
	print(f"Recall '{key1}': {memory['recall'](key1)}")
	print(f"Recall 'unknown': {memory['recall']('')}")