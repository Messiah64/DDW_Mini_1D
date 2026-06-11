from html import escape
from pathlib import Path

import streamlit as st


APP_STYLE_FILE = Path(__file__).parent / "styles" / "app.css"
STYLE_FILE = Path(__file__).parent / "styles" / "exercise_3.css"


def load_styles():
    # Keeping the CSS in its own file makes this page much easier to explain.
    css = APP_STYLE_FILE.read_text(encoding="utf-8")
    css += "\n" + STYLE_FILE.read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def render_hero():
    st.markdown(
        """
        <section class="pancake-hero">
            <div class="hero-copy">
                <p class="hero-kicker">Exercise 3</p>
                <h1>Pancake Sort Cafe</h1>
                <p>
                    Sort cafe menu names by flipping the stack one section at
                    a time, just like Pancake Sort does.
                </p>
            </div>
            <div class="pancake-art" aria-hidden="true">
                <div class="steam steam-one"></div>
                <div class="steam steam-two"></div>
                <div class="pancake syrup"></div>
                <div class="pancake golden"></div>
                <div class="pancake berry"></div>
                <div class="plate"></div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_small_cards():
    st.markdown(
        """
        <div class="info-grid">
            <div class="info-card">
                <span class="info-label">Data</span>
                <strong>Menu names</strong>
                <p>Non-numeric text data.</p>
            </div>
            <div class="info-card">
                <span class="info-label">Algorithm</span>
                <strong>Pancake Sort</strong>
                <p>Find, flip, and lock one item at a time.</p>
            </div>
            <div class="info-card">
                <span class="info-label">Demo</span>
                <strong>Step by step</strong>
                <p>The animation shows every flip.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_title(title: str, text: str):
    st.markdown(
        f"""
        <div class="section-heading">
            <h2>{escape(title)}</h2>
            <p>{escape(text)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_menu_card(title: str, items: list[str], empty_text: str, card_type: str):
    if len(items) == 0:
        content = f'<p class="empty-text">{escape(empty_text)}</p>'
    else:
        chips = []

        for item in items:
            chips.append(f'<span class="menu-chip">{escape(item)}</span>')

        content = '<div class="chip-list">' + "".join(chips) + "</div>"

    st.markdown(
        f"""
        <div class="menu-card {escape(card_type)}">
            <p class="card-kicker">{escape(title)}</p>
            {content}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_animation_frame(
    area,
    step_number: int,
    total_steps: int,
    message: str,
    items_text: str,
):
    area.markdown(
        f"""
        <div class="animation-card">
            <div class="animation-topline">
                <span>Step {step_number} of {total_steps}</span>
            </div>
            <p class="animation-message">{escape(message)}</p>
            <p class="animation-stack">{escape(items_text)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_flip_steps(steps: list[dict]):
    if len(steps) == 0:
        return

    rows = []

    for index, step in enumerate(steps, start=1):
        rows.append(
            '<div class="timeline-item">'
            f'<span class="timeline-number">{index}</span>'
            "<div>"
            f"<strong>{escape(step['action'])}</strong>"
            f"<p>{escape(step['message'])}</p>"
            "</div>"
            "</div>"
        )

    st.markdown(
        '<div class="timeline">' + "".join(rows) + "</div>",
        unsafe_allow_html=True,
    )
