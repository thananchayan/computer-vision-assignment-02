import numpy as np
import cv2
from collections import deque

def region_growing(image, seed_point, threshold=50):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    visited = np.zeros_like(gray_image, dtype=bool)
    region = np.zeros_like(gray_image, dtype=np.uint8)
    queue = deque()
    queue.append(seed_point)
    seed_value = gray_image[seed_point]
    visited[seed_point] = True

    while queue:
        x, y = queue.popleft()
        region[x, y] = 255

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if (0 <= nx < gray_image.shape[0]) and (0 <= ny < gray_image.shape[1]) and not visited[nx, ny]:
                    if abs(int(gray_image[nx, ny]) - int(seed_value)) <= threshold:
                        visited[nx, ny] = True
                        queue.append((nx, ny))

    return region
