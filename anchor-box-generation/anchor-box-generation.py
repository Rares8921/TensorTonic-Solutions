from math import sqrt

def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here
    stride = image_size / feature_size
    anchors = []
    for i in range(feature_size):
        for j in range(feature_size):
            cx, cy = (j + 0.5) * stride, (i + 0.5) * stride
            
            for s in scales:
                for r in aspect_ratios:
                    w = s * sqrt(r)
                    h = s / sqrt(r)

                    anchor = [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]
                    anchors.append(anchor)

    return anchors