def update_weight(weights:list, pos: int):
    if isinstance(pos, list):
        for p in pos:
            weights[p] += 10
    elif isinstance(pos, int):
        weights[pos] += 10
    else:
        return
