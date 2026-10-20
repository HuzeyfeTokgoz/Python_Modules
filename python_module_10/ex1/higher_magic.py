import random


heal = lambda target, power: f"Heal restores {target} for {power} HP"
fireball = lambda target, power: f"Fireball hits {target} for {power} damage"
is_safe_power = lambda target, power: power <= random.randint(0, 25)

spell_combiner = lambda spell1, spell2: lambda target, power: (spell1(target, power), spell2(target, power))
power_amplifier = lambda base_spell, multiplier: lambda target, power: base_spell(target, power * multiplier)
conditional_caster = lambda condition, spell: lambda target, power: spell(target, power) if condition(target, power) else "Spell fizzled"
spell_sequence = lambda spells: lambda target, power: [spell(target, power) for spell in spells]


if __name__ == "__main__":
    test_values = [23, 12, 24]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    combo_spell = spell_combiner(heal, fireball)
    print("Testing Spell Combiner:", combo_spell(random.choice(test_targets), random.choice(test_values)))

    mega_fireball = power_amplifier(fireball, 3)
    amplifier_value = random.choice(test_values)
    print(f"\nTesting Power Amplifier: Testing normal_value = {amplifier_value}", mega_fireball(random.choice(test_targets), amplifier_value))

    safe_heal = conditional_caster(is_safe_power, heal)
    Cond_values = random.choice(test_values)
    print(f"\nTesting Conditional Caster *Testing Values {Cond_values}*:", safe_heal(random.choice(test_targets), Cond_values))

    ultimate_spell = spell_sequence([heal, fireball])
    print("\nTesting Spell Sequence:", ultimate_spell(random.choice(test_targets), random.choice(test_values)))
