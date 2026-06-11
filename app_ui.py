import time
from html import escape
from pathlib import Path

import streamlit as st


STYLE_FILE = Path(__file__).parent / "styles" / "app.css"


def apply_app_style():
    # The shared look for Home, Exercise 1, and Exercise 2 lives in CSS.
    css = STYLE_FILE.read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def render_header(kicker: str, title: str, description: str):
    st.markdown(
        f"""
        <section class="app-hero">
            <div>
                <p class="hero-kicker">{escape(kicker)}</p>
                <h1>{escape(title)}</h1>
                <p>{escape(description)}</p>
            </div>
            <div class="sort-hero-art" aria-hidden="true">
                <div class="hero-card card-one">9</div>
                <div class="hero-card card-two">2</div>
                <div class="hero-card card-three">6</div>
                <div class="hero-arrow">sort</div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_metric_card(title: str, content: str, description: str, tone: str = "blue"):
    st.markdown(
        f"""
        <div class="metric-card {escape(tone)}">
            <p>{escape(title)}</p>
            <strong>{escape(content)}</strong>
            <span>{escape(description)}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_panel_start(title: str, description: str):
    st.markdown(
        f"""
        <div class="section-title">
            <h2>{escape(title)}</h2>
            <p>{escape(description)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_panel_end():
    st.write("")


def render_note(text: str):
    st.markdown(
        f"""
        <div class="note-card">
            {escape(text)}
        </div>
        """,
        unsafe_allow_html=True,
    )


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
    items = split_display_text(value)

    if len(items) == 0:
        content = f'<p class="empty-result">{escape(empty_text)}</p>'
    else:
        chips = []

        for item in items:
            chips.append(f'<span class="result-chip {escape(chip_style)}">{escape(item)}</span>')

        content = '<div class="result-chip-row">' + "".join(chips) + "</div>"

    st.markdown(
        f"""
        <div class="result-card">
            <p class="card-label">{escape(label)}</p>
            {content}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sort_frame(step, step_number: int, total_steps: int, target=None):
    values = step["values"]
    active_indices = step["active_indices"]
    sorted_until = step["sorted_until"]
    message = step["message"]
    cards = []

    for index, value in enumerate(values):
        state_class = ""

        if index in active_indices:
            state_class = "active"
        elif index <= sorted_until:
            state_class = "sorted"

        cards.append(
            f'<div class="number-card {state_class}"><span>{escape(str(value))}</span></div>'
        )

    active_text = ""

    if len(active_indices) > 0:
        active_text = f"<span>Active index: {escape(str(active_indices))}</span>"

    cards_html = "".join(cards)
    html = (
        '<div class="sort-frame">'
        '<div class="sort-frame-top">'
        f"<span>Step {step_number} of {total_steps}</span>"
        f"{active_text}"
        "</div>"
        f"<p>{escape(message)}</p>"
        f'<div class="number-row">{cards_html}</div>'
        "</div>"
    )

    if target is None:
        st.markdown(html, unsafe_allow_html=True)
    else:
        target.markdown(html, unsafe_allow_html=True)


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
    st.markdown(
        f"""
        <div class="workflow-card">
            <strong>{escape(title)}</strong>
            <p>{escape(description)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
