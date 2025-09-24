import requests
import streamlit as st

st.set_page_config(page_title="Скоринг кредита", page_icon="💳", layout="centered")

st.title("Скоринг кредита")
st.write("Узнайте решение по вашей заявке всего за несколько секунд!")

with st.form("credit_scoring_form"):
    st.subheader("Введите ваши данные:")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Возраст", min_value=18, max_value=100, step=1, help="Минимальный возраст — 18 лет")
        education = st.checkbox("Высшее образование")
        car = st.checkbox("Наличие автомобиля")

    with col2:
        income = st.number_input("Ежемесячный доход (в тыс. ₽)", min_value=0.0, step=0.1)
        work = st.checkbox("Стабильная работа")

    submit = st.form_submit_button("Проверить заявку")

if submit:
    data = {
        "age": int(age),
        "income": float(income),
        "education": education,
        "work": work,
        "car": car,
    }

    try:
        response = requests.post("http://127.0.0.1:8000/score", json=data)
        response.raise_for_status()
        result = response.json()

        if result.get("approved"):
            st.success("✅ Поздравляем! Ваша заявка на кредит одобрена.")
        else:
            st.warning("❌ К сожалению, заявка отклонена.\n\nСовет: попробуйте указать дополнительные данные или выбрать дебетовую карту.")
    except Exception as e:
        st.error(f"Ошибка при обращении к сервису: {e}")