from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = []
    for item in dark_spell_allowed_ingredients():
        allowed.append(item.lower())

    item_list: list[str] = []
    for item in ingredients.split(","):
        item_list.append(item.strip().lower())

    for i in item_list:
        if i in allowed:
            return f"{ingredients} VALID"

    return f"{ingredients} INVALID"
