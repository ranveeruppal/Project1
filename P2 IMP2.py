import random
import matplotlib.pyplot as plt
import time

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (b[0] - o[0]) * (a[1] - o[1])

def merge_hulls(left, right):
    # Helper function to get next index in a list
    def next_index(i, length):
        return (i + 1) % length

    # Helper function to get previous index in a list
    def prev_index(i, length):
        return (i - 1) % length

    # Find upper tangent
    l = len(left) - 1
    r = 0
    while True:
        changed = False
        
        # Adjust point in left hull for upper tangent
        while cross_product(right[r], left[l], left[prev_index(l, len(left))]) < 0:
            l = prev_index(l, len(left))
            changed = True
        
        # Adjust point in right hull for upper tangent
        while cross_product(left[l], right[r], right[next_index(r, len(right))]) > 0:
            r = next_index(r, len(right))
            changed = True

        # If neither of the points were adjusted, upper tangent is found
        if not changed:
            break

    upper_left, upper_right = l, r

    # Reset indices for lower tangent
    l = len(left) - 1
    r = 0

    while True:
        changed = False
        
        # Adjust point in left hull for lower tangent
        while cross_product(right[r], left[l], left[prev_index(l, len(left))]) > 0:
            l = prev_index(l, len(left))
            changed = True
        
        # Adjust point in right hull for lower tangent
        while cross_product(left[l], right[r], right[next_index(r, len(right))]) < 0:
            r = next_index(r, len(right))
            changed = True

        # If neither of the points were adjusted, lower tangent is found
        if not changed:
            break

    lower_left, lower_right = l, r

    # Constructing the merged hull
    merged_hull = []

    # Start from lower tangent on left hull and move till upper tangent
    while True:
        merged_hull.append(left[lower_left])
        if lower_left == upper_left:
            break
        lower_left = next_index(lower_left, len(left))

    # Start from upper tangent on right hull and move till lower tangent
    while True:
        merged_hull.append(right[upper_right])
        if upper_right == lower_right:
            break
        upper_right = next_index(upper_right, len(right))

    return merged_hull




def convex_hull(points):
    if len(points) <= 3:
        return points

    mid = len(points) // 2
    left = convex_hull(points[:mid])
    right = convex_hull(points[mid:])

    return merge_hulls(left, right)

def main():
    n = int(input("Enter the number of random points: "))
    
    points = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(n)]
    points.sort(key=lambda p: p[0])

    start_time = time.time()  # Start the timer

    hull = convex_hull(points)

    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time
    print(f"The time was {elapsed_time:.6f} seconds.")

    # Visualization
    plt.scatter([p[0] for p in points], [p[1] for p in points])
    hull.append(hull[0]) # To close the convex hull
    plt.plot([p[0] for p in hull], [p[1] for p in hull], 'r')
    plt.show()

    

if __name__ == "__main__":
    main()












