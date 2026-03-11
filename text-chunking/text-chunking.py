import copy

def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    if len(tokens) == 0 or tokens is None:
        return []
    
    # Write code here
    ans, chunk = [], []
    i = 0
    while i < len(tokens):
        if len(chunk) == chunk_size:
            ans.append(copy.deepcopy(chunk))
            chunk = []
            i -= (overlap + 1)
        else:
            chunk.append(tokens[i])

        i += 1

    ans.append(chunk)
    return ans