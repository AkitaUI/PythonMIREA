import heapq

def dijkstra(check, start, goals):
    x0, y0 = start
    queue = []
    heapq.heappush(queue, (0, x0, y0, []))  # (g, x, y, path)
    visited = set()

    while queue:
        g, x, y, path = heapq.heappop(queue)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) in goals:
            return path[0] if path else "pass"

        for dx, dy, move in [
            (-1, 0, "left"),
            (1, 0, "right"),
            (0, -1, "up"),
            (0, 1, "down"),
        ]:
            nx, ny = x + dx, y + dy
            if check("wall", nx, ny) or (nx, ny) in visited:
                continue
            heapq.heappush(queue, (g + 1, nx, ny, path + [move]))

    return "pass"

def script(check, x, y):
    if check("gold", x, y):
        return "take"
    gold_positions = [
        (gx, gy) for gx in range(32) for gy in range(32) if check("gold", gx, gy)
    ]
    if gold_positions:
        return dijkstra(check, (x, y), gold_positions)
    return "right" if not check("wall", x + 1, y) else "down"
