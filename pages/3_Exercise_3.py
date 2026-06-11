import time

import streamlit as st

from exercise_3_logic import (
    DEFAULT_MENU_ITEMS,
    make_menu_items,
    make_menu_string,
    sort_menu_text,
)
from exercise_3_ui import (
    load_styles,
    render_animation_frame,
    render_flip_steps,
    render_hero,
    render_menu_card,
    render_section_title,
    render_small_cards,
)


st.set_page_config(page_title="Exercise 3", layout="wide")
load_styles()


def reset_page():
    # All the starting values live here, so the Clear button is easy to follow.
    st.session_state["menu_text"] = DEFAULT_MENU_ITEMS
    st.session_state["original_items"] = make_menu_items(DEFAULT_MENU_ITEMS)
    st.session_state["sorted_items"] = []
    st.session_state["flip_steps"] = []
    st.session_state["exercise_3_error"] = ""


def play_animation(steps):
    # This only displays the steps. The actual sorting already happened in logic.
    animation_area = st.empty()
    progress_bar = st.progress(0)
    total_steps = len(steps)

    for step_number, step in enumerate(steps, start=1):
        render_animation_frame(
            animation_area,
            step_number,
            total_steps,
            step["message"],
            make_menu_string(step["items"]),
        )
        progress_bar.progress(int(step_number / total_steps * 100))
        time.sleep(0.35)

    progress_bar.empty()


if "menu_text" not in st.session_state:
    reset_page()


render_hero()
render_small_cards()
render_section_title(
    "Try Pancake Sort",
    "Edit the cafe menu, then sort it alphabetically with Pancake Sort.",
)

menu_input = st.text_area(
    "Menu items",
    value=st.session_state["menu_text"],
    label_visibility="collapsed",
)

button_columns = st.columns([1, 1, 4])

with button_columns[0]:
    sort_button = st.button("Sort", use_container_width=True)

with button_columns[1]:
    clear_button = st.button("Clear", use_container_width=True)

if sort_button:
    result = sort_menu_text(menu_input)

    if result["ok"]:
        st.session_state["menu_text"] = make_menu_string(result["original_items"])
        st.session_state["original_items"] = result["original_items"]
        st.session_state["sorted_items"] = result["sorted_items"]
        st.session_state["flip_steps"] = result["steps"]
        st.session_state["exercise_3_error"] = ""
        play_animation(result["steps"])
    else:
        st.session_state["sorted_items"] = []
        st.session_state["flip_steps"] = []
        st.session_state["exercise_3_error"] = result["error"]

if clear_button:
    reset_page()
    st.rerun()

if st.session_state["exercise_3_error"]:
    st.error(st.session_state["exercise_3_error"])

result_columns = st.columns(2)

with result_columns[0]:
    render_menu_card(
        "Original menu",
        st.session_state["original_items"],
        "No menu items yet.",
        "original",
    )

with result_columns[1]:
    render_menu_card(
        "Sorted menu",
        st.session_state["sorted_items"],
        "Press Sort to see the sorted menu.",
        "sorted",
    )

render_section_title(
    "Flip steps",
    "Each line below is one move Pancake Sort made during the animation.",
)
render_flip_steps(st.session_state["flip_steps"])
