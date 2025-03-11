import string

def generate_matrix(key):

    key = key.upper().replace(" ", "").replace("J", "I")
    seen = set()
    matrix = []
    

    for char in key:
        if char not in seen and char in string.ascii_uppercase:
            matrix.append(char)
            seen.add(char)
    
   
    for char in string.ascii_uppercase:
        if char != "J" and char not in seen:
            matrix.append(char)
    
    return matrix

def prepare_text(text):
 
    text = text.upper().replace(" ", "").replace("J", "I")
    processed = []
    i = 0
    
    while i < len(text):
       
        if text[i] not in string.ascii_uppercase:
            i += 1
            continue
        
       
        a = text[i]
        
       
        j = i + 1
        while j < len(text) and text[j] not in string.ascii_uppercase:
            j += 1
        
        if j >= len(text):
            b = "X"
        else:
            b = text[j]
            if a == b:
                b = "X"
                j = i  
        
        processed.extend([a, b])
        i = j + 1 if a != b else i + 1
    

    if len(processed) % 2 != 0:
        processed.append("X")
    
    return processed

def get_positions(matrix):
    return {char: (idx//5, idx%5) for idx, char in enumerate(matrix)}

def transform_pair(a, b, positions, mode):
    row1, col1 = positions[a]
    row2, col2 = positions[b]
    
    
    if row1 == row2:
        offset = 1 if mode == "E" else -1
        return (
            matrix[row1*5 + (col1 + offset) % 5],
            matrix[row2*5 + (col2 + offset) % 5]
        )
    
  
    if col1 == col2:
        offset = 1 if mode == "E" else -1
        return (
            matrix[((row1 + offset) % 5)*5 + col1],
            matrix[((row2 + offset) % 5)*5 + col2]
        )
    
 
    return (
        matrix[row1*5 + col2],
        matrix[row2*5 + col1]
    )

def playfair_operation(matrix, text, mode):
    positions = get_positions(matrix)
    result = []
    
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        new_a, new_b = transform_pair(a, b, positions, mode)
        result.extend([new_a, new_b])
    
    return "".join(result)


keyword = input("Enter keyword: ").strip()
matrix = generate_matrix(keyword)

print("\nPlayfair Matrix:")
for row in [matrix[i*5:(i+1)*5] for i in range(5)]:
    print(" ".join(row))

mode = input("\nChoose mode (E)ncrypt/(D)ecrypt: ").upper()
while mode not in ("E", "D"):
    mode = input("Invalid choice! Enter E/D: ").upper()

message = input("Enter message: ").strip()
processed_text = prepare_text(message)
result = playfair_operation(matrix, processed_text, mode)

print(f"\nFinal result: {result}")