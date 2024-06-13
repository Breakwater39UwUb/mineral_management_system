"""
1. make_employee_id(department: str, position: str, id_length: int = 3)
2. make_client_id()
3. make_supplier_id()
4. make_category_id()
5. make_warehouse_id()
6. make_item_id()
7. make_order_id()
8. make_order_details_id()
9. make_bill_id()
10. test_all_functions()
11. random_emp_id()
"""
import random
import string
from datetime import datetime
from my_packs.business import DEPS, DEP_NAME

def make_employee_id(department: str,
                     position: str,
                     id_length: int = 3):
    """
    This function generates an employee ID based on the department and position.

    Parameters:
    department: The department of the employee. It should be abbreviated in 1~3 characters.
    position: The position of the employee. It should be abbreviated in 1~3 characters.
    id_length: The length of the random alphanumeric string in the employee ID. Default is 3.

    Returns:
    employee_id: The generated employee ID in the format 'DEP-POS-ID'.

    Raises:
    ValueError: If the department or position is not abbreviated in 1~3 characters.
    ValueError: If the id_length is not a positive integer.

    Format in `DEP-POS-ID`
    1. `DEP`: The employee department abbreviated in 1~3 characters
    2. `POS`: The employee position abbreviated in 1~3 characters
    3. `ID`: A 3-character long random uppercase alphanumeric string, `[A-Z0-9]{3}`.

    Example:
    >>> make_employee_id('HR', 'Manager')
    'HR-MN-AB0'
    """

    if len(department) > 3:
        raise ValueError(f'Department must be abbreviated in 1~3 characters\nYour input: {department}')

    if len(position) > 3:
        raise ValueError(f'Position must be abbreviated in 1~3 characters\nYour input: {position}')
    
    # Check if id_length is a positive integer
    if not isinstance(id_length, int) or id_length <= 0:
        raise ValueError(f'id_length must be a positive integer.\nYour input: {id_length}')

    department = department.upper()
    position = position.upper()

    # Generate a random ID
    employee_id = ''.join(random.choices(string.ascii_uppercase+string.digits, k=id_length))

    # Add the department and position to the employee ID.
    employee_id = f'{department}-{position}-{str(employee_id)}'

    return employee_id

def make_employee_email(emp_id: str,
                        third_level: str='',
                        second_leve: str='company',
                        top_level: str='com'):
    email = emp_id + '@'
    if third_level != '':
        email += f'{third_level}.'
    if second_leve != '':
        email += f'{second_leve}.'
    if top_level != '':
        email += f'{top_level}'

    return email

def make_employee_data(emp_name: str,
                       emp_dep: str,
                       emp_pos: str,
                       emp_id: str=None):
    if emp_id is None:
        emp_id = make_employee_id(emp_dep, emp_pos)
    emp_email = make_employee_email(emp_id)

    return emp_id, emp_name, emp_dep, emp_pos, emp_email

def make_client_id(prefix: str = 'CLIENT',
                   id_length: int = 3):
    """
    This function generates a client ID.

    Parameters:
    prefix: A string representing the prefix of the client ID. Default is 'CLIENT'.
    id_length: An integer representing the length of the random alphanumeric string in the client ID. Default is 3.
    
    Returns: 
    client_id: A string representing the generated client ID.

    Raises:
    ValueError: If the id_length is not a positive integer.

    Format in `Client-ID`.
    1. `Client` is a 6-character uppercase letter constant `CLIENT`.
    2. `ID` is a 3-character long random uppercase alphanumeric string, `[A-Z0-9]{3}`.

    The function generates a client ID by concatenating the constant
    'CLIENT' with a randomly generated 3-character alphanumeric string.

    Example:
    >>> make_client_id()
    'SUPPLIER-ABCD'
    """

    # Check if id_length is a positive integer
    if not isinstance(id_length, int) or id_length <= 0:
        raise ValueError(f'id_length must be a positive integer.\nYour input: {id_length}')

    # Generate the client ID
    id = ''.join(random.choices(string.ascii_uppercase+string.digits, k=id_length))
    client_id = prefix + '-' + id

    return client_id

def make_supplier_id(prefix: str = 'SUPPLIER',
                     id_length: int = 2):
    """
    This function generates a supplier ID.

    Format in `Supplier-ID`.
    格式為 `Supplier-ID`
    長度為 10 個字元, 由 6 個字元之大寫字母 `SUPPLIER` 與 4 個隨機的大寫英數字串, `[A-Z0-9]{4}` 組成.

    Parameters:
    prefix: A string representing the prefix of the supplier ID. Default is 'SUPPLIER'.
    id_length: An integer representing the length of the random alphanumeric string in the supplier ID. Default is 4.

    Returns:
    supplier_id: A string representing the generated supplier ID.

    Raises:
    ValueError: If the id_length is not a positive integer.

    Example:
    >>> make_supplier_id()
    'SUPPLIER-A0'
    """

    # Check if id_length is a positive integer
    if not isinstance(id_length, int) or id_length <= 0:
        raise ValueError(f'id_length must be a positive integer.\nYour input: {id_length}')

    # Generate the supplier ID
    id = ''.join(random.choices(string.ascii_uppercase+string.digits, k=id_length))
    supplier_id = prefix + '-' + id

    return supplier_id

def make_category_id(prefix: str = 'CAT',
                     id_length: int = 3):
    """
    This function generates a category ID.

    Parameters:
    prefix: The prefix for the category ID. Default is 'CAT'.
    id_length: The length of the random digits in the category ID. Default is 3.

    Returns:
    cat_id: The generated category ID in the format 'CAT-XXX', where XXX is a 3-digit random number.

    Raises:
    ValueError: If the id_length is not a positive integer.

    Example:
    >>> make_category_id()
    'CAT-123'
    """

    # Check if id_length is a positive integer
    if not isinstance(id_length, int) or id_length <= 0:
        raise ValueError(f'id_length must be a positive integer.\nYour input: {id_length}')

    # Generate the category ID
    id = ''.join(random.choices(string.digits, k=id_length))
    cat_id = prefix + '-' + id

    return cat_id

def make_warehouse_id(prefix: str = 'WH',
                      id_length: int = 4):
    """
    This function generates a warehouse ID.

    Parameters:
    prefix: The prefix for the warehouse ID. Default is 'WH'.
    id_length: The length of the random digits in the warehouse ID. Default is 4.

    Returns:
    warehouse_id: The generated warehouse ID in the format 'WH-XXXX', where XXXX is a 4-digit random number.

    Raises:
    ValueError: If the id_length is not a positive integer.

    Example:
    >>> make_warehouse_id()
    'WH-1234'
    """

    # Check if id_length is a positive integer
    if not isinstance(id_length, int) or id_length <= 0:
        raise ValueError(f'id_length must be a positive integer.\nYour input: {id_length}')

    # Generate the warehouse ID
    id = ''.join(random.choices(string.digits, k=id_length))
    warehouse_id = prefix + '-' + id
    return warehouse_id

def make_item_id():
    """
    This function generates an item ID.

    The item ID is a combination of a 5-character uppercase alphanumeric prefix and a 10-character numeric postfix.
    The prefix is randomly generated using the `random.choices` function from the `random` module,
    and the postfix is also randomly generated using the `random.choices` function.

    Parameters:
    None

    Returns:
    item_id: A string representing the generated item ID. The format of the item ID is 'PREFIXPOSTFIX',
         where 'PREFIX' is a 5-character uppercase alphanumeric string and 'POSTFIX' is a 10-character numeric string.

    Example:
    >>> make_item_id()
    'ABCDE1234567890'
    """

    prefix = ''.join(random.choices(string.ascii_uppercase, k=5))
    postfix = ''.join(random.choices(string.digits, k=10))
    item_id = f'{prefix}{postfix}'

    return item_id

def make_order_id(id_length: int = 3):
    """
    This function generates an order ID.

    The order ID is a combination of a date in the format 'YYYYMMDD' and a randomly generated alphanumeric string.
    The date is obtained using the `datetime.now().strftime('%Y%m%d')` method.
    The alphanumeric string is generated using the `random.choices` function from the `random` module.

    Parameters:
    id_length: The length of the randomly generated alphanumeric string.

    Returns:
    order_id: A string representing the generated order ID. The format of the order ID is 'YYYYMMDD-RANDOMSTRING',
         where 'YYYYMMDD' is the current date and 'RANDOMSTRING' is a randomly generated alphanumeric string.

    Raises:
    ValueError: If the id_length is not a positive integer.

    Example:
    >>> make_order_id(5)
    '20220101-ABCDE'
    """

    # Check if id_length is a positive integer
    if not isinstance(id_length, int) or id_length <= 0:
        raise ValueError(f'id_length must be a positive integer.\nYour input: {id_length}')

    date = datetime.now().strftime('%Y%m%d')
    id = random.choices(string.ascii_letters+string.digits, k=id_length)

    order_id = date + '-' + ''.join(id)

    return order_id

def make_order_details_id(order_id: str,
                          detail_page: int=0) -> str:
    """
    This function generates a unique order details ID.

    The order details ID is a combination of the order ID and the detail page number.
    It is used to uniquely identify each order detail record in a database.

    Parameters:
    order_id: The unique identifier of the order.
    detail_page: The page number of the order details. Default is 0.

    Returns:
    detail_id: A string representing the generated order details ID.
         The format of the order details ID is 'ORDER_ID-DETAIL_PAGE',
         where ORDER_ID is the unique identifier of the order and DETAIL_PAGE is the page number of the order details.
    
    Raises:
        ValueError: If the detail_page is not a positive integer.

    Example:
    >>> make_order_details_id('ORD-123', 1)
    'ORD-123-01'
    """

    # Check if id_length is a positive integer
    if not isinstance(detail_page, int) or detail_page < 0:
        raise ValueError(f'id_length must be a positive integer.\nYour input: {detail_page}')

    # Fill leading 0
    detail_page = str(detail_page).zfill(2)
    detail_id = order_id + '-' + detail_page

    return detail_id

def make_bill_id(id_length: int = 6) -> str:
    """
    This function generates a unique bill ID.

    The bill ID is a combination of a 3-character alphanumeric prefix and a 6-digit numeric ID.
    The prefix is randomly generated using the `random.choices` function from the `random` module,
    and the numeric ID is also randomly generated using the `random.choices` function.

    Parameters:
    id_length: The length of the numeric ID. Default is 6.

    Returns:
    bill_id: A string representing the generated bill ID. The format of the bill ID is 'PREFIX-ID',
         where 'PREFIX' is a 3-character alphanumeric string and 'ID' is a 6-digit numeric string.

    Raises:
    ValueError: If the id_length is not a positive integer.

    Example:
    >>> make_bill_id(8)
    'ABC-12345678'
    """

    # Check if id_length is a positive integer
    if not isinstance(id_length, int) or id_length <= 0:
        raise ValueError(f'id_length must be a positive integer.\nYour input: {id_length}')

    prefix = ''.join(random.choices(string.ascii_letters+string.digits, k=3))
    id = ''.join(random.choices(string.digits, k=id_length))

    bill_id = prefix + '-' + id

    return bill_id

def test_all_functions():
    """
    This function tests all the ID generating functions.
    It generates IDs for employee, client, supplier, category, warehouse, item, order, order details, and bill.
    The generated IDs are printed for verification.

    Parameters:
    None

    Returns:
    None
    """

    orders = []

    print('make_employee_id')
    for i in range(0, 5):
        print(make_employee_id('ASP', 'AD'))
    print()

    print('make_client_id')
    for i in range(0, 5):
        print(make_client_id())
    print()

    print('make_supplier_id')
    for i in range(0, 5):
        print(make_supplier_id())
    print()

    print('make_category_id')
    for i in range(0, 5):
        print(make_category_id())
    print()

    print('make_warehouse_id')
    for i in range(0, 5):
        print(make_warehouse_id())
    print()

    print('make_item_id')
    for i in range(0, 5):
        print(make_item_id())
    print()

    print('make_order_id')
    for i in range(0, 5):
        orders.append(make_order_id())
        print(orders[i])
    print()

    print('make_order_details_id')
    for i in range(0, 5):
        print(make_order_details_id(orders[i]))
    print()

    print('make_bill_id')
    for i in range(0, 5):
        print(make_bill_id())
    print()

def test_random_dep_pos(is_print: bool=False):

    dep, P = random.choice(list(DEPS.items()))
    pos = random.choice(list(P.keys()))
    dep_name = DEP_NAME[dep]
    pos_name = P[pos]

    if is_print:
        print(dep, pos)
        print(dep_name, '/', pos_name)
    return dep, pos