# goit-algo-hw-09

Greedy Algorithms and Dynamic Programming

# Coin Change Problem: Greedy vs Dynamic Programming

## Problem:

Given an amount of change (e.g. 113), determine the optimal way to return coins using:

- `find_coins_greedy` — greedy algorithm
- `find_min_coins` — dynamic programming

## Coin set used:

[50, 25, 10, 5, 2, 1]

---

## ✅ Algorithms

### 1. Greedy Algorithm

- Chooses largest coin at every step
- Fast: O(n)
- ✅ Efficient with common denominations
- ❌ Can be suboptimal with custom or tricky coin sets

### 2. Dynamic Programming

- Computes minimum number of coins for each sum
- Slower: O(amount × n)
- ✅ Always optimal solution
- ❌ Heavier for large amounts

---

## 📊 Example (amount = 113)

| Method | Result                     | Time         |
| ------ | -------------------------- | ------------ |
| Greedy | {50: 2, 10: 1, 2: 1, 1: 1} | 0.000001 sec |
| DP     | {1: 1, 2: 1, 10: 1, 50: 2} | 0.0002 sec   |

🧠 Both return same result — **because coin set is well structured**

---

## Conclusion:

- For standard coins like [50, 25, 10, 5, 2, 1], **greedy works well**
- For arbitrary coins (e.g. [9, 6, 1]), **dynamic programming is essential**
- Use **greedy for speed**, **DP for correctness**

---

## 🇺🇦 Українською

### Завдання:

Знайти оптимальний набір монет для видачі здачі (наприклад, 113) за допомогою:

- Жадібного алгоритму
- Динамічного програмування

### Приклад:

| Метод    | Результат                  | Час виконання |
| -------- | -------------------------- | ------------- |
| Жадібний | {50: 2, 10: 1, 2: 1, 1: 1} | ~0.000001 сек |
| ДП       | {50: 2, 10: 1, 2: 1, 1: 1} | ~0.0002 сек   |

---

## Висновок:

- **Жадібний** — дуже швидкий, але не завжди оптимальний
- **ДП** — завжди дає найменше число монет, підходить для будь-яких номіналів
