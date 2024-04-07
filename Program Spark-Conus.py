import pdb
import pandas as pd
import matplotlib.pyplot as plt

# Определение режимов работы двигателя
engine_modes = ['МГ', 'ПК']

# Определение позиций лопастей для каждого режима работы двигателя
blade1 = [0.00, 0.00]
blade2 = [15.00, 10.00]
blade3 = [10.00, 5.00]
blade4 = [-15.00, -10.00]
blade5 = [-20.00, -15.00]

# Выбор новой базовой лопасти
new_base_blade = 4  # Выбираем другую лопасть в качестве новой базовой лопасти

if new_base_blade > 1:
    # Определение начальных отклонений от базовой лопасти
    if new_base_blade == 2:
        initial_offsets = blade2
    elif new_base_blade == 3:
        initial_offsets = blade3
    elif new_base_blade == 4:
        initial_offsets = blade4
    else:
        initial_offsets = blade5

    # Вычисление отклонений относительно новой базовой лопасти
    offsets = {
        1: [blade1[0] - initial_offsets[0], blade1[1] - initial_offsets[1]],
        2: [blade2[0] - initial_offsets[0], blade2[1] - initial_offsets[1]],
        3: [blade3[0] - initial_offsets[0], blade3[1] - initial_offsets[1]],
        4: [blade4[0] - initial_offsets[0], blade4[1] - initial_offsets[1]],
        5: [blade5[0] - initial_offsets[0], blade5[1] - initial_offsets[1]],
    }
else:
    offsets = {
        1: [0.00, 0.00],
        2: [0.00, 0.00],
        3: [0.00, 0.00],
        4: [0.00, 0.00],
        5: [0.00, 0.00],
    }

# pdb.set_trace()

# Создание нового графика
plt.figure(figsize=(10, 5))

# Построение позиций каждой лопасти для обоих режимов работы двигателя
plt.plot(engine_modes, [offsets[1][0], offsets[1][1]], marker='o', label='Лопасть №1')
plt.plot(engine_modes, [offsets[2][0], offsets[2][1]], marker='o', label='Лопасть №2')
plt.plot(engine_modes, [offsets[3][0], offsets[3][1]], marker='o', label='Лопасть №3')
plt.plot(engine_modes, [offsets[4][0], offsets[4][1]], marker='o', label='Лопасть №4')
plt.plot(engine_modes, [offsets[5][0], offsets[5][1]], marker='o', label='Лопасть №5')

# Добавление заголовка и меток осей
plt.title('Геометрическая соконусность несущего винта')
plt.xlabel('Режим полёта')
plt.ylabel('Усреднённые координаты лопасти (мм)')

# Добавление легенды для различных лопастей
plt.legend()

# Отображение сетки
plt.grid(True)

# Отображение графика
plt.show()

# Создание таблицы на основе новых данных
data = {
    'Режим полёта': engine_modes,
    'Лопасть 1': [offsets[1][0], offsets[1][1]],
    'Лопасть 2': [offsets[2][0], offsets[2][1]],
    'Лопасть 3': [offsets[3][0], offsets[3][1]],
    'Лопасть 4': [offsets[4][0], offsets[4][1]],
    'Лопасть 5': [offsets[5][0], offsets[5][1]],
}

df = pd.DataFrame(data)
df = df.set_index('Режим полёта')
print(df)