from transformers import pipeline
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the text generation pipeline with GPT-2
logger.info("Loading GPT-2 model...")
try:
    generator = pipeline('text-generation', model='gpt2')
except Exception as e:
    logger.error(f"Failed to load GPT-2 model: {e}")
    print("Error: Could not load the GPT-2 model. Check your internet connection and try again.")
    exit(1)

# Function to generate text
def generate_text(prompt, max_length=300):
    try:
        result = generator(
            prompt,
            max_length=max_length,
            num_return_sequences=1,
            truncation=True,
            temperature=0.7,         # Lowered temperature for more focused output
            top_k=40,               # Adjusted top_k for balanced diversity
            top_p=0.85,             # Lowered top_p for more coherence
            no_repeat_ngram_size=4, # Kept to reduce repetition
            do_sample=True,         # Ensure diverse sampling
            pad_token_id=50256      # GPT-2's end-of-text token to help with natural endings
        )
        return result[0]['generated_text']
    except Exception as e:
        logger.error(f"Error generating text: {e}")
        return "Error: Could not generate text."

# Main loop
if __name__ == "__main__":
    print("AI Text Generator with GPT-2")
    print("Enter a prompt to generate text (e.g., 'Once upon a time, in a magical kingdom, there lived a brave princess who') or type 'exit' to quit.")
    while True:
        prompt = input("Prompt: ")
        if prompt.lower() == 'exit':
            break
        if not prompt.strip():
            print("Please enter a non-empty prompt.")
            continue
        logger.info(f"Generating text for prompt: {prompt}")
        generated_text = generate_text(prompt, max_length=300)
        print(f"Generated Text: {generated_text}\n")