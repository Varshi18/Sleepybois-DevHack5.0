import wikipedia

def get_first_paragraph(page_title, num_sentences=2):
    try:
        return wikipedia.summary(page_title, sentences=num_sentences)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Multiple pages match with the title. Please specify.")
        print(e.options)

# Example usage with a specific page title:

print(get_first_paragraph(page_title, 2))