def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    x1_a, y1_a, x2_a, y2_a = box_a
    x1_b, y1_b, x2_b, y2_b = box_b
    
    area_a = max(0, x2_a - x1_a) * max(0, y2_a - y1_a) 
    area_b = max(0, x2_b - x1_b) * max(0, y2_b - y1_b)

    x1_i, y1_i, x2_i, y2_i = max(x1_a, x1_b), max(y1_a, y1_b), min(x2_a, x2_b), min(y2_a, y2_b) 
    intersection = max(0, x2_i - x1_i) * max(0, y2_i - y1_i)
    
    union = area_a + area_b - intersection

    if union == 0.0:
        return 0.0

    return intersection / union