** start of main.py **

def hanoi_solver(n):
    # Initialize rods as lists, first rod has disks n..1 (largest to smallest)
    rods = [list(range(n, 0, -1)), [], []]
    result = []

    def record_state():
        # Record current state of rods as a string: "[rod1] [rod2] [rod3]"
        result.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move_disks(num, start, end, temp):
        if num == 0:
            return
        # Move top n-1 disks to temp rod
        move_disks(num - 1, start, temp, end)

        # Move the nth disk from start to end
        disk = rods[start].pop()
        rods[end].append(disk)
        record_state()

        # Move the n-1 disks from temp to end rod
        move_disks(num - 1, temp, end, start)

    # Record initial state before any move
    record_state()

    # Solve the puzzle by recursive moves
    move_disks(n, 0, 2, 1)

    # Return all states joined by newline character
    return "\n".join(result)


** end of main.py **
