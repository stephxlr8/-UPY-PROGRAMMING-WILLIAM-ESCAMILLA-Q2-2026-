import random
import stddraw
from color import Color


# ---------- DIBUJO ----------
def draw_bars(numbers, selected=(), sorted_until=-1):
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n
    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2
        if i in selected:
            color = Color(255, 90, 90)        # lo que se esta comparando
        elif i <= sorted_until:
            color = Color(90, 200, 120)       # ya quedo ordenado
        else:
            color = Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    stddraw.show(300)


def setup_canvas(numbers):
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)


# ---------- BUBBLE ----------
def bubble_sort(numbers):
    n = len(numbers)
    for sweep in range(n):
        for pair in range(0, n - 1 - sweep):
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair + 1], numbers[pair]


def bubble_sort_animated(numbers):
    setup_canvas(numbers)
    n = len(numbers)
    for sweep in range(n):
        for pair in range(0, n - 1 - sweep):
            draw_bars(numbers, selected=(pair, pair + 1))
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair + 1], numbers[pair]
                draw_bars(numbers, selected=(pair, pair + 1))
    draw_bars(numbers)
    stddraw.show()


# ---------- SELECTION ----------
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        # asumimos que el minimo esta en la posicion i
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        # mandamos el minimo al frente de la parte no ordenada
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]


def selection_sort_animated(numbers):
    setup_canvas(numbers)
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            draw_bars(numbers, selected=(min_index, j), sorted_until=i - 1)
            if numbers[j] < numbers[min_index]:
                min_index = j
        if min_index != i:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
            draw_bars(numbers, selected=(i, min_index), sorted_until=i - 1)
    draw_bars(numbers, sorted_until=n - 1)
    stddraw.show()


# ---------- INSERTION ----------
def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        # recorremos a la derecha todo lo que sea mayor que key
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key


def insertion_sort_animated(numbers):
    setup_canvas(numbers)
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        draw_bars(numbers, selected=(i,), sorted_until=i - 1)
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
            draw_bars(numbers, selected=(j + 1,), sorted_until=i - 1)
        numbers[j + 1] = key
        draw_bars(numbers, selected=(j + 1,), sorted_until=i)
    draw_bars(numbers, sorted_until=n - 1)
    stddraw.show()


# ---------- MAIN ----------
numbers = [random.randint(0, 100) for x in range(10)]
print(f"Antes: {numbers}")

# escoge el que quieras probar (solo uno a la vez):
# bubble_sort_animated(numbers)
# selection_sort_animated(numbers)
insertion_sort_animated(numbers)

print(f"Despues: {numbers}")