import tkinter as tk

def solve_sudoku():
    b=[[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            b[i].append(cells[i][j].get())
    l=['1','2','3','4','5','6','7','8','9']
    
    def check(i,j,k):
        if k in b[i]:
            return 0
        for a in b:
            if a[j]==k:
                return 0
        i1=(i//3)*3 
        j1=(j//3)*3
        for a1 in range(i1,i1+3):
            for a2 in range(j1,j1+3):
                if b[a1][a2]==k:
                    return 0
        return 1
    
    def find():
        for i in range(9):
            for j in range(9):
                if b[i][j]=='':
                    for k in l:
                        if check(i,j,k)==1:
                            b[i][j]=k
                            if find()==1:
                                return 1
                            else:
                                b[i][j]=''
                    return 0
        return 1
    
    find()
    
    solve_button.config(state=tk.DISABLED)
    for i in range(9):
        for j in range(9):
            if cells[i][j].get()!=b[i][j]:
                cell=cells[i][j]
                cell.delete(0, tk.END)
                cell.insert(0, b[i][j])
                cell.config(fg='red')

def clear_board():
    solve_button.config(state=tk.NORMAL)
    for i in range(9):
        for j in range(9):
            cell = cells[i][j]
            cell.delete(0, tk.END)
            cell.config(fg='black')
    cells[0][0].focus()

def create_input_grid(root):
    input_grid = tk.Frame(root)
    input_grid.pack()
    cells = []
    for i in range(9):
        row = []
        for j in range(9):
            cell = tk.Entry(input_grid, width=3, font=('Arial', 35), justify='center')
            if j % 3 == 0 and i%3==0:
                cell.grid(row=i, column=j, padx=(5, 1), pady=(5,1))
            elif j % 3 == 0:
                cell.grid(row=i, column=j, padx=(5, 1), pady=1)
            elif i%3==0:
                cell.grid(row=i, column=j, padx=1, pady=(5,1))
            else:
                cell.grid(row=i, column=j, padx=(1, 1), pady=1)
            cell.bind('<Button-1>', lambda event: event.widget.focus())
            cell.config(validate='key', validatecommand=(cell.register(validate_entry), '%P', '%d'))
            cell.bind('<Return>', lambda event, r=i, c=j: move_to_next_cell(event, r, c))
            row.append(cell)
        cells.append(row)
    
    return cells

def validate_entry(value, action):
    if action == '0':
        return True
    if len(value) > 1 or not value.isdigit() or int(value) ==0:
        return False
    return True

def move_to_next_cell(event, row, col):
    if col==8 and row==8:
        cells[0][0].focus()
    elif col==8:
        cells[row+1][0].focus()
    else:
        cells[row][col+1].focus()

def create_buttons(root):
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)
    global solve_button
    solve_button = tk.Button(button_frame, text='Solve', command=solve_sudoku)
    solve_button.pack(side=tk.LEFT, padx=5)

    clear_button = tk.Button(button_frame, text='Clear', command=clear_board)
    clear_button.pack(side=tk.LEFT, padx=5)

def create_gui():
    root = tk.Tk()
    root.title("Vishnu's Sudoku Solver")
    global cells
    cells = create_input_grid(root)
    create_buttons(root)
    root.mainloop()
    
create_gui()
