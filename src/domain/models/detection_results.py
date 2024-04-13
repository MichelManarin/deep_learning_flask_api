from collections import namedtuple

DetectionResult = namedtuple("DetectionResults", "id, user_input_id, box, number_fps, class_name, confidence")