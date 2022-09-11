import os


IMG_EXTENSIONS = ['.h5']
def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

# filename = './data/nyudepthv2/test/00001.h5'
# print(is_image_file(filename))


def make_dataset(dir, class_to_idx):
    images = []
    dir = os.path.expanduser(dir)
    for target in sorted(os.listdir(dir)):
        d = os.path.join(dir, target)
        if not os.path.isdir(d):
            continue
        for root, _, fnames in sorted(os.walk(d)):
            for fname in sorted(fnames):
                if is_image_file(fname):
                    path = os.path.join(root, fname)
                    item = (path, class_to_idx[target])
                    images.append(item)
    return images

# print(os.path.expanduser(dir))

dir = './data/nyudepthv2/val/'
def find_classes(dir):
    classes = [d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]
    classes.sort()
    class_to_idx = {classes[i]: i for i in range(len(classes))}
    return classes, class_to_idx

classes, class_to_idx = find_classes(dir)
print("find_classes........", classes, class_to_idx)
dir = './data/nyudepthv2/val'
print(make_dataset(dir, class_to_idx))


def num_classes(dir):
    """
    os.path.isdir() 判断是否为目录
    os.path.isfile() 判断是否为文件
    os.path.dirname() 返回上一级目录
    """
    classes =  []
    for d in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, d)):
            classes.append(d)
    class_to_index = {}
    for i in range(len(classes)):
        class_to_index[classes[i]] = i
    return classes, class_to_index

classes, class_to_idx = num_classes(dir)
# print("num_classes..........", classes, class_to_idx)



