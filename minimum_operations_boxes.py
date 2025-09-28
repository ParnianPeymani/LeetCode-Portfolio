def minOperations(boxes):
    n = len(boxes)
    ball_positions = [i for i, ball in enumerate(boxes) if ball == "1"]
    result = [sum(abs(i - pos) for pos in ball_positions) for i in range(n)]
    return result