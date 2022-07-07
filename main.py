import random
import streamlit as st

st.write('가위 바위 보 게임')

choice = ['가위','바위','보']
com_choice = random.choice(choice)

jiho_choice = st.text_input("가위 바위 보 중 하나를 입력하세요")


if jiho_choice =='가위' and com_choice == '가위':
    st.write(f'AI: {com_choice} 나: {jiho_choice} - 결과: 비겼다')
elif jiho_choice =='가위' and com_choice == '보':
    st.write(f'AI: {com_choice} 나: {jiho_choice} - 결과: 이겼다')
elif jiho_choice =='가위' and com_choice == '바위':
    st.write(f'AI: {com_choice} 나: {jiho_choice} - 결과: 졌다')
elif jiho_choice =='보' and com_choice == '보':
    st.write(f'AI: {com_choice} 나: {jiho_choice} - 결과: 비겼다')
elif jiho_choice =='보' and com_choice == '바위':
    st.write(f'AI: {com_choice} 나: {jiho_choice} - 결과: 이겼다')
elif jiho_choice =='보' and com_choice == '주먹':
    st.write(f'AI: {com_choice} 나: {jiho_choice} - 결과: 졌다')
elif jiho_choice =='바위' and com_choice == '바위':
    st.write(f'AI: {com_choice} 나: {jiho_choice} - 결과: 비겼다')
elif jiho_choice =='바위' and com_choice == '가위':
    st.write(f'AI: {com_choice} 나: {jiho_choice} - 결과: 이겼따')
elif jiho_choice =='바위' and com_choice == '보':
    st.write(f'AI: {com_choice} 나: {jiho_choice} - 결과: 졌다')
