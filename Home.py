# Main Streamlit app file.
# Run this project with: streamlit run Home.py

import streamlit as st

from app_ui import (
    apply_app_style,
    render_header,
    render_metric_card,
    render_note,
    render_panel_end,
    render_panel_start,
    render_workflow_step,
)

st.set_page_config(
    page_title="Sorting Studio",
    layout="wide",
)

apply_app_style()

render_header(
    "Mini Project 1",
    "Sorting Studio",
    "Generate lists, sort them with your own algorithms, and inspect the output in a clean native Streamlit interface.",
)

metric_columns = st.columns(3)

with metric_columns[0]:
    render_metric_card(
        "Core Algorithm",
        "Insertion Sort",
        "Implemented in library.py",
        "blue",
    )

with metric_columns[1]:
    render_metric_card(
        "Input Modes",
        "3",
        "Random, manual, and text data",
        "teal",
    )

with metric_columns[2]:
    render_metric_card(
        "Pages",
        "4",
        "Home plus three exercises",
        "amber",
    )

render_panel_start(
    "Pick a workflow",
    "Choose the exercise you want to run. Each page keeps the original sorting behavior and presents the input, action, and result clearly.",
)

workflow_columns = st.columns(3)

with workflow_columns[0]:
    render_workflow_step(
        "Exercise 1",
        "Generate ten random integers, sort them, and compare the generated and sorted lists.",
    )
    st.page_link("pages/1_Exercise_1.py", label="Open Exercise 1", icon=":material/shuffle:")

with workflow_columns[1]:
    render_workflow_step(
        "Exercise 2",
        "Type your own comma-separated integers and send them through the same sorting function.",
    )
    st.page_link("pages/2_Exercise_2.py", label="Open Exercise 2", icon=":material/edit_note:")

with workflow_columns[2]:
    render_workflow_step(
        "Exercise 3",
        "Sort non-numeric text data using the open-ended custom sorting page.",
    )
    st.page_link("pages/3_Exercise_3.py", label="Open Exercise 3", icon=":material/text_fields:")

render_panel_end()

render_note(
    "Each workflow uses the functions in library.py, so the app UI and algorithm tests stay separate."
)
