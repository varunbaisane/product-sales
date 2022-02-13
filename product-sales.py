print('Product Sales Management')
print('Enter Your Product Details for Two Halves of the Year -->')
h1_table = []
h2_table = []
col_heading = ['PRODUCT ID', 'NAME', 'COST PRICE', 'SELLING PRICE', 'UNITS SOLD', 'TOTAL AMOUNT', 'PROFIT', 'PROFIT %']
h1_table.append(col_heading)
h2_table.append(col_heading)

def enter_data():
    data_choice = 'yes'
    while data_choice.lower() == 'yes':
        prod_id = input('\ni)Enter the ID of the Product: ')
        prod_name = input('\nii)Enter the Name of your Product: ')
        prod_cp = float(input('\niii)Enter the Cost Price of the Product: '))
        prod_cp = round(prod_cp, 2)

        print('\nI] Now Enter the values for First Half of the Year -->')
        h1_prod_sp = float(input('\ni)Enter the Selling Price of the Product: '))
        h1_prod_sp = round(h1_prod_sp, 2)
        h1_prod_sold = int(input('\nii)Enter the number of Units Sold: '))

        print('\nII] Now Enter the values for First Half of the Year -->')
        h2_prod_sp = float(input('\ni)Enter the Selling Price of the Product: '))
        h2_prod_sp = round(h2_prod_sp, 2)
        h2_prod_sold = int(input('\nii)Enter the number of Units Sold: '))

        h1_cp_tot = h1_prod_sold * prod_cp
        h1_sp_tot = h1_prod_sold * h1_prod_sp
        h1_profit = h1_sp_tot - h1_cp_tot
        h1_profit_pc = round((h1_profit / h1_cp_tot) * 100, 2)

        h2_cp_tot = h2_prod_sold * prod_cp
        h2_sp_tot = h2_prod_sold * h2_prod_sp
        h2_profit = h2_sp_tot - h2_cp_tot
        h2_profit_pc = round((h2_profit / h2_cp_tot) * 100, 2)

        h1_table.append([prod_id, prod_name, prod_cp, h1_prod_sp, h1_prod_sold, h1_sp_tot, h1_profit, h1_profit_pc])
        h2_table.append([prod_id, prod_name, prod_cp, h2_prod_sp, h2_prod_sold, h2_sp_tot, h2_profit, h2_profit_pc])

        data_choice = input('\nWant to Enter data for next Product?\nEnter "Yes" to enter data and Enter "No" to Exit: ')

def display_h1():
    h1_len = -1
    for row in range(len(h1_table)):
        for ind in range(8):
            if len(str(h1_table[row][ind])) > h1_len:
                h1_len = len(str(h1_table[row][ind]))
                h1_w = h1_table[row][ind]

    h1_width = len(str(h1_w))

    print('  --------------------  ')
    print('| 1ST HALF OF THE YEAR |')
    print('  --------------------  ')
    for row in range(len(h1_table)):
        for col in range(8):
            print('| {:<{}} '.format(h1_table[row][col], h1_width), end=' |')
        print()

def display_h2():
    h2_len = -1
    for row in range(len(h2_table)):
        for ind in range(8):
            if len(str(h2_table[row][ind])) > h2_len:
                h2_len = len(str(h2_table[row][ind]))
                h2_w = h2_table[row][ind]

    h2_width = len(str(h2_w))

    print('  --------------------  ')
    print('\n \n| 2ND HALF OF THE YEAR |')
    print('  --------------------  ')
    for row in range(len(h2_table)):
        for col in range(8):
            print('| {:<{}} '.format(h2_table[row][col], h2_width), end=' |')
        print()

def display_prod():
    print()#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def update_data():
    print()#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def delete_prod():
    del_id = input("Enter the Product ID which you want to Delete: ")
    for i in range(0, len(h1_table)):
        if h1_table[i][0] == del_id:
            h1_table.pop(i)
            break
    display_h1()
    for i in range(0, len(h2_table)):
        if h2_table[i][0] == del_id:
            h2_table.pop(i)
            break
    display_h2()

def sort_data():
    print()#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

choice = 5
#main loop
while choice == 5:
    enter_data()

    choice = 1
    while choice != 5:
        choice = int(input('Commands to Perform Action:\n1 - Display Data \n2 - Update Data\n3 - Delete Particular Product Data\n4 - Sort Data\n5 - Enter more Product Data\n6 - Enter "no" to Exit\n:=>'))

        #*Display Data
        if choice == 1:

            dis_choice = input('Commands to Display Data:\n Enter "h1" to Display Data for First Half of the Year\n Enter "h2" to Display Data for Second Half of the Year\n Enter "bh" to Display Data for Both Halves of the Year\n Enter "Pd" to Display Data for Particular Product(NOT DONE YET)\n:=>')

            if dis_choice.lower() == 'h1':
                display_h1()

            elif dis_choice.lower() == 'h2':
                display_h2()

            elif dis_choice.lower() == 'bh':
                display_h1()
                display_h2()

            elif dis_choice.lower() == 'pd':
                display_prod()
                print('Work under process...')

            else:
                print('Oops some error')
        
        #*Update Data
        elif choice == 2:
            print('Not yet')
        
        #*Delete Data
        elif choice == 3:
            delete_prod()
        
        #*Again Enter Data
        elif choice == 5:
            print()
        
        elif choice == 6:
            break

        else:
            print('Error...')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
update_id = input("Enter the id no which u want to update")
n = int(input("Enter following nos. to update data from \n1-product id \n2-product name \n3-product cost price \n4-first half product selling price \n5-first half product sold"))
m = input("Enter ur new data")
for k in range(0, len(h1_table)):
    if h1_table[k][0] == update_id:
        if n == 1:
            h1_table[k][0] = m
        elif n == 2:
            h1_table[k][1] = m
        elif n == 3:
            h1_table[k][2] = m
        elif n == 4:
            h1_table[k][3] = m
        elif n == 5:
            h1_table[k][4] = m
        elif n > 5:
            print("Error...")
display_h1()

update_id2 = input("Enter the id no which u want to update")
q = int(input("Enter following nos. to update data from \n1-product id \n2-product name \n3-product cost price \n4-first half product selling price \n5-first half product sold"))
p = input("Enter ur new data")
for u in range(0, len(h2_table)):
    if h2_table[u][0] == update_id2:
        if q == 1:
            prod_id = p
        elif q == 2:
            prod_name = p
        elif q == 3:
            prod_cp = p
        elif q == 4:
            h2_prod_sp = p
        elif q == 5:
            h2_prod_sold = p
        elif q > 5:
            print("Enter valid no.")
display_h2()

