from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = [item.lower() for item
                          in dark_spell_allowed_ingredients()]
    item_list: list[str] = [item.strip().lower() for item
                            in ingredients.split(",")]

    for i in item_list:
        if i in allowed:
            return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
