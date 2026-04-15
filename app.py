"""Streamlit entrypoint for the marketplace card maker MVP skeleton."""

import streamlit as st


def main() -> None:
    """Render a minimal landing page for the v1 project skeleton."""
    st.set_page_config(page_title="Marketplace Card Maker", page_icon="🛍️", layout="centered")

    st.title("🛍️ Marketplace Card Maker")
    st.write(
        "Внутренний инструмент для пошаговой генерации карточек товаров "
        "для Ozon и Wildberries."
    )
    st.info("Сейчас это каркас v1: базовая структура проекта без бизнес-логики.")


if __name__ == "__main__":
    main()
