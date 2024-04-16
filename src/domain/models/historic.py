from collections import namedtuple

Historic = namedtuple("Historic", "id, video_path, confidence, iou, created_at, box, number_fps, class_name")