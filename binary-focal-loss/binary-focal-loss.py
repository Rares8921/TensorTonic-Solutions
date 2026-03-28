def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    pt = [predictions[i] if targets[i] == 1 
          else 1 - predictions[i] 
          for i in range(len(targets))]

    from math import log
    FL = [-alpha * (1 - pT)**gamma * log(pT) for pT in pt]
    
    return sum(FL) / len(FL)