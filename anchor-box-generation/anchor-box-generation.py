import numpy as np

def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    stride = image_size / feature_size
    centers = (np.arange(feature_size) + 0.5) * stride
    cx, cy = np.meshgrid(centers, centers) # shape (feature_size, feature_size)

    cx = cx.flatten()[:, None, None] # shape (num_cells, 1, 1)
    cy = cy.flatten()[:, None, None] # shape (num_cells, 1, 1)

    scales = np.array(scales)[None, :, None] # shape (1, num_scales, 1)
    ratios = np.array(aspect_ratios)[None, None, :] # shape (1, 1, num_ratios)

    w = scales * np.sqrt(ratios) # shape (1, num_scales, num_ratios)
    h = scales / np.sqrt(ratios)

    anchors = np.stack([
        cx - w / 2, # x_min
        cy - h / 2, # y_min
        cx + w / 2, # x_max
        cy + h / 2  # y_max
    ], axis = -1) # shape (num_cells, num_scales, num_ratios, 4)

    return anchors.reshape(-1, 4).tolist()