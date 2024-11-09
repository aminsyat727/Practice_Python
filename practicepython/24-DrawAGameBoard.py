def column_create(size):
    horizontal_line = " ---"
    vertical_line = "|   "
    horizontal_column = ""
    vertical_column = ""
    for i in range(size):
        horizontal_column += horizontal_line
        vertical_column += vertical_line
    
    horizontal_column += " "
    vertical_column += "|"

    return horizontal_column, vertical_column


 
def row_create(column, rowsize, columnsize):
    h, v = column_create(columnsize)
    for i in range(rowsize):
        print(h + "\n" + v)

    return print(h)

def get_size():
    row_size = int(input("Please specify row size: "))
    column_size = int(input("Please specify column size: "))

    return row_size, column_size

row, column = get_size()
print(row, column)
row_create(column_create(column), row, column)








