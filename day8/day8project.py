import sys
from pathlib import Path

def analyze_text_file(filepath):
    """
    Analyzes a text file and returns the number of lines and words.
    
    Args:
        filepath (str): Path to the text file to analyze
        
    Returns:
        tuple: (line_count, word_count)
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        IOError: If there's an error reading the file
    """
    try:
        # Convert string path to Path object
        file_path = Path(filepath)
        
        # Check if file exists
        if not file_path.is_file():
            raise FileNotFoundError(f"File not found: {filepath}")
            
        # Initialize counters
        line_count = 0
        word_count = 0
        
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Count lines (including empty ones)
                line_count += 1
                
                # Split line into words and count them
                # This splits on any whitespace and handles multiple spaces
                words = line.split()
                word_count += len(words)
                
        return line_count, word_count
        
    except UnicodeDecodeError:
        raise IOError("File is not readable as text")
    except Exception as e:
        raise IOError(f"Error reading file: {str(e)}")

def main():
    # Check if filename was provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
        
    try:
        filename = sys.argv[1]
        lines, words = analyze_text_file(filename)
        print(f"Number of lines: {lines}")
        print(f"Number of words: {words}")
        
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()