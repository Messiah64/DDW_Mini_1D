import time

import streamlit as st

from exercise_3_logic import DEFAULT_MENU_ITEMS, make_menu_string, sort_menu_text


# This file is only for the Streamlit page.
# The data cleanup and sorting code is in exercise_3_logic.py.

st.set_page_config(page_title="Exercise 3", layout="wide")


def set_starting_values():
    st.session_state["menu_items"] = DEFAULT_MENU_ITEMS
    st.session_state["sorted_menu_items"] = ""
    st.session_state["flip_steps"] = []
    st.session_state["exercise_3_error"] = ""


def show_animation(steps):
    message_area = st.empty()
    progress_bar = st.progress(0)
    total_steps = len(steps)

    for step_number, step in enumerate(steps, start=1):
        message_area.write(f"Step {step_number} of {total_steps}")
        message_area.write(step["message"])
        message_area.write(make_menu_string(step["items"]))
        progress_bar.progress(int(step_number / total_steps * 100))
        time.sleep(0.4)

    progress_bar.empty()


if "menu_items" not in st.session_state:
    set_starting_values()


st.title("Exercise 3: Pancake Sort Cafe")
st.write("This page sorts menu item names using Pancake Sort.")

st.subheader("Try Pancake Sort")
st.write("Enter menu item names separated by commas.")

menu_input = st.text_input("Menu items", value=st.session_state["menu_items"])

button_columns = st.columns([1, 1, 4])

with button_columns[0]:
    sort_button = st.button("Sort")

with button_columns[1]:
    clear_button = st.button("Clear")

if sort_button:
    result = sort_menu_text(menu_input)

    if result["ok"]:
        st.session_state["menu_items"] = make_menu_string(result["original_items"])
        st.session_state["sorted_menu_items"] = make_menu_string(
            result["sorted_items"]
        )
        st.session_state["flip_steps"] = result["steps"]
        st.session_state["exercise_3_error"] = ""
        show_animation(result["steps"])
    else:
        st.session_state["sorted_menu_items"] = ""
        st.session_state["flip_steps"] = []
        st.session_state["exercise_3_error"] = result["error"]

if clear_button:
    set_starting_values()
    st.rerun()

if st.session_state["exercise_3_error"]:
    st.error(st.session_state["exercise_3_error"])

result_columns = st.columns(2)

with result_columns[0]:
    st.subheader("Original menu")
    if st.session_state["menu_items"]:
        st.write(st.session_state["menu_items"])
    else:
        st.write("No menu items yet.")

with result_columns[1]:
    st.subheader("Sorted menu")
    if st.session_state["sorted_menu_items"]:
        st.write(st.session_state["sorted_menu_items"])
    else:
        st.write("Press Sort to see the sorted menu.")

if st.session_state["flip_steps"]:
    st.subheader("Flip steps")

    for index, step in enumerate(st.session_state["flip_steps"], start=1):
        st.write(f"{index}. {step['message']}")
