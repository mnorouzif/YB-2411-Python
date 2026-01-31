class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""
    
    def read_file(self):
        """Reads the file and stores the content."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
            print("File content:")
            print(self.content)
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
    
    def count_asterisks(self):
        if not self.content:
            print("Warning: File content is empty. Did you call read_file()?")
            return 0
        
        count = self.content.count('*')
        print(f"Number of '*' characters: {count}")
        return count



if __name__ == "__main__":
    F_processor = FileProcessor('.\Week3\demo_file.txt') 
    F_processor.read_file()
    F_processor.count_asterisks()
