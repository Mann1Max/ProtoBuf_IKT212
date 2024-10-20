from proto.puzzle_input_pb2 import PuzzleInput

def read_binary_input(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()

    puzzle_input = PuzzleInput()
    puzzle_input.ParseFromString(data)
    return puzzle_input

if __name__ == "__main__":
    puzzle_data = read_binary_input("puzzle_input.bin")
    for puzzle in puzzle_data.puzzles:
        print(f"Puzzle ID: {puzzle.puzzle_id}")
        print(f"Width: {puzzle.width}, Height: {puzzle.height}")
        for i, row in enumerate(puzzle.rows):
            print(f"Row {i + 1}: symbols={row.symbols}, end_value={row.end_value}")
