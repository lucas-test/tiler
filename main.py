### TON ALGO


# t est un tableau de taille n* où n=len(t)
def algo(t):
    


    return []








### DO NOT TOUCH



import tkinter as tk


def top_rect(t, i, j):
    n = len(t)
    while i >= 0 and t[i][j]:
        i -= 1
    if i < 0:
        return 0
    else:
        return i+1

def bottom_rect(t, i, j):
    n = len(t)
    while i < n and t[i][j]:
        i += 1
    if i >= n:
        return n-1
    else:
        return i-1

def left_rect(t, i, j):
    n = len(t)
    while j >= 0 and t[i][j]:
        j -= 1
    if j < 0:
        return 0
    else:
        return j+1

def right_rect(t, i, j):
    n = len(t)
    while j < n and t[i][j]:
        j += 1
    if j >= n:
        return n-1
    else:
        return j-1

def has_unique_max(t, n, i, j):
    top = top_rect(t, i, j)
    left = left_rect(t,i,j)
    right = right_rect(t,i,j)
    bottom = bottom_rect(t,i,j)

    for k in range(left, right+1):
        for l in range(top, bottom+1):
            if t[l][k] == 0:
                return False
    return True

def fill_rect(t, rect):
    left, right, top, bottom = rect[0], rect[1], rect[2], rect[3]
    modifications = []
    for k in range(left, right+1):
        for l in range(top, bottom+1):
            if t[l][k] == 0:
                print("bug fill rect", l, k)
            elif t[l][k] == 1:
                t[l][k] = 2
                modifications.append([l,k])
    return modifications


def get_max_rect(t, n, i,j):
    top = top_rect(t, i, j)
    left = left_rect(t,i,j)
    right = right_rect(t,i,j)
    bottom = bottom_rect(t,i,j)
    return [left, right, top, bottom]

def fill_unique_max(t,n,i,j):
    top = top_rect(t, i, j)
    left = left_rect(t,i,j)
    right = right_rect(t,i,j)
    bottom = bottom_rect(t,i,j)

    return fill_rect(t, [left, right, top, bottom])
    # for k in range(left, right+1):
    #     for l in range(top, bottom+1):
    #         t[l][k] = 2


def search_unique_max(t,n):
    for i in range(n):
        for j in range(n):
            if t[i][j] == 1 and has_unique_max(t,n, i,j):
                return [i,j]
    return None


# def print_colored_matrix(matrix):
#     colors = {
#         0: '\033[97m',  # White
#         1: '\033[90m',  # Black
#         2: '\033[91m',  # Red
#         '\033[0m': ''     # Reset color
#     }

#     max_width = len(str(len(matrix)))
#     max_height = len(matrix)

#     for row in matrix:
#         for val in row:
#             if val == 1:
#                 print('\033[40m\033[K', end='')  # Set background color to black
#             elif val == 2:
#                 print('\033[41m\033[K', end='')  # Set background color to red
#             else:
#                 print('\033[47m\033[K', end='')  # Set background color to white
            
#             print(' ', end=' ')  # Print a space
#         print()  # Newline after each row

#     print('\033[0m', end='')  # Reset color for final output

def search_uncovered(t,n):
    for i in range(n):
        for j in range(n):
            if t[i][j] == 1:
                return [i,j]
    return None


def check_is_rect(t, n, left, right, top, bottom):
    for k in range(left, right+1):
        for l in range(top, bottom+1):
            if t[l][k] == 0:
                return False
    return True

def is_max(rects, rect):
    for r in rects:
        if r[0] <= rect[0] and rect[1] <= r[1] and r[2] <= rect[2] and rect[3] <= r[3]:
            return False
    return True

def add_rect(rects, r):
    cleaned = [r]
    for rect in rects:
        if r[0] <= rect[0] and rect[1] <= r[1] and r[2] <= rect[2] and rect[3] <= r[3]:
            continue
        else:
            cleaned.append(rect)
    return cleaned
    

            

def get_max_useful_rects(t, n, i, j):
    top = top_rect(t, i,j)
    bottom = bottom_rect(t, i, j)
    left = left_rect(t,  i,j)
    right = right_rect(t,i,j)

    # print(i,j, " -- ", left, right, top, bottom)

    rects = []
    for a in range(left, j+1):
        for b in range(top, i+1):
            for c in range(j, right+1):
                for d in range(i, bottom+1):
                    rect = [a,c,b,d]
                    # print( rect, check_is_rect(t,n,a,c,b,d), is_max(rects, rect))
                    if check_is_rect(t, n, a, c, b, d) and is_max(rects, rect):
                        rects = add_rect(rects, rect)
    return rects


def reset_modif(t, modif):
    for [i,j] in modif:
        t[i][j] = 1


def aux(t, current):
    n = len(t)
    r = search_unique_max(t,n)
    if r == None:
        s = search_uncovered(t,n)
        if s == None:
            return current.copy()
        else:
            i,j = s[0], s[1]

            rects = get_max_useful_rects(t,n,i,j)
            if len(rects) == 0:
                print("bug", i, j, "max rects empty")
            best_score = len(t)*len(t)
            best_rects = []
            for rect in rects:
                modif = fill_rect(t, rect)
                current.append(rect)
                result = aux(t, current)
                current.pop()
                if len(result) < best_score:
                    best_score = len(result)
                    best_rects = result
                reset_modif(t, modif)
            return best_rects
    else:
        i,j = r[0], r[1]
        modif = fill_unique_max(t, n, i, j)
        rect = get_max_rect(t,n, i, j)
        current.append(rect)
        best_rects = aux(t, current)
        current.pop()
        reset_modif(t, modif)
        return best_rects






def solve(t):
    print(t)
    n = len(t)

    while True:
        r = search_unique_max(t,n)
        if r == None:
            return
        else:
            i,j = r[0], r[1]
            fill_unique_max(t, n, i, j) 
            print("--------------")
            print_colored_matrix(t)

        




class SquareGrid:
    def __init__(self, master):
        self.master = master
        self.size = 200
        self.square_size = 20
        self.grid = [[False for _ in range(self.size // self.square_size)] for _ in range(self.size // self.square_size)]
        
        self.canvas = tk.Canvas(master, width=self.size, height=self.size)
        self.canvas.pack()
        
        self.draw_grid()
        self.bind_click_events()
        self.bind_key_events()

        self.draw_rect([1,2,1,1])


    def bind_key_events(self):
        # self.master.bind('r', lambda event: self.run_solve())
        # self.master.bind('R', lambda event: self.run_solve())

        self.master.bind('s', lambda event: self.run_min())
        self.master.bind('S', lambda event: self.run_min())

        self.master.bind('e', lambda event: self.run_algo())
        self.master.bind('E', lambda event: self.run_algo())

    def run_solve(self):
        t = [[int(bool_val) for bool_val in row] for row in self.grid]
        solve(t)

    def run_algo(self):
        t = [[int(bool_val) for bool_val in row] for row in self.grid]
        rects = algo(t)
        if rects != None:
            print("min", len(rects))
            for rect in rects:
                self.draw_rect(rect)


    def run_min(self):
        t = [[int(bool_val) for bool_val in row] for row in self.grid]
        rects = aux(t,[])
        print("min cover", len(rects))
        for rect in rects:
            self.draw_rect(rect)


    def draw_grid(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                
                color = 'black' if self.grid[row][col] else 'white'
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def bind_click_events(self):
        self.canvas.bind('<Button-1>', self.toggle_square)

    def toggle_square(self, event):
        row = event.y // self.square_size
        col = event.x // self.square_size
        
        self.grid[row][col] = not self.grid[row][col]
        self.draw_grid()

    def draw_rect(self, rect):
        left, right, top, bottom = rect
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        size = self.square_size

        # Convert grid indices to canvas coordinates
        x1 = max(0, int(left * self.square_size))
        y1 = max(0, int(top * self.square_size))
        x2 = min(canvas_width, int(right * self.square_size))
        y2 = min(canvas_height, int(bottom * self.square_size))

        # Draw the rectangle
        color = '#2196F3'  # Modern blue color
        padding = 4
        self.canvas.create_rectangle(
            left*size + padding, 
            top*size + padding, 
            (right+1)*size -padding, 
            (bottom+1)*size- padding ,
             outline=color, width=1)

root = tk.Tk()
app = SquareGrid(root)
root.mainloop()