import pandas as pd
import numpy as np

import streamlit as st

st.markdown("<h2 style='text-align: center; color: black;'>Введение в PyTorch</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image('images/introduction.png', width = 650)

with col3:
    st.write("")

st.write("")
st.write(
"""

Нейронные сети – это мощный инструмент в области искусственного интеллекта, который имитирует работу человеческого мозга. Они используются для решения различных задач, таких как распознавание образов, классификация данных, генерация изображений, прогнозирование и многое другое. Нейронные сети состоят из множества взаимосвязанных нейронов, которые передают и обрабатывают информацию. Они обладают способностью обучаться на основе имеющихся данных и адаптироваться к новым ситуациям.

PyTorch — это фреймворк для языка программирования Python, предназначенный для работы с нейронными сетями. Он включает в себя набор инструментов для работы с моделями, используется в обработке естественного языка, компьютерном зрении и других похожих направлениях. 
"""
)

st.write("""Взаимодействие с данными в PyTorch очень похоже на взаимодействие с данными в numpy. [У всех функций Numpy есть своя пара в Torch!](https://github.com/torch/torch7/wiki/Torch-for-Numpy-users) Осталось теперь вспомнить [numpy](https://pythonist.ru/python-numpy-tutorial/) 🙂""")

st.write("""Тензоры являются ключевыми компонентами Pytorch. Можно сказать, что PyTorch полностью основан на тензорах. С математической точки зрения, прямоугольный массив чисел называется метрикой. В библиотеке Numpy эти метрики называются ndaaray. В PyTorch они известны как Tensor. Тензор — это n-мерный контейнер данных. Например, в PyTorch 1d-тензор — это вектор, 2d-тензор — это метрика, 3d-тензор — это куб, а 4d-тензор — это кубический вектор.""")

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image('images/tensor_example.jpeg', width = 750)

with col3:
    st.write("")

st.write(
"""
Давайте теперь посмотрим, как мы можем использовать PyTorch для работы с векторами и тензорами.

Напомним, что тензор - это многомерный вектор, например :

x = np.array ([1,2,3]) - вектор = тензор с 1 размерностью (точнее: (3,))

y = np.array ([[1, 2, 3], [4, 5, 6]]) - матрица = тензор с двумя измерениями ((2, 3) в данном случае)

z = np.array ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])-" куб "(3, 3, 3) = тензор с тремя измерениями (( 3, 3, 3)в этом случае)

Одним из реальных примеров трехмерного тензора является изображение, оно имеет 3 измерения: высота, ширина и глубина канала.
"""
)

st.markdown("<h6 style='text-align: left; color: black;'>Типы Тензоров</h6>", unsafe_allow_html=True)

st.write("""
В PyTorch мы будем использовать torch.Tensor (FloatTensor, IntTensor, ByteTensor) для всех вычислений.

torch.HalfTensor      # 16 бит, floating point

torch.FloatTensor     # 32 бита, floating point

torch.DoubleTensor    # 64 бита, floating point

torch.ShortTensor     # 16 бит, integer, signed

torch.IntTensor       # 32 бита, integer, signed

torch.LongTensor      # 64 бита, integer, signed

torch.CharTensor      # 8 бит, integer, signed

torch.ByteTensor      # 8 бит, integer, unsigned
""")

st.markdown("<h6 style='text-align: left; color: black;'>Создание тензора</h6>", unsafe_allow_html=True)

st.write("""Следующая конструкция создаст нам тензор с двумя строками и тремя столбцами и заполнит его случайными значениями:""")
st.image('images/example_1.png', width = 650)

st.write("""Для того чтобы посмотреть размеры созданного тензера, можно воспользоваться командой shape""")

st.image('images/example_2.png', width = 350)


st.markdown("<h6 style='text-align: left; color: black;'>Изменение формы</h6>", unsafe_allow_html=True)
st.write("""Изменять форму тензора можно двумя, абсолютно эквивалентными, командами: np.reshape() == torch.view():""")

st.image('images/example_3.png', width = 350)
st.image('images/example_4.png', width = 350)

st.markdown("<h6 style='text-align: left; color: black;'>Изменение типа тензора</h6>", unsafe_allow_html=True)
st.image('images/example_5.png', width = 350)

st.markdown("<h6 style='text-align: left; color: black;'>Арифметические операции</h6>", unsafe_allow_html=True)
st.write("""Сложение и вычитание""")
st.image('images/example_6.png', width = 600)
st.image('images/example_7.png', width = 350)
st.write("""Так же сложение и вычитание можно производить при помощи команд add и sub. Которые могут как создавать новый тензор с результатом, так и перезаписать результат в первый тензор""")
st.image('images/example_21.png', width = 700)
st.image('images/example_8.png', width = 350)
st.image('images/example_9.png', width = 350)
st.write("""Умножение и деление""")
st.write("""Умножение и деление, так же как и сложение и вычитание, можно делать как при помощи стандартных операций * и /, так и при помощи специальных функций mull и div""")
st.image('images/example_10.png', width = 600)

st.markdown("<h6 style='text-align: left; color: black;'>Операции сравнения</h6>", unsafe_allow_html=True)
st.image('images/example_11.png', width = 600)
st.markdown("<h6 style='text-align: left; color: black;'>Использование индексации по логической маске</h6>", unsafe_allow_html=True)
st.image('images/example_12.png', width = 600)
st.write("""Применение функции вдоль оси""")
st.write("""Многие функции в NumPy требуют, чтобы вы указали ось, вдоль которой применяется определенный расчет.

Обычно применяется следующее эмпирическое правило:

axis=0 : применить вычисление «по столбцам» \n
axis=1 : применить вычисление «построчно» \n
На следующем изображении показано визуальное представление осей в матрице NumPy с 2 строками и 4 столбцами:""")
st.image('images/example_13.png', width = 750)
st.image('images/example_14.png', width = 400)
st.markdown("<h6 style='text-align: left; color: black;'>Матричные операции</h6>", unsafe_allow_html=True)
st.write("""При помощи pytorch с матрицами можно производить много различный манипуляций. Например, \n
транспонировать""")
st.image('images/example_15.png', width = 500)
st.write("""Скалярно и вектарно переменожать""")
st.image('images/example_16.png', width = 550)


st.markdown("<h6 style='text-align: center; color: black;'>Задание для лабораторной работы</h6>", unsafe_allow_html=True)


click0 = st.selectbox("Что такое PyTorch?", ["", "Фреймворк для языка программирования Python, предназначенный для работы с матрицами", "Библиотека в языке Python для работы с тензорами", "Фреймворк для языка программирования Python, предназначенный для работы с нейронными сетями."])

click1 = st.selectbox("Какие размеры у тензора [[1, 2], [3, 4], [5, 6], [7, 8]]", ["", "[4, 2]", "[2, 2, 2, 2]", "[2, 2, 2, 4]"])

st.write("""Чему будет равно среднее значение четвертого стобца векторного произведения матриц""")
st.image('images/example_17.png', width = 400)
click2 = st.selectbox("", ["", "46", "31", "26"])

st.write("""Дана матрица  𝑀×𝑁. Выберете недастающий кусок кода для функции, чтобы она возвращала вектор средних значений по вертикали.""")
st.image('images/example_18.png', width = 400)

click3 = st.selectbox("", ["","A.avg(dim=0)", "A.mean(dim=1)", "A.mean(dim=0)"])

st.write("""Дана две матрицы. Чему будет равно среднее значение произведения этих матриц, если их транспонировать""")
st.image('images/example_19.png', width = 500)

click4 = st.selectbox("", ["", "2919.22", "618.15", "3875.43"])


click5 = st.selectbox("Чем функция sub отличается от функции sub_", ["", "sub записывает результат в первый тензор, а sub_ создает новый тензое", "sub создает новый тензор, а sub_ записывает результат в первый тензор", "Они ничем не отличаются"])

st.write("""Как получить тензор размера [1, 9]""")
st.image('images/example_20.png', width = 500)

click6 = st.selectbox("", ["", "reshape(-1)", "view(-1)", "Можно использовать как reshape(-1) так и view(-1)"])

click7 = st.selectbox("Как произвести суммирование по строке", ["", "torch.sum(A, axis=0)", "torch.sum(A)", "torch.sum(A, axis=1)"])

count = 0
if click0 == "Фреймворк для языка программирования Python, предназначенный для работы с нейронными сетями.":
    count += 1
    
if click1 == "[4, 2]":
    count += 1
    
if click2 == "26":
    count += 1
    
if click3 == "A.mean(dim=1)":
    count += 1
    
if click4 == "2919.22":
    count += 1
    
if click5 == "sub создает новый тензор, а sub_ записывает результат в первый тензор":
    count += 1
    
if click6 == "Можно использовать как reshape(-1) так и view(-1)":
    count += 1

if click7 == "torch.sum(A, axis=1)":
    count += 1

if count >= 7:
    st.markdown("<h6 style='text-align: center; color: black;'>Лабораторная работа cдана!</h6>", unsafe_allow_html=True)


else:
    st.markdown("<h6 style='text-align: center; color: black;'>Лабораторная работа пока не сдана</h6>", unsafe_allow_html=True)

