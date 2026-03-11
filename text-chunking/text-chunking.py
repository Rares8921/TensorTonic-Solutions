import copy

def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    if not tokens:
        return []

    step = chunk_size - overlap
    res = []

    for i in range(0, len(tokens), step):
        chunk = tokens[i:i + chunk_size]
        if not chunk:
            break
        res.append(chunk)
        if i + chunk_size >= len(tokens):
            break

    return res