# COVER PAGE
# Name:      <José Luis Guillen González>
# Student ID:       <2630455>
# Group:     <IM 1-2>
# Course:    Programming fundamentals
# Topic:     Collections in Python: list, tuple and dict
# GitHub repository: <https://github.com/usuario/repositorio>

# EXECUTIVE SUMMARY

# Una lista (list) es una colección ordenada y mutable esto significa que se pueden agregar,
# quitar y cambiar elementos. Una tupla (tuple) es una colección ordenada pero inmutable:
# una vez creada sus elementos no pueden cambiar. Un diccionario (dict) guarda
# parejas clave-valor y permite buscar un dato directamente por su clave.
# Mutable significa que el objeto se puede modificar en su lugar (append,
# remove, sort); inmutable significa que para "cambiarlo" hay que crear otro.
# Los diccionarios asocian una clave descriptiva (nombre, id) con un valor
# (precio, lista de calificaciones, teléfono).

# PRINCIPLES AND BEST PRACTICES

# - Usar listas cuando se agregan o eliminan elementos con frecuencia.
# - Usar tuplas para datos que no deben cambiar (coordenadas, fechas, config).
# - Usar diccionarios cuando se busca información por una clave (nombre, id).
# - Evitar modificar una lista mientras se recorre con un for.
# - Usar nombres de clave descriptivos ("name", "age", "price").
# - Escribir código legible y mensajes claros para el usuario.

# MAIN MENU

# El programa pregunta qué problema ejecutar: 1-6, o 0 para ejecutar todos.
VALID_CHOICES = ["0", "1", "2", "3", "4", "5", "6"]

choice = input("Select problem (1-6, 0 = run all): ").strip()
if choice not in VALID_CHOICES:
    print("Error: invalid input")


# =============================================================================
# Problem 1: Shopping list basics (list operations)
# =============================================================================
# Description: The program starts with an initial list of products (strings)
#   created in the code. It reads a new product and appends it at the end of
#   the list, shows the number of items before and after, and checks whether
#   a given product is in the list (boolean found_item).
#
# Inputs:
#   - initial_items_text (list created in the code: orange, banana, apple,
#     pineapple)
#   - new_item (string; product to add)
#   - search_item (string; product to search)
#
# Outputs:
#   - "Starting item count:" <number of items before appending>
#   - "Initial items:" <initial list>
#   - "New item:" <new_item>
#   - "Items list:" <list after appending new_item>
#   - "Total items:" <len_list>
#   - "Item to search:" <search_item>
#   - "Found item:" true|false
#
# Validations:
#   - new_item and search_item are cleaned with strip() and must not be empty.
#   - Decision: the initial list is never empty because it is created in the
#     code.
#   - Decision: the search is case-sensitive ("Banana" does not match
#     "banana").
#
# Test cases:
#   1) Normal: new "grape", search "banana"
#        -> Items list: ['orange', 'banana', 'apple', 'pineapple', 'grape']
#           Total items: 5 / Found item: true
#   2) Border: new "grape", search "Banana" (different letter case)
#        -> Items list: ['orange', 'banana', 'apple', 'pineapple', 'grape']
#           Total items: 5 / Found item: false
#   3) Error: new_item = "   " (empty after strip())
#        -> Error: invalid input
if choice == "1" or choice == "0":
    print("\n--- Problem 1 ---")
    initial_items_text = ["orange", "banana", "apple", "pineapple"]
    print("Starting item count:", len(initial_items_text))
    print("Initial items:", initial_items_text)
    new_item = input("New item: ").strip()
    search_item = input("Item to search: ").strip()

    if new_item == "" or search_item == "":
        print("Error: invalid input")
    else:
        print("New item:", new_item)
        initial_items_text.append(new_item)
        print("Items list:", initial_items_text)
        print("Total items:", len(initial_items_text))
        print("Item to search:", search_item)
        found_item = False
        for item in initial_items_text:
            if search_item == item:
                found_item = True
                break
        print("Found item:", found_item)


# =============================================================================
# Problem 2: Points and distances with tuples
# =============================================================================
# Description: Represents two 2D points as tuples, computes the Euclidean
#   distance between them and builds a new tuple with the midpoint.
#
# Inputs:
#   - x1, y1, x2, y2 (float)
#
# Outputs:
#   - "Point A:" (x1, y1)
#   - "Point B:" (x2, y2)
#   - "Distance:" <distance>   (rounded to 2 decimals)
#   - "Midpoint:" (mx, my)
#
# Validations:
#   - The 4 inputs must be convertible to float (checked with try/except
#     ValueError). Text like "abc" or an empty input is an error.
#
# Test cases:
#   1) Normal: x1=0, y1=0, x2=3, y2=4
#        -> Distance: 5.0 / Midpoint: (1.5, 2.0)
#   2) Border: x1=2, y1=2, x2=2, y2=2 (same point)
#        -> Distance: 0.0 / Midpoint: (2.0, 2.0)
#   3) Error: x1="abc" -> Error: invalid input
if choice == "2" or choice == "0":
    print("\n--- Problem 2 ---")
    x1_text = input("x1: ").strip()
    y1_text = input("y1: ").strip()
    x2_text = input("x2: ").strip()
    y2_text = input("y2: ").strip()

    try:
        x1 = float(x1_text)
        y1 = float(y1_text)
        x2 = float(x2_text)
        y2 = float(y2_text)
        is_valid = True
    except ValueError:
        is_valid = False

    if not is_valid:
        print("Error: invalid input")
    else:
        point_a = (x1, y1)
        point_b = (x2, y2)
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

        print("Point A:", point_a)
        print("Point B:", point_b)
        print("Distance:", round(distance, 2))
        print("Midpoint:", midpoint)


# =============================================================================
# Problem 3: Product catalog with dictionary
# =============================================================================
# Description: A dictionary maps product names to unit prices. The program
#   reads a product and a quantity and computes the total to pay if the
#   product exists; otherwise it shows an error.
#
# Inputs:
#   - product_name (string; lookup is case-insensitive)
#   - quantity (int)
#
# Outputs:
#   - Always: "Catalog:" <product_prices> (initial catalog created in the code)
#   - Found: "Unit price:" <unit_price>, "Quantity:" <quantity>,
#            "Total:" <total_price>
#   - Not found: "Error: product not found"
#
# Validations:
#   - product_name not empty after strip().
#   - quantity is an int and quantity > 0.
#   - product_name must be a key of the dictionary (operator in).
#
# Catalog: apple 10.0, banana 5.5, orange 8.25, milk 22.0
#
# Test cases:
#   1) Normal: "apple", quantity 3
#        -> Unit price: 10.0 / Quantity: 3 / Total: 30.0
#   2) Border: "milk", quantity 1
#        -> Unit price: 22.0 / Quantity: 1 / Total: 22.0
#   3) Error: "apple", quantity 0 -> Error: invalid input
#      Error: "grape", quantity 2 -> Error: product not found
if choice == "3" or choice == "0":
    print("\n--- Problem 3 ---")
    product_prices = {
        "apple": 10.0,
        "banana": 5.5,
        "orange": 8.25,
        "milk": 22.0,
    }

    print("Catalog:", product_prices)

    product_name = input("Product name: ").strip().lower()
    print("Product name:", product_name)
    quantity_text = input("Quantity: ").strip()
    print("Quantity:", quantity_text)

    try:
        quantity = int(quantity_text)
        is_valid = product_name != "" and quantity > 0
    except ValueError:
        is_valid = False

    if not is_valid:
        print("Error: invalid input")
    elif product_name in product_prices:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity
        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", round(total_price, 2))
    else:
        print("Error: product not found")


# =============================================================================
# Problem 4: Student grades with dict and list
# =============================================================================
# Description: A dictionary maps each student name to a list of grades. The
#   program computes the average of the requested student and tells whether
#   the student passed (average >= 70.0).
#
# Inputs:
#   - student_name (string; lookup ignores letter case)
#
# Outputs:
#   - Always: "Students:" <grades> (initial dictionary created in the code)
#   - Found: "Grades:" <grades_list>, "Average:" <average>,
#            "Passed:" true|false
#   - Not found: "Error: student not found"
#
# Validations:
#   - student_name not empty after strip().
#   - student_name must be a key of the dictionary.
#   - The grades list must not be empty before computing the average
#     (otherwise "Error: no grades available").
#
# Data: Alice [90, 85, 100], Bob [60, 70, 65], Carla [70, 70, 70], Dan []
#
# Test cases:
#   1) Normal: "Alice"
#        -> Grades: [90.0, 85.0, 100.0] / Average: 91.67 / Passed: true
#   2) Border: "Carla" (average exactly 70.0)
#        -> Average: 70.0 / Passed: true
#      Border: "Dan" (empty list) -> Error: no grades available
#   3) Error: "Zoe" -> Error: student not found
if choice == "4" or choice == "0":
    print("\n--- Problem 4 ---")
    grades = {
        "Alice": [90.0, 85.0, 100.0],
        "Bob": [60.0, 70.0, 65.0],
        "Carla": [70.0, 70.0, 70.0],
        "Dan": [],
    }
    PASSING_GRADE = 70.0

    print("Students:", grades)

    student_name = input("Student name: ").strip().title()
    print("Student name:", student_name)

    if student_name == "":
        print("Error: invalid input")
    elif student_name not in grades:
        print("Error: student not found")
    elif len(grades[student_name]) == 0:
        print("Error: no grades available")
    else:
        grades_list = grades[student_name]
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= PASSING_GRADE

        print("Grades:", grades_list)
        print("Average:", round(average, 2))
        print("Passed:", str(is_passed).lower())


# =============================================================================
# Problem 5: Word frequency counter (list + dict)
# =============================================================================
# Description: Reads a sentence, converts it to lowercase, removes simple
#   punctuation, splits it into a list of words and builds a dictionary with
#   the frequency of each word. Shows the most common word.
#
# Inputs:
#   - sentence (string)
#
# Outputs:
#   - "Words list:" <words_list>
#   - "Frequencies:" <freq_dict>
#   - "Most common word:" <word> (on a tie, the first one found)
#
# Validations:
#   - sentence not empty after strip().
#   - Decision: the punctuation characters . , ; : ! ? are replaced by a
#     space with replace() before splitting.
#   - The words list must not be empty after cleaning.
#
# Test cases:
#   1) Normal: "The cat and the dog"
#        -> Words list: ['the', 'cat', 'and', 'the', 'dog']
#           Frequencies: {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
#           Most common word: the
#   2) Border: "Hello" -> Words list: ['hello'] / Frequencies: {'hello': 1}
#      Border: "Hi, hi! HI?" -> Frequencies: {'hi': 3} / Most common: hi
#   3) Error: "   " -> Error: invalid input
if choice == "5" or choice == "0":
    print("\n--- Problem 5 ---")
    sentence = input("Sentence: ").strip()

    clean_sentence = sentence.lower()
    for symbol in [".", ",", ";", ":", "!", "?"]:
        clean_sentence = clean_sentence.replace(symbol, " ")
    words_list = clean_sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        most_common_word = ""
        highest_count = 0
        for word, count in freq_dict.items():
            if count > highest_count:
                highest_count = count
                most_common_word = word

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)


# =============================================================================
# Problem 6: Simple contact book (dictionary CRUD)
# =============================================================================
# Description: A dictionary maps contact names to phone numbers (strings).
#   The user chooses one action (ADD, SEARCH or DELETE) and the program
#   creates/updates, looks up or removes the contact accordingly.
#
# Inputs:
#   - action_text (string: "ADD", "SEARCH" or "DELETE"; any letter case)
#   - name (string)
#   - phone (string; only for ADD)
#
# Outputs:
#   - Always: "Contacts:" <contacts> (initial dictionary created in the code)
#   - ADD:    "Contact saved:" name, phone
#   - SEARCH: "Phone:" <phone>  |  "Error: contact not found"
#   - DELETE: "Contact deleted:" name  |  "Error: contact not found"
#
# Validations:
#   - action_text is normalized to uppercase and must be one of the 3 options.
#   - name not empty after strip().
#   - For ADD: phone not empty after strip().
#
# Contacts: Alice 1234567890, Bob 5551234567, Carla 8341112233
#
# Test cases:
#   1) Normal: action "add", name "Eve", phone "5559876543"
#        -> Contact saved: Eve 5559876543
#   2) Border: action "ADD", name "Alice", phone "0000000000"
#        (existing contact is updated) -> Contact saved: Alice 0000000000
#      Border: action "SEARCH", name "Bob" -> Phone: 5551234567
#   3) Error: action "UPDATE" -> Error: invalid input
#      Error: action "DELETE", name "Zoe" -> Error: contact not found
if choice == "6" or choice == "0":
    print("\n--- Problem 6 ---")
    contacts = {
        "Alice": "1234567890",
        "Bob": "5551234567",
        "Carla": "8341112233",
    }
    VALID_ACTIONS = ["ADD", "SEARCH", "DELETE"]

    print("Contacts:", contacts)

    action_text = input("Action (ADD, SEARCH, DELETE): ").strip().upper()
    print("Action:", action_text)

    if action_text not in VALID_ACTIONS:
        print("Error: invalid input")
    else:
        name = input("Contact name: ").strip()
        print("Contact name:", name)
        if name == "":
            print("Error: invalid input")
        elif action_text == "ADD":
            phone = input("Phone: ").strip()
            print("Phone:", phone)
            if phone == "":
                print("Error: invalid input")
            else:
                contacts[name] = phone
                print("Contact saved:", name, phone)
        elif action_text == "SEARCH":
            phone = contacts.get(name)
            if phone is None:
                print("Error: contact not found")
            else:
                print("Phone:", phone)
        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")


# =============================================================================
# CONCLUSIONS (CONCLUSIONES)
# =============================================================================
# Las listas conviene usarlas cuando el conjunto de datos crece o se reduce,
# porque append(), insert(), remove() y pop() permiten modificarlas con
# flexibilidad (Problem 1). Las tuplas son útiles para datos que no deben
# cambiar, como las coordenadas del Problem 2, ya que su inmutabilidad evita
# modificaciones accidentales. Los diccionarios facilitan búsquedas rápidas
# por clave sin recorrer toda la colección, como en el catálogo (Problem 3)
# y la agenda (Problem 6). Un patrón común fue el diccionario de listas
# (Problem 4), que asocia a cada estudiante con varias calificaciones y el
# uso de un diccionario como contador de frecuencias (Problem 5). También
# aprendí que validar entradas antes de procesarlas (claves existentes,
# listas vacías, tipos correctos) evita errores en tiempo de ejecución.

# =============================================================================
# REFERENCES (REFERENCIAS)
# =============================================================================
# References:
# 1) Python Software Foundation. Python documentation - Built-in Types: list,
#    tuple, dict. https://docs.python.org/3/library/stdtypes.html
# 2) Python Software Foundation. The Python Tutorial - Data Structures.
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) van Rossum, G., Warsaw, B., Coghlan, A. PEP 8 - Style Guide for Python
#    Code. https://peps.python.org/pep-0008/
# 4) Downey, A. Think Python (3rd ed.). O'Reilly Media.
# 5) Real Python. Lists and Tuples in Python.
#    https://realpython.com/python-lists-tuples/