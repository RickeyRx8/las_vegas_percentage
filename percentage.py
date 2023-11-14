import streamlit as st


def tryout():
    try_out_new = st.session_state['amount']
    try_out_new1 = st.session_state['percentage']
    answer = try_out_new1 * try_out_new / 100
    final_price = round(try_out_new - answer, 2)
    sales_tax = round((8.38 / 100) * final_price, 2)
    return (f'Total Savings is : {round(answer, 2)}   Final Price is  ${final_price}, '
            f'after taxes: {round(sales_tax + final_price,2)}')


st.text('Nv. Percentage Calculator')
user_amount1 = st.number_input('Enter Amount', key='amount')
user_percentage1 = st.number_input('Enter percentage', key='percentage', step=1)
tst = tryout()
show = st.write(tst)
st.button('Calculate', show)

st.session_state
