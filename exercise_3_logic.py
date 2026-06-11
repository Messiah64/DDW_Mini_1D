from library import pancake_sort_steps, pancake_sort_text


# This file has the Exercise 3 data logic.
# It does not use Streamlit, so it is easier to test.

DEFAULT_MENU_ITEMS = (
    "Cloud Berry Pancakes, Apple Cinnamon Stack, Banana Brunch Cakes, "
    "Mango Maple Minis, Cocoa Sunday Stack, Lemon Zest Flapjacks"
)


def make_menu_items(text: str) -> list[str]:
    items = []

    for item in text.split(","):
        item = item.strip()

        if item != "":
            items.append(item)

    return items


def make_menu_string(items: list[str]) -> str:
    return ", ".join(items)


def sort_menu_text(menu_text: str) -> dict:
    menu_items = make_menu_items(menu_text)

    if len(menu_items) == 0:
        return {
            "ok": False,
            "error": "Please enter at least one menu item.",
            "original_items": [],
            "sorted_items": [],
            "steps": [],
        }

    return {
        "ok": True,
        "error": "",
        "original_items": menu_items,
        "sorted_items": pancake_sort_text(menu_items),
        "steps": pancake_sort_steps(menu_items),
    }
