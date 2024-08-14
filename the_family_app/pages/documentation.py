"""The documentation page of the app."""

from the_family_app import styles
from the_family_app.templates import template

import reflex as rx


@template(route="/documentation", title="Documentation")
def documentation() -> rx.Component:
    """The documentation page.

    Returns:
        The UI for the docs page.
    """
    with open("docs/index.md", encoding="utf-8") as docs:
        content = docs.read()

    return rx.markdown(content, component_map=styles.markdown_style)
