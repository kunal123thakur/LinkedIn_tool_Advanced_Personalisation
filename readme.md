# LinkedIn Post Generator Tool

## Overview
This is an **Advanced RAG-based LinkedIn Post Generator** that learns the writing style of a targeted content creator and generates posts similar to their style. The tool preprocesses past posts, extracts metadata, and uses few-shot learning to maintain writing consistency. It also offers customization options for **topic, length, and language**.

## Features
- **Mimics writing style** of a targeted LinkedIn content creator.
- **Supports multiple topics** for post generation.
- **Offers different post lengths** (Short, Medium, Long).
- **Supports English and Hinglish** (a mix of Hindi and English in English script).
- **Streamlit-based UI** for ease of use.
- **Preprocessing and metadata extraction** for better tagging and categorization.

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
