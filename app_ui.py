import time

import streamlit as st


def apply_app_style():
    # Keep the app close to default Streamlit styling.
    pass


def render_header(kicker: str, title: str, description: str):
    st.caption(kicker)
    st.title(title)
    st.write(description)


def render_metric_card(title: str, content: str, description: str, tone: str = "blue"):
    st.metric(title, content, help=description)


def render_panel_start(title: str, description: str):
    st.subheader(title)
    st.write(description)


def render_panel_end():
    st.write("")


def render_note(text: str):
    st.info(text)


def split_display_text(value: str) -> list[str]:
    if value == "":
        return []

    value = value.strip()

    if value.endswith("."):
        value = value[:-1]

    items = []

    for item in value.split(","):
        item = item.strip()

        if item != "":
            items.append(item)

    return items


def render_result(label: str, value: str, empty_text: str, chip_style: str = "number"):
    st.write(f"**{label}**")

    items = split_display_text(value)

    if len(items) == 0:
        st.write(empty_text)
    else:
        st.write(", ".join(items))


def render_sort_frame(step, step_number: int, total_steps: int, target=None):
    values = step["values"]
    message = step["message"]
    active_indices = step["active_indices"]

    if len(active_indices) > 0:
        message += f" Active index: {active_indices}"

    text = (
        f"Step {step_number} of {total_steps}\n\n"
        f"{message}\n\n"
        f"{values}"
    )

    if target is None:
        st.write(text)
    else:
        target.text(text)


def play_sort_animation(steps, target, delay_seconds: float = 0.25):
    if len(steps) == 0:
        return []

    progress = st.progress(0)
    total_steps = len(steps)

    for step_number, step in enumerate(steps, start=1):
        render_sort_frame(step, step_number, total_steps, target=target)
        progress.progress(int(step_number / total_steps * 100))
        time.sleep(delay_seconds)

    progress.empty()
    return steps[-1]["values"]


def render_workflow_step(title: str, description: str):
    st.write(f"**{title}**")
    st.write(description)
