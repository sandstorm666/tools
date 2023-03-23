import os
 
class BatchRename():
 
    def __init__(self):
        self.path = 'training/library_train/'

    def rename(self):
        filelist = os.listdir(self.path)
        filelist.sort()
        fo=open('training/library_train/frames.txt','w')
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item.endswith('.png'):#要识别的文件格式尾缀
                src = os.path.join(os.path.abspath(self.path), item)
                s = str(i)
                s = s.zfill(6)
                dst = os.path.join(os.path.abspath(self.path), s + '.jpg')
                fo.write(s + '.jpg'+'\n')
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print ('total %d to rename & converted %d pngs' % (total_num, i))
 
 
if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
