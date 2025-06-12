import tkinter as tk
import time

class HanoiGUI:
    def __init__(self, root, num_disks):
        self.root = root
        self.num_disks = num_disks
        self.canvas_width = 600
        self.canvas_height = 300
        self.peg_width = 10
        self.disk_height = 20
        self.disk_min_width = 30
        self.disk_max_width = 120
        self.delay = 0.3  # thời gian delay giữa các bước

        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        # Vị trí 3 cọc
        self.pegs_x = [150, 300, 450]
        self.pegs_y = self.canvas_height - 20

        # Danh sách đĩa trên từng cọc
        self.stacks = [[], [], []]

        # Vẽ 3 cọc
        for x in self.pegs_x:
            self.canvas.create_rectangle(x - self.peg_width // 2, 50, x + self.peg_width // 2, self.pegs_y, fill='black')

        # Tạo đĩa ban đầu ở cọc A
        for i in range(self.num_disks):
            width = self.disk_min_width + (self.disk_max_width - self.disk_min_width) * (self.num_disks - i - 1) // (self.num_disks - 1)
            disk = self.canvas.create_rectangle(
                self.pegs_x[0] - width // 2,
                self.pegs_y - i * self.disk_height,
                self.pegs_x[0] + width // 2,
                self.pegs_y - i * self.disk_height - self.disk_height,
                fill='skyblue'
            )
            self.stacks[0].append(disk)

        # Bắt đầu thuật toán
        self.root.after(1000, lambda: self.solve(self.num_disks, 0, 1, 2))

    def move_disk(self, from_peg, to_peg):
        if not self.stacks[from_peg]:
            return

        disk = self.stacks[from_peg].pop()
        y = self.pegs_y - len(self.stacks[to_peg]) * self.disk_height

        coords = self.canvas.coords(disk)
        width = coords[2] - coords[0]

        new_x1 = self.pegs_x[to_peg] - width // 2
        new_x2 = self.pegs_x[to_peg] + width // 2
        new_y1 = y - self.disk_height
        new_y2 = y

        self.canvas.coords(disk, new_x1, new_y1, new_x2, new_y2)
        self.stacks[to_peg].append(disk)
        self.root.update()
        time.sleep(self.delay)

    def solve(self, n, source, auxiliary, target):
        if n == 1:
            self.move_disk(source, target)
        else:
            self.solve(n - 1, source, target, auxiliary)
            self.move_disk(source, target)
            self.solve(n - 1, auxiliary, source, target)

# Gọi chương trình chính
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tháp Hà Nội - Python GUI")
    gui = HanoiGUI(root, num_disks=7)  # Bạn có thể đổi số đĩa tại đây
    root.mainloop()
