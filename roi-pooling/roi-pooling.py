import math

def roi_pool(feature_map, rois, output_size):
    """
    Apply ROI Pooling to extract fixed-size features.
    """
    pooled_outputs = []

    for x1, y1, x2, y2 in rois:
        roi_height = y2 - y1
        roi_width = x2 - x1

        pooled_roi = []

        for i in range(output_size):
            row = []

            h_start = y1 + math.floor(i * roi_height / output_size)
            h_end = y1 + math.floor((i + 1) * roi_height / output_size)

            if h_end == h_start:
                h_end = h_start + 1

            for j in range(output_size):
                w_start = x1 + math.floor(j * roi_width / output_size)
                w_end = x1 + math.floor((j + 1) * roi_width / output_size)

                if w_end == w_start:
                    w_end = w_start + 1

                max_value = float("-inf")

                for r in range(h_start, h_end):
                    for c in range(w_start, w_end):
                        max_value = max(max_value, feature_map[r][c])

                row.append(max_value)

            pooled_roi.append(row)

        pooled_outputs.append(pooled_roi)

    return pooled_outputs