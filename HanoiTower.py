# HanoiTower is a classic algorithm to learn recursion and problem-solving.
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

hanoi(7, 'A', 'C', 'B')  # Example with 3 disks