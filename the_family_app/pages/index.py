"""The home page of the app."""

from the_family_app import styles
from reflex_calendar import calendar
from the_family_app.templates import template

import reflex as rx


@template(route="/", title="Home")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
        
    tabs = rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Home", value="tab1"),
                rx.tabs.trigger("Calendar", value="tab2"),
            ),
            rx.tabs.content(
                rx.markdown(content, component_map=styles.markdown_style),
                value="tab1",
            ),
            rx.tabs.content(
                calendar(),
                value="tab2",
            ),
            default_value="tab1",
        )

    return tabs

