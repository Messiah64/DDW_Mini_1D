import time

import streamlit as st

from app_ui import apply_app_style, render_header, render_metric_card, render_result
from library import pancake_sort_steps, pancake_sort_text


DEFAULT_MENU_ITEMS = (
    "Cloud Berry Pancakes, Apple Cinnamon Stack, Banana Brunch Cakes, "
    "Mango Maple Minis, Cocoa Sunday Stack, Lemon Zest Flapjacks"
)


st.set_page_config(page_title="Exercise 3", layout="wide")
apply_app_style()


def create_item_list(text: str) -> list[str]:
    items = []

    for item in text.split(","):
        cleaned_item = item.strip()

        if cleaned_item != "":
            items.append(cleaned_item)

    return items


def create_display_string(items: list[str]) -> str:
    return ", ".join(items)


def show_pancake_step(step, step_number: int, total_steps: int, placeholder):
    placeholder.write(f"Step {step_number} of {total_steps}")
    placeholder.write(step["message"])
    placeholder.write(step["items"])


def animate_pancake_sort(steps):
    placeholder = st.empty()
    progress_bar = st.progress(0)
    total_steps = len(steps)

    for step_number, step in enumerate(steps, start=1):
        show_pancake_step(step, step_number, total_steps, placeholder)
        progress_bar.progress(int(step_number / total_steps * 100))
        time.sleep(0.4)

    progress_bar.empty()


def clear():
    st.session_state["menu_items"] = DEFAULT_MENU_ITEMS
    st.session_state["sorted_menu_items"] = ""
    st.session_state["flip_steps"] = []
    st.session_state["exercise_3_error"] = ""


if "menu_items" not in st.session_state:
    st.session_state["menu_items"] = DEFAULT_MENU_ITEMS

if "sorted_menu_items" not in st.session_state:
    st.session_state["sorted_menu_items"] = ""

if "flip_steps" not in st.session_state:
    st.session_state["flip_steps"] = []

if "exercise_3_error" not in st.session_state:
    st.session_state["exercise_3_error"] = ""


render_header(
    "Exercise 3",
    "Pancake Sort Cafe",
    "This page sorts menu item names using Pancake Sort.",
)

columns = st.columns(3)

with columns[0]:
    render_metric_card("Data", "Menu items", "Food app data")

with columns[1]:
    render_metric_card("Algorithm", "Pancake Sort", "New algorithm")

with columns[2]:
    render_metric_card("Type", "Text", "Non-numeric data")

demo_tab, checkoff_tab, algorithm_tab = st.tabs(
    ["Demo", "Checkoff Notes", "Algorithm Notes"]
)

with demo_tab:
    st.subheader("Try Pancake Sort")
    st.write("Enter menu item names separated by commas.")

    menu_input = st.text_input(
        "Menu items",
        value=st.session_state["menu_items"],
    )

    button_columns = st.columns([1, 1, 4])

    with button_columns[0]:
        sort_clicked = st.button("Sort")

    with button_columns[1]:
        clear_clicked = st.button("Clear")

    if sort_clicked:
        items = create_item_list(menu_input)

        if len(items) == 0:
            st.session_state["exercise_3_error"] = "Please enter at least one menu item."
            st.session_state["sorted_menu_items"] = ""
            st.session_state["flip_steps"] = []
        else:
            st.session_state["menu_items"] = menu_input
            st.session_state["exercise_3_error"] = ""
            steps = pancake_sort_steps(items)
            sorted_items = pancake_sort_text(items)
            animate_pancake_sort(steps)
            st.session_state["sorted_menu_items"] = create_display_string(sorted_items)
            st.session_state["flip_steps"] = steps

    if clear_clicked:
        clear()
        st.rerun()

    if st.session_state["exercise_3_error"]:
        st.error(st.session_state["exercise_3_error"])

    result_columns = st.columns(2)

    with result_columns[0]:
        render_result(
            "Original menu",
            st.session_state["menu_items"],
            "No menu items yet.",
            chip_style="text",
        )

    with result_columns[1]:
        render_result(
            "Sorted menu",
            st.session_state["sorted_menu_items"],
            "Press Sort to see the sorted menu.",
            chip_style="text",
        )

    if st.session_state["flip_steps"]:
        st.subheader("Flip steps")

        for index, step in enumerate(st.session_state["flip_steps"], start=1):
            st.write(f"{index}. {step['message']}")

with checkoff_tab:
    st.subheader("Brainstorming")
    st.write("I looked at data from food apps, music apps, contact apps, and learning systems.")
    st.write("I chose food app menu item names because it matches the pancake theme.")

    st.subheader("Data Pugh Chart")
    st.table(
        [
            {
                "Choice": "Menu item names",
                "Non-numeric": "+",
                "Easy input": "+",
                "Easy display": "+",
                "Theme match": "+",
            },
            {
                "Choice": "Playlist titles",
                "Non-numeric": "+",
                "Easy input": "+",
                "Easy display": "0",
                "Theme match": "-",
            },
            {
                "Choice": "Contact names",
                "Non-numeric": "+",
                "Easy input": "+",
                "Easy display": "+",
                "Theme match": "-",
            },
        ]
    )

    st.subheader("Algorithm Pugh Chart")
    st.table(
        [
            {
                "Choice": "Pancake Sort",
                "New to me": "+",
                "Easy to explain": "+",
                "Fun demo": "+",
                "Chosen": "Yes",
            },
            {
                "Choice": "Gnome Sort",
                "New to me": "+",
                "Easy to explain": "0",
                "Fun demo": "0",
                "Chosen": "No",
            },
            {
                "Choice": "Shell Sort",
                "New to me": "+",
                "Easy to explain": "-",
                "Fun demo": "-",
                "Chosen": "No",
            },
        ]
    )

    st.subheader("UI Design Iterations")
    st.write("1. First idea: just input and output. Too boring.")
    st.write("2. Second idea: show all flip messages. Better.")
    st.write("3. Final idea: simple cafe demo with animation and checkoff notes.")

with algorithm_tab:
    st.subheader("How Pancake Sort Works")
    st.write("1. Look at the unsorted part of the list.")
    st.write("2. Find the biggest item alphabetically.")
    st.write("3. Flip it to the top if needed.")
    st.write("4. Flip it to the bottom of the unsorted part.")
    st.write("5. Repeat until the whole list is sorted.")

    st.subheader("Whiteboard Pseudocode")
    st.code(
        """
for size from len(items) down to 2:
    find biggest item from index 0 to size - 1

    if biggest item is not already at size - 1:
        flip biggest item to the top
        flip it into its final position
        """.strip()
    )

    st.write("Time complexity: O(n^2)")
