import time
import random

def typing_speed_test(sample_text):
    print("Welcome to Typing Speed Test!")
    print("Type the following text:")
    print(sample_text)
    
    input("Press Enter to start typing...")
    
    start_time = time.time()
    typed_text = input("Type the text: ")
    end_time = time.time()

    typed_words = typed_text.split()
    example_words = sample_text.split()

    correct_words = 0
    for typed_word, example_word in zip(typed_words, example_words):
        if typed_word == example_word:
            correct_words += 1
    
    total_words = len(example_words)
    
    print(f"Number of correct words: {correct_words}/{total_words}")
    
    elapsed_time = end_time - start_time
    words_typed = len(sample_text.split())
    words_per_minute = int((words_typed / elapsed_time) * 60)
    
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Words typed: {words_typed}")
    print(f"Your typing speed: {words_per_minute} words per minute")

if __name__ == "__main__":
    sample_texts = [
        "The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog ",
        "Pack my box with five dozen liquor jugs Pack my box with five dozen liquor jugs Pack my box with five dozen liquor jugs ",
        "How razorback-jumping frogs can level six piqued gymnasts! How razorback-jumping frogs can level six piqued gymnasts!",
        "The five boxing wizards jump quickly The five boxing wizards jump quickly The five boxing wizards jump quickly ",
        "The quick onyx goblin jumps over the lazy dwarf The quick onyx goblin jumps over the lazy dwarf The quick onyx goblin jumps over the lazy dwarf "
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla aliquet facilisis lacinia. Sed justo risus, ornare eget elementum ac, laoreet nec risus. Nulla id fermentum quam. Suspendisse faucibus justo nulla"
    ]
    sample_text = random.choice(sample_texts)
    typing_speed_test(sample_text)