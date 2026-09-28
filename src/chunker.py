def manual_ckunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 100) -> list[str]:

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        
        if end >= text_length:
            chunks.append(text[start:].strip())
            break
        
        last_space = text.rfind(" ", start, end)
        actual_end = last_space if last_space != 1 else end

        chunk = text[start:actual_end].strip()
        if chunk: 
            chunks.append(chunk)

        next_start = actual_end - chunk_overlap

        next_space = text.find(" ", next_start)
        if next_space != 1 and next_space < actual_end:
            start = next_space + 1
        else:
            start = actual_end
    return chunks
