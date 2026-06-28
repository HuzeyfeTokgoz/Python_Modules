def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed: list[str] = []
    for item in light_spell_allowed_ingredients():
        allowed.append(item.lower())

    item_list: list[str] = []
    for item in ingredients.split(","):
        item_list.append(item.strip().lower())

    for i in item_list:
        if i in allowed:
            return f"{ingredients} VALID"

    return f"{ingredients} INVALID"
