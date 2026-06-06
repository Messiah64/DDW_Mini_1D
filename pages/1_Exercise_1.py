import streamlit as st
from datetime import datetime
from library import gen_random_int, create_string, insertion_sort_steps
from app_ui import (
    apply_app_style,
    render_header,
    play_sort_animation,
    render_result,
)

st.set_page_config(
    page_title="Exercise 1",
    layout="wide",
)

apply_app_style()


def generate():
    # Generate 10 random numbers using the current time as the seed.
    seed = datetime.now().timestamp()
    array: list[int] = gen_random_int(10, seed)

    # Convert the list into text so Streamlit can display it.
    array_str: str = create_string(array)

    st.session_state["numbers"] = array_str
    st.session_state["sorted_numbers"] = ""


def parse_generated_numbers(numbers: str) -> list[int]:
    numbers = numbers.replace(".", "")
    number_strings = numbers.split(",")
    array_int: list[int] = []

    for number in number_strings:
        cleaned_number = number.strip()

        if cleaned_number != "":
            integer_number = int(cleaned_number)
            array_int.append(integer_number)

    return array_int


def sort_generated_numbers(animation_slot):
    # Retrieves the generated number from the session_state
    numbers: str = st.session_state.numbers

    if numbers == "":
        st.session_state["sorted_numbers"] = ""
        animation_slot.warning("Generate numbers first, then sort them.", icon=":material/info:")
        return

    array_int = parse_generated_numbers(numbers)
    steps = insertion_sort_steps(array_int)
    sorted_array = play_sort_animation(steps, animation_slot)
    array_str: str = create_string(sorted_array)

    st.session_state["sorted_numbers"] = array_str


def clear():
    st.session_state['numbers'] = ""
    st.session_state['sorted_numbers'] = ""


if 'numbers' not in st.session_state:
    st.session_state.numbers = ""

if 'sorted_numbers' not in st.session_state:
    st.session_state.sorted_numbers = ""

render_header(
    "Exercise 1",
    "Random Number Sorting",
    "Generate ten random integers and sort them step by step.",
)

st.subheader("Controls")
button_columns = st.columns(3)
animation_slot = st.empty()

with button_columns[0]:
    if st.button("Generate"):
        generate()
        st.rerun()

with button_columns[1]:
    if st.button("Sort"):
        sort_generated_numbers(animation_slot)

with button_columns[2]:
    if st.button("Clear"):
        clear()
        st.rerun()

result_columns = st.columns(2)

with result_columns[0]:
    render_result(
        "Generated Numbers",
        st.session_state['numbers'],
        "No numbers generated yet.",
    )

with result_columns[1]:
    render_result(
        "Sorted Numbers",
        st.session_state['sorted_numbers'],
        "Sort output will appear here.",
    )
