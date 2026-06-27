def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed: list[str] = [item.lower() for item
                          in light_spell_allowed_ingredients()]
    item_list: list[str] = [item.strip().lower() for item
                            in ingredients.split(",")]

    for i in item_list:
        if i in allowed:
            return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
