class Solution(object):
    def imageSmoother(self, img):
        img0=[[0 for i in range(len(img[0]))] for j in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[0])):
                floor=0
                c=0
                for i0 in range(max(i-1,0),min(i+2,len(img))):
                    for j0 in range(max(j-1,0),min(j+2,len(img[0]))):
                        floor+=img[i0][j0]
                        c+=1
                img0[i][j]=floor//c
        return img0