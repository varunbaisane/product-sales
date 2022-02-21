print("+--------------------------+")
print('| Product Sales Management |')
print("+--------------------------+")
print("\nWelcome to Our Project :)")
h1_table = []
h2_table = []
col_heading = ['PRODUCT ID', 'NAME', 'COST PRICE', 'SELLING PRICE', 'UNITS SOLD', 'TOTAL AMOUNT', 'PROFIT', 'PROFIT %']
h1_table.append(col_heading)
h2_table.append(col_heading)

def enter_data():
    data_choice = 'yes'
    while data_choice.lower() == 'yes':
        print('\nEnter the following details about your product :- ')
        prod_id = input('\t\ti)Enter the ID of the Product:=> ')
        prod_name = input('\t\tii)Enter the Name of your Product:=> ')
        prod_cp = float(input('\t\tiii)Enter the Cost Price of the Product:=> '))
        prod_cp = round(prod_cp, 2)

        print('\nI] Now Enter the values for First Half of the Year: ')
        h1_prod_sp = float(input('\t\ti)Enter the Selling Price of the Product:=> '))
        h1_prod_sp = round(h1_prod_sp, 2)
        h1_prod_sold = int(input('\t\tii)Enter the number of Units Sold:=> '))

        print('\nII] Now Enter the values for Second Half of the Year:')
        h2_prod_sp = float(input('\t\ti)Enter the Selling Price of the Product:=> '))
        h2_prod_sp = round(h2_prod_sp, 2)
        h2_prod_sold = int(input('\t\tii)Enter the number of Units Sold:=> '))

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

        data_choice = input('\n\nWant to Enter data for next Product?\n\t\t"Yes" - Enter Data\n\t\t"Any key/No" - Exit:\n\t\t:=> ')

def limit_prod():
    for i in range(len(h1_table)):
        if len(h1_table[i][1]) > 10:
            h1_table[i][1] = h1_table[i][1][:8] + '...'
    for i in range(len(h2_table)):
        if len(h2_table[i][1]) > 10:
            h2_table[i][1]=h2_table[i][1][:8] + '...'

def display(table_list):
    table_len = -1
    for row in range(len(table_list)):
        for ind in range(len(table_list[row])):
            if len(str(table_list[row][ind])) > table_len:
                table_len = len(str(table_list[row][ind]))

    limit_prod()
    for row in range(len(table_list)):
        for col in range(len(table_list[row])):
            print('| {:<{}} '.format(table_list[row][col], table_len), end=' |')
        print()
                
def display_h1():
    h1_len = -1
    for row in range(len(h1_table)):
        for ind in range(8):
            if len(str(h1_table[row][ind])) > h1_len:
                h1_len = len(str(h1_table[row][ind]))

    print('\n\n+----------------------+')
    print('| 1ST HALF OF THE YEAR |')
    print('+----------------------+\n')
    limit_prod()
    for row in range(len(h1_table)):
        for col in range(8):
            print('| {:<{}} '.format(h1_table[row][col], h1_len), end=' |')
        print()

def display_h2():
    h2_len = -1
    for row in range(len(h2_table)):
        for ind in range(8):
            if len(str(h2_table[row][ind])) > h2_len:
                h2_len = len(str(h2_table[row][ind]))
    print('\n\n+----------------------+')
    print('| 2ND HALF OF THE YEAR |')
    print('+----------------------+\n')
    limit_prod()
    for row in range(len(h2_table)):
        for col in range(8):
            print('| {:<{}} '.format(h2_table[row][col], h2_len), end=' |')
        print()

def display_prod():
    print('\nProduct IDs:')
    for k in range(len(h1_table)-1):
        print(h1_table[k+1][0])
    prod_choice = input('\nEnter the ID of the Product for Display:=> ')
    head_col = ['SELLING PRICE', 'UNITS SOLD', 'TOTAL AMOUNT', 'PROFIT', 'PROFIT %']
    details_head = ['Product ID', 'Product Name', 'Product Cost Price']
    print() 
    prod_details = []
    prod_list = []
    prod_list.append([])
    prod_list[0].extend([' ', '1st Half', '2nd Half'])
    for i in range(len(h1_table)):
        if prod_choice == h1_table[i][0]:
            for y in range(3):
                prod_details.append([])
                prod_details[y].append(details_head[y])
                prod_details[y].append(h1_table[i][y])
            for x in range(5):
                prod_list.append([])
                prod_list[x+1].append(head_col[x])
                prod_list[x+1].append(h1_table[i][x+3])
                prod_list[x+1].append(h2_table[i][x+3])
            break
    print()
    print('+-----------------+')
    print('| PRODUCT DETAILS |')
    print('+-----------------+')
    print()
    display(prod_details)
    print()
    display(prod_list)
    print()

def update_data():
    print('\nProduct IDs:')
    for k in range(len(h1_table)-1):
        print(h1_table[k+1][0])
    update_id = input("\nEnter the ID of the  Product which you want to Update\n:=> ")
    ud_choice=int(input("Enter command for Updatation: \n\t1 - Product ID \n\t2 - Product Name \n\t3 - Product Cost Price \n\t4 - Product Selling Price \n\t5 - Products Sold \n\t:=> "))
    for k in range(len(h1_table)):
        if h1_table[k][0] == update_id:
            if ud_choice == 1:
                h1_table[k][0] = input('Enter New Product ID:=> ')
                h2_table[k][0] = h1_table[k][0]
                break
            elif ud_choice == 2:
                h1_table[k][1] = input('Enter New Product Name:=> ')
                h2_table[k][1] = h1_table[k][1]
                break
            elif ud_choice == 3:
                h1_table[k][2] = input('Enter New Product Cost Price:=> ')
                h2_table[k][2] = h1_table[k][2]
                h1_table[k][6] = (h1_table[k][3] * h1_table[k][4]) - (h1_table[k][4] * h1_table[k][2])
                h1_table[k][7] = round((h1_table[k][6])/(h1_table[k][4] * h1_table[k][2]) * 100,2)
                h2_table[k][6] = (h2_table[k][3] * h2_table[k][4]) - (h2_table[k][4] * h2_table[k][2])
                h2_table[k][7] = round((h2_table[k][6])/(h2_table[k][4] * h2_table[k][2]) * 100,2)
                break
            elif ud_choice==4:
                ud_yr_choice = int(input('Enter:\n\t1 - First Half\n\t2 - Second Half'))
                if ud_yr_choice == 1:
                    h1_table[k][3]=input('Enter New Product Selling Price:=> ')
                    h1_table[k][5] = h1_table[k][4] * h1_table[k][3]
                    h1_table[k][6] = h1_table[k][5] - (h1_table[k][4] * h1_table[k][2])
                    h1_table[k][7] = round(h1_table[k][6] - (h1_table[k][4] * h1_table[k][2]), 2)
                    break
                elif ud_yr_choice == 2:
                    h2_table[k][3]=input('Enter New Product Selling Price:=> ')
                    h2_table[k][5] = h2_table[k][4] * h2_table[k][3]
                    h2_table[k][6] = h2_table[k][5] - (h2_table[k][4] * h2_table[k][2])
                    h2_table[k][7] = round(h2_table[k][6] - (h2_table[k][4] * h2_table[k][2]), 2)
                    break
            elif ud_choice==5:
                ud_yr_choice = int(input('Enter:\n\t1 - First Half\n\t2 - Second Half'))
                if ud_yr_choice == 1:
                    h1_table[k][4] = input('Enter New Number of Products Sold:=> ')
                    h1_table[k][5] = h1_table[k][4] * h1_table[k][3]
                    h1_table[k][6] = h1_table[k][5] - (h1_table[k][4] * h1_table[k][2])
                    h1_table[k][7] = round(h1_table[k][6] - (h1_table[k][4] * h1_table[k][2]), 2)
                    break
                elif ud_yr_choice == 2:
                    h2_table[k][4]=input('Enter New Number of Products Sold:=> ')
                    h2_table[k][5] = h2_table[k][4] * h2_table[k][3]
                    h2_table[k][6] = h2_table[k][5] - (h2_table[k][4] * h2_table[k][2])
                    h2_table[k][7] = round(h2_table[k][6] - (h2_table[k][4] * h2_table[k][2]), 2)
                    break
    print('\nAfter Updatation:\n')
    display_h1()
    display_h2()
    print()

def delete_prod():
    print('\nProduct IDs:')
    for k in range(len(h1_table)-1):
        print(h1_table[k+1][0])
    del_id = input("Enter the Product ID which you want to Delete: ")
    print('\nAfter Deletion: ')
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
    h1_copy = h1_table.copy()
    for x in range(1,len(h1_copy)-1):
        if float(h1_copy[x][2]) > float(h1_copy[x+1][2]):
            h1_copy[x],h1_copy[x+1] = h1_copy[x+1],h1_copy[x]
    display(h1_copy)  

choice = 5
while choice == 5:
    enter_data()

    choice = 1
    while choice != 5:
        choice = int(input('\nCommands to Perform Action:\n\t\t1 - Display Data \n\t\t2 - Update Data\n\t\t3 - Delete Particular Product Data\n\t\t4 - Sort Data according to Cost Price\n\t\t5 - Enter more Product Data\n\t\t6 - Exit\n\t\t:=> '))

        if choice == 1:

            dis_choice = input('\n\nCommands to Display Data:\n\t\tEnter "h1" - Display Data for First Half of the Year\n\t\tEnter "h2" -  Display Data for Second Half of the Year\n\t\tEnter "bh" - Display Data for Both Halves of the Year\n\t\tEnter "Pd" - Display Data for Particular Product\n\t\t:=> ')

            if dis_choice.lower() == 'h1':
                display_h1()

            elif dis_choice.lower() == 'h2':
                display_h2()

            elif dis_choice.lower() == 'bh':
                display_h1()
                display_h2()

            elif dis_choice.lower() == 'pd':
                display_prod()

            else:
                print('Enter valid command.')
        
        elif choice == 2:
            update_data()
        
        elif choice == 3:
            delete_prod()

        elif choice == 4:
            sort_data()
        
        elif choice == 5:
            print()
        
        elif choice == 6:
            print('Thank You :)')
            break

        else:
            print('Enter valid command.')