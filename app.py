"""Streamlit entrypoint for the marketplace card maker v1 interface skeleton."""

from __future__ import annotations

import streamlit as st


ALLOWED_IMAGE_TYPES = ["png", "jpg", "jpeg", "webp"]


def render_uploaded_images(title: str, files: list) -> None:
    """Render a simple preview gallery for uploaded images."""
    st.markdown(f"**{title}**")
    if not files:
        st.caption("Пока ничего не загружено.")
        return

    cols = st.columns(3)
    for index, uploaded_file in enumerate(files):
        with cols[index % 3]:
            st.image(uploaded_file, caption=uploaded_file.name, use_container_width=True)


def main() -> None:
    """Render the basic Streamlit UI for step-by-step card generation workflow."""
    st.set_page_config(page_title="Marketplace Card Maker", page_icon="🛍️", layout="wide")

    st.title("🛍️ Marketplace Card Maker")
    st.write(
        "Внутренний инструмент для подготовки карточек товаров для Ozon и Wildberries. "
        "Сейчас это базовый интерфейс v1 без подключения генерации."
    )

    st.divider()

    st.subheader("Данные товара")
    product_name = st.text_input("Название товара")
    product_description = st.text_area("Описание товара", height=100)
    product_specs = st.text_area("Характеристики", height=100)
    product_benefits = st.text_area("Преимущества", height=100)
    product_bundle = st.text_area("Комплектация", height=80)

    size_col, material_col = st.columns(2)
    with size_col:
        product_sizes = st.text_input("Размеры")
    with material_col:
        product_material = st.text_input("Материал")

    restricted_phrases = st.text_area("Что нельзя писать", height=80)

    st.divider()

    st.subheader("Площадка")
    marketplace = st.radio("Выберите площадку", options=["Ozon", "Wildberries"], horizontal=True)

    st.subheader("Количество карточек")
    card_count = st.selectbox("Сколько карточек нужно", options=[6, 8], index=0)

    st.divider()

    st.subheader("Фото товара")
    product_images = st.file_uploader(
        "Загрузите фото товара (от 1 до 10)",
        type=ALLOWED_IMAGE_TYPES,
        accept_multiple_files=True,
    )

    if len(product_images) > 10:
        st.warning("Можно загрузить не более 10 фото товара.")
    elif product_images:
        st.success(f"Загружено фото товара: {len(product_images)}")

    render_uploaded_images("Предпросмотр фото товара", product_images)

    st.divider()

    st.subheader("Референсы и стиль")
    reference_images = st.file_uploader(
        "Загрузите референсы (от 1 до 5)",
        type=ALLOWED_IMAGE_TYPES,
        accept_multiple_files=True,
    )

    if len(reference_images) > 5:
        st.warning("Можно загрузить не более 5 референсов.")
    elif reference_images:
        st.success(f"Загружено референсов: {len(reference_images)}")

    likes_in_references = st.text_area("Что нравится в референсах", height=80)
    avoid_in_style = st.text_area("Чего избегать", height=80)
    has_brand_book = st.checkbox("У клиента есть фирменный стиль")
    brand_style_comment = st.text_area("Комментарий по фирменному стилю", height=80)

    render_uploaded_images("Предпросмотр референсов", reference_images)

    st.divider()

    st.subheader("Действия")
    action_col_1, action_col_2, action_col_3 = st.columns(3)

    with action_col_1:
        if st.button("Сохранить проект", use_container_width=True):
            st.info("Заглушка: сохранение проекта будет добавлено на следующем шаге.")

    with action_col_2:
        if st.button("Сгенерировать анализ референсов", use_container_width=True):
            st.info("Заглушка: анализ референсов будет подключен позже.")

    with action_col_3:
        if st.button("Сгенерировать 3 главные карточки", use_container_width=True):
            st.success("Заглушка: генерация 3 главных карточек будет реализована позже.")

    # Keep variables referenced to show clear structure for future integration.
    _ = {
        "product_name": product_name,
        "product_description": product_description,
        "product_specs": product_specs,
        "product_benefits": product_benefits,
        "product_bundle": product_bundle,
        "product_sizes": product_sizes,
        "product_material": product_material,
        "restricted_phrases": restricted_phrases,
        "marketplace": marketplace,
        "card_count": card_count,
        "product_images": product_images,
        "reference_images": reference_images,
        "likes_in_references": likes_in_references,
        "avoid_in_style": avoid_in_style,
        "has_brand_book": has_brand_book,
        "brand_style_comment": brand_style_comment,
    }


if __name__ == "__main__":
    main()
