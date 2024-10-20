from proto.puzzle_input_pb2 import PuzzleInput

def text_to_binary_input(file_path: str) -> bytes:
    # Read the entire content from the input text file
    with open(file_path, "r", encoding='utf-8') as f:
        input_text = f.read()

    lines = input_text.strip().split("\n")
    puzzle_input = PuzzleInput()
    puzzle_count_line = lines[0].strip()

    # Verify if the first line starts with "puzzles" and has a number after it
    if not puzzle_count_line.startswith("puzzles"):
        raise ValueError("Input must start with 'puzzles <count>'")

    try:
        puzzle_count = int(puzzle_count_line.split()[1])
    except (IndexError, ValueError):
        raise ValueError("Invalid puzzle count format on the first line.")

    index = 1
    while index < len(lines):
        # Find the next "size" line to identify a new puzzle
        while index < len(lines) and not lines[index].strip().startswith("size"):
            index += 1
        
        if index >= len(lines):
            break  # End of file

        # Process the size line
        size_line = lines[index].strip()
        try:
            width, height = map(int, size_line.split()[1].split("x"))
        except (IndexError, ValueError):
            raise ValueError(f"Invalid size format '{size_line}'. Expected 'WxH'.")

        puzzle = puzzle_input.puzzles.add()
        puzzle.puzzle_id = len(puzzle_input.puzzles)
        puzzle.width = width
        puzzle.height = height

        # Move to the next line, which is a metadata row we should skip
        index += 2  # Skip the "size" line and move to the first row of the puzzle

        # Read the puzzle grid rows
        for y in range(height):
            if index >= len(lines):
                raise ValueError("Unexpected end of input: not enough rows for the puzzle grid.")

            row = puzzle.rows.add()
            symbols = lines[index].strip().split()
            
            # Extract the symbols and the end value
            if len(symbols) < width + 1:
                raise ValueError(f"Expected at least {width + 1} symbols on row {y + 1} but got {len(symbols)}. Content: {symbols}")
            
            # The last element is the end value, the rest are symbols
            end_value = int(symbols[-1])
            row.symbols.extend(symbols[:-1])
            row.end_value = end_value

            # Diagnostics: Print out what we parsed for each row
            print(f"Reading row {y + 1}: symbols={symbols[:-1]}, end_value={end_value}")
            
            index += 1  # Move to the next line

        # Move to the next puzzle's size line, and also skip any blank lines in between
        while index < len(lines) and lines[index].strip() == "":
            index += 1

        # Debug: Print transition to the next puzzle
        print(f"Finished reading puzzle {puzzle.puzzle_id}. Moving to the next puzzle...")

    # Check if we got the expected number of puzzles
    if len(puzzle_input.puzzles) != puzzle_count:
        print(f"Warning: Expected {puzzle_count} puzzles, but found {len(puzzle_input.puzzles)}.")
        
    return puzzle_input.SerializeToString()

# Example usage
if __name__ == "__main__":
    input_file_path = "puzzle_input.txt"
    
    try:
        binary_data = text_to_binary_input(input_file_path)
        with open("puzzle_input.bin", "wb") as f:
            f.write(binary_data)
    except ValueError as e:
        print(f"Error: {e}")
