# LinkedIn Post Generator Tool - An ultimate working Mate


https://github.com/user-attachments/assets/65c2108c-ebab-4767-a654-7b9b68f7a477


## Overview
This is an **Advanced RAG-based LinkedIn Post Generator tool that inherits your style of creating** that learns the writing style of a targeted content creator and generates posts similar to their style which saves them a lot of time . The tool preprocesses past posts, extracts metadata, and uses few-shot learning to maintain writing consistency. It also offers customization options for **topic, length, and language**.

## Features
- **Mimics writing style** of a targeted LinkedIn content creator.
- **Supports multiple topics** for post generation.
- **Offers different post lengths** (Short, Medium, Long).
- **Supports English and Hinglish** (a mix of Hindi and English in English script).
- **Streamlit-based UI** for ease of use.
- **Preprocessing and metadata extraction** for better tagging and categorization.

## I want to credit my friend Navneet for these content of his on top of which i have personalised my LinkedIn tool 
## These are some of his work from where I took my contents
sources:
![Screenshot 2025-03-28 201849](https://github.com/user-attachments/assets/e47b60e6-8719-46fb-a639-61afe243b4b2)
**write style**
![Screenshot 2025-03-28 201921](https://github.com/user-attachments/assets/07f0e38e-efe3-4442-bc5c-d6e336094890)


## Project Structure
```
C:.
│   backup.txt
│   cleaner.py          # Cleans text and removes unnecessary elements
│   few_shot.py         # Implements few-shot learning for maintaining writing style
│   LLm_model.py        # LLM wrapper for text generation
│   main.py             # Streamlit app for generating LinkedIn posts
│   post_generator.py   # Generates posts based on selected options
│   preprocessing.py    # Processes raw LinkedIn posts and extracts metadata
│   test.py             # Testing script
│
├───content
│       Screenshot 2025-03-28 193156.png
│       Screenshot 2025-03-28 201513.png
│
├───data
│       processed_posts.json   # Processed posts with metadata
│       raw_posts.json         # Original raw LinkedIn posts
│
└───__pycache__
```

## Installation & Setup
### 1. Clone the Repository
```sh
 git clone https://github.com/your-repo/LinkedIn_post_Generator_tool.git
 cd LinkedIn_post_Generator_tool
```

### 2. Set Up Virtual Environment (Optional but Recommended)
```sh
 python -m venv env
 source env/bin/activate   # For Mac/Linux
 env\Scripts\activate      # For Windows
```

### 3. Install Dependencies
```sh
 pip install -r requirements.txt
```

### 4. Run the Streamlit App
```sh
 streamlit run main.py
```
![Screenshot 2025-03-28 201513](https://github.com/user-attachments/assets/739f202b-99a5-411e-8bff-ba83da23f8f3)


## How It Works
### 1. **Preprocessing & Metadata Extraction**
- Raw LinkedIn posts are **cleaned** and **analyzed** to extract metadata such as language, line count, and relevant tags.
- Tags are unified to create a **better structured dataset** for similarity-based retrieval.

### 2. **Few-Shot Learning & Post Generation**
- When generating a post, the model retrieves **similar past posts** based on topic, length, and language.
- The retrieved posts are **provided as context** to the LLM for generating a post **in the same style**.
- The output always ends with a **personalized signature line** to maintain authenticity.

## Example Usage
### Generating a Post
```python
from post_generator import generate_post

post = generate_post("Medium", "English", "Career Growth")
print(post)
```

### Expected Output
```
Building a career is not about chasing job titles, it's about gaining skills that make you valuable.

Many professionals get stuck in their comfort zone, unwilling to take risks or learn new things.

The ones who grow are the ones who challenge themselves constantly!

---------
Signing off
Navneet - The letters ✉️ guy
```
