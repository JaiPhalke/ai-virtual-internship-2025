from transformers import pipeline

# Load the model only once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def split_text(text, max_chunk_length=1024):
    """
    Splits the input text into smaller chunks to fit model input limits.
    """
    import textwrap
    return textwrap.wrap(text, max_chunk_length)

def summarize_text(text):
    """
    Summarizes the input text in chunks and combines into a final note.
    """
    chunks = split_text(text)
    summary_parts = []

    for chunk in chunks:
        part = summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
        summary_parts.append(part)

    final_summary = ' '.join(summary_parts)

    # Optional: If you want an even shorter summary of all parts combined
    if len(summary_parts) > 1:
        # Re-summarize the combined parts (like summarizing a summary)
        final_summary = summarizer(final_summary, max_length=100, min_length=40, do_sample=False)[0]['summary_text']

    return final_summary
