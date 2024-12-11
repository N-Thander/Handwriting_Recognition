import numpy as np

def decode_prediction(prediction):
    alphabets = u"ABCDEFGHIJKLMNOPQRSTUVWXYZ-' "
    decoded = []
    for seq in prediction[0]:
        max_index = np.argmax(seq)
        if max_index == len(alphabets):
            break
        decoded.append(alphabets[max_index])
    return "".join(decoded)
