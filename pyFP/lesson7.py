import itertools

def ConquestCampaign(N, M, L, battalion):
    # Инициализация
    coords = list(zip(battalion[::2], battalion[1::2]))
    initial = set(coords)
    total_cells = N * M
    
    if len(initial) == total_cells:
        return 1
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def generate_new(current):
        # Генерирует все возможные соседние клетки для текущего множества
        points_directions = itertools.product(current, directions)
        new_points = ((x + dx, y + dy) for (x, y), (dx, dy) in points_directions)
        # Фильтруем точки в пределах плацдарма
        valid_points = filter(lambda p: 1 <= p[0] <= N and 1 <= p[1] <= M, new_points)
        # Преобразуем в множество и вычитаем уже захваченные
        return set(valid_points) - current

    
    def conquere(day, conquered):
        if len(conquered) == total_cells:
            return day
        new_neighbors = generate_new(conquered)
        new_captured = conquered.union(new_neighbors)
        return conquere(day + 1, new_captured)
    
    return conquere(1, initial)


print(ConquestCampaign(3,4,2,[2,2,3,4]))
