import streamlit as st
from library import create_string, insertion_sort_steps
from app_ui import (
    apply_app_style,
    render_header,
    render_panel_start,
    play_sort_animation,
    render_result,
)

st.set_page_config(
    page_title="Exercise 2",
    layout="wide",
)

apply_app_style()


def sort_numbers(numbers: str, animation_slot):
    # Split by comma, remove extra spaces, and ignore empty entries.
    number_strings = [number.strip() for number in numbers.split(",") if number.strip()]

    if not number_strings:
        st.session_state['sorted_numbers'] = ""
        st.session_state['input_error'] = "Please enter at least one integer."
        animation_slot.empty()
        return

    try:
        array_int: list[int] = [int(number) for number in number_strings]
    except ValueError:
        st.session_state['sorted_numbers'] = ""
        st.session_state['input_error'] = "Use only integers separated by commas."
        animation_slot.empty()
        return

    steps = insertion_sort_steps(array_int)
    sorted_array = play_sort_animation(steps, animation_slot)
    array_str: str = create_string(sorted_array)

    st.session_state['numbers'] = numbers
    st.session_state['sorted_numbers'] = array_str
    st.session_state['input_error'] = ""


def clear():
    st.session_state['numbers'] = ""
    st.session_state['sorted_numbers'] = ""
    st.session_state['input_error'] = ""

if 'numbers' not in st.session_state:
    st.session_state.numbers = ""

if 'sorted_numbers' not in st.session_state:
    st.session_state.sorted_numbers = ""

if 'input_error' not in st.session_state:
    st.session_state.input_error = ""

render_header(
    "Exercise 2",
    "Manual Number Sorting",
    "Type comma-separated integers and sort them step by step.",
)

render_panel_start(
    "Type your own stack",
    "Use commas between integers, then watch the cards move into sorted order.",
)

entered_numbers = st.text_input(
    "Numbers",
    value=st.session_state['numbers'],
    placeholder="8, 3, 5, 1, 9",
)

st.session_state['numbers'] = entered_numbers

button_columns = st.columns([1, 1, 4])
animation_slot = st.empty()

with button_columns[0]:
    if st.button("Sort"):
        sort_numbers(st.session_state['numbers'], animation_slot)

with button_columns[1]:
    if st.button("Clear"):
        clear()
        st.rerun()

if st.session_state['input_error']:
    st.error(st.session_state['input_error'], icon=":material/error:")

result_columns = st.columns(2)

with result_columns[0]:
    render_result(
        "Input Numbers",
        st.session_state['numbers'],
        "Type numbers to build a stack.",
    )

with result_columns[1]:
    render_result(
        "Sorted Numbers",
        st.session_state['sorted_numbers'],
        "Sorted output will appear here after you enter integers.",
    )
