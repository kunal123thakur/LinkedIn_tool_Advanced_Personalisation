from LLm_model import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "10 to 40 lines"
    if length == "Long":
        return "40 to 100 lines"


def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    Always include ---------\nSigning off\nNavneet - The letters ✉️ guy in the last line
    '''
    # prompt = prompt.format(post_topic=tag, post_length=length_str, post_language=language)

    examples = few_shot.get_filtered_posts(length, language, tag)  # ye wahi function hai jo few_shot me hai aur last me jo [] ek aisa problem aa rha tha na jo solve kiye the baad me wo wahi tha ki tag,size ,languague ke basis pr similarity search kr ke bht sara post de rha hai aur fir use context me result dega humlogo ka model 
# ye hai examples file [{'text': "Just saw a LinkedIn Influencer with 'Organic Growth' written in the profile with 65K+ followers claiming that he can help you in growing your platform, copying the posts from other influencers.", 'engagement': 90, 'line_count': 2, 'language': 'Hinglish', 'tags': ['Influencer', 'Organic Growth'], 'length': 'Short'}, {'text': "Next time when I'll be reading some LinkedIn Influencer's story, I am starting from the last line.\nIf there's a link attached to it, it's most probably a fake one.\nSaves me time!", 'engagement': 188, 'line_count': 3, 'language': 'Hinglish', 'tags': ['Influencer', 'LinkedIn'], 'length': 'Short'}]
    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: # Use max two samples
            break

    return prompt


if __name__ == "__main__":
    print(generate_post("Medium", "English", "Mental Health"))