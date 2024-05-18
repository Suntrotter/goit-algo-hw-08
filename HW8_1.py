import heapq

def min_cost_to_combine_cables(cables):
    heapq.heapify(cables)  # Перетворення списку в купу

    total_cost = 0
    while len(cables) > 1:
        # Отримуємо два найкоротші кабелі
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)

        # З'єднуємо кабелі
        combined_length = shortest1 + shortest2
        total_cost += combined_length

        # Додаємо об'єднаний кабель назад до купи
        heapq.heappush(cables, combined_length)

    return total_cost

# Приклад використання
cables = [9, 8, 7, 6, 14] #101
min_cost = min_cost_to_combine_cables(cables)
print("Мінімальні витрати на об'єднання кабелів:", min_cost)

