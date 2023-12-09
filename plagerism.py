from difflib import SequenceMatcher

def calculate_similarity(text1, text2):
    # Calculate the similarity ratio between two texts
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    return similarity_ratio

def check_plagiarism(file1_path, file2_path, threshold=0.8):
    # Read the contents of the files
    with open(file1_path, 'r', encoding='utf-8') as file1:
        text1 = file1.read()

    with open(file2_path, 'r', encoding='utf-8') as file2:
        text2 = file2.read()

    # Calculate the similarity ratio
    similarity_ratio = calculate_similarity(text1, text2)

    # Check if the similarity ratio is above the threshold
    if similarity_ratio >= threshold:
        print(f"Plagiarism detected! Similarity ratio: {similarity_ratio:.2f}")
    else:
        print(f"No plagiarism detected. Similarity ratio: {similarity_ratio:.2f}")

# Example usage
file1_path = 'C:\Users\varsh\OneDrive\Documents\plagearism file1.txt'
file2_path = 'C:\Users\varsh\OneDrive\Documents\plagearism file2.txt'
check_plagiarism(file1_path, file2_path)
