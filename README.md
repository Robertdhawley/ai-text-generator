# AI Text Generator
A Python script that uses GPT-2 to generate text based on a user prompt.

## Features
- Generates text continuations using the GPT-2 model from Hugging Face.
- Interactive command-line interface for entering prompts.
- Enhanced text generation with tuned parameters for better coherence and creativity.

## Setup
1. Clone the repo.
2. Install the required libraries by running the following commands in the Replit shell:

pip install transformerspip install tensorflowpip install tf-keras

3. Run `python main.py` to start the script.

## Usage
- Enter a prompt (e.g., "Once upon a time, in a magical kingdom, there lived a brave princess who").
- The script will generate a continuation of up to 300 words.
- Type `exit` to quit.

## Example

Prompt: Once upon a time, in a magical kingdom, there lived a brave princess whoGenerated Text: Once upon a time, in a magical kingdom, there lived a brave princess who loved exploring the enchanted forests. Her name was Elara, and she carried a golden locket that glowed with fairy light. One sunny morning, a talking sparrow named Pip told her that the Moonflower, a magical bloom that kept the kingdom’s nights bright, had been stolen by a grumpy ogre. Elara set off with Pip, journeying through the Whispering Meadows where flowers giggled softly. They crossed a sparkling stream guarded by a playful water nymph, who asked them to sing a song for passage. Elara’s sweet voice charmed the nymph, and they continued to the ogre’s cave. Inside, Elara found the ogre, who was lonely and sad. With kindness, she befriended him, and he returned the Moonflower. Elara planted it back in the royal garden, and the kingdom glowed brighter than ever, thanks to her bravery and heart.


## Notes
- Requires an internet connection to download the GPT-2 model on first run.
- The model may take a few seconds to load.
- Text generation parameters (`temperature`, `top_k`, `top_p`, `no_repeat_ngram_size`) have been tuned to reduce repetition and improve output quality.
