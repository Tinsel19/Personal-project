
import os

path = "//storage//emulated//0"

image_dir = [path]
image_dir1 = [path]
for root, dirs, files in os.walk(path):
    for dir in dirs:
        x = os.path.join(root, dir)
        y = dir
        for v in os.listdir(x):
            if v.endswith(".png") or v.endswith(".jpg"):
                if x in image_dir:
                    pass
                else:
                    image_dir.append(x)
                    image_dir1.append(y)


print(len(image_dir1))
print(image_dir)