from __future__ import division
import re, sys
from PIL import Image

def draw_regex_rec(pixels, regex, pixel_id, xmin, xmax, ymin, ymax):
    if xmin == xmax:
        match = regex.search(pixel_id)
        if match:
            group_len = sum(len(group) for group in match.groups())
            color = int(255 * group_len / len(pixel_id))
            pixels[xmin, ymin] = (color, 0, 0)
    else:
        xmid = (xmin + xmax) // 2
        ymid = (ymin + ymax) // 2
        draw_regex_rec(pixels, regex, pixel_id + "1", xmid + 1, xmax, ymin, ymid)
        draw_regex_rec(pixels, regex, pixel_id + "2", xmin, xmid, ymin, ymid)
        draw_regex_rec(pixels, regex, pixel_id + "3", xmin, xmid, ymid + 1, ymax)
        draw_regex_rec(pixels, regex, pixel_id + "4", xmid + 1, xmax, ymid + 1, ymax)

def draw_regex(size, regex):
    img = Image.new("RGB", (size, size), "black")
    draw_regex_rec(img.load(), regex, "", 0, size - 1, 0, size - 1)
    img.save('image.png')

if __name__ == "__main__":
    size = int(sys.stdin.readline())
    regex = re.compile(sys.stdin.readline().strip())
    draw_regex(size, regex)
