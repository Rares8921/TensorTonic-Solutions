def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    srt = sorted(values)
    mp = {}
    N = len(srt)
    i = 0
    while i < N:
        j = i
        while j < N and srt[i] == srt[j]:
            j += 1
        j -= 1
        
        mp[srt[i]] = (i + j + 2) / 2

        i = j + 1
    
    return [mp[value] for value in values]