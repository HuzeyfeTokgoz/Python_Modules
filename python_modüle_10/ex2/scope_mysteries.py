import random

mage_counter = lambda : (lambda x=[0]: x.append(x[-1] + 1) or x[-1])
spell_accumulator = lambda initial_power: (lambda added_power, x = [initial_power]: x.append(x[-1] + added_power) or x[-1])
enchantment_factory = lambda enchantment_type: ()

if __name__ == "__main__":
	initial_powers = [71, 51, 52]
	power_additions = [15, 19, 20, 5, 9]
	enchantment_types = ['Shocking', 'Earthen', 'Dark']
	items_to_enchant = ['Armor', 'Wand', 'Cloak', 'Sword']

	sayac1 = mage_counter()
	sayac2 = mage_counter()
	added_value = spell_accumulator(10)

	print("Testing mage counter...")
	for _ in range(2):
		print("counter_a:", sayac1())
	print("counter_b:", sayac2())

	print("\nTesting spell accumulator...")
	for _ in range(3):
		print(f"Base {test_value}, add {random.choice(initial_powers)}:", added_value(random.choice(power_additions)))
		#eksik ve yanlış