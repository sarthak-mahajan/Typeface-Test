# %%
import numpy as np
import cv2
import matplotlib.pyplot as plt
import copy

# %%
def get_bb(img_file, verbose=False):
    img1 = cv2.imread(img_file)
    
    if verbose:
        print("Original Image")
        plt.imshow(img1)
        plt.show()
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    th, im_th = cv2.threshold(img1, 220, 255, cv2.THRESH_BINARY);
    
    im_floodfill = im_th.copy()
    
    h, w = im_th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    
    cv2.floodFill(im_floodfill, mask, (0,0), 255);
    
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    
    im_out = im_th | im_floodfill_inv

    if verbose:
        print("Flood fill Image")
        plt.imshow(im_out, cmap='gray')
        plt.show()

    img_copy = copy.deepcopy(im_out)
    rect, thresh = cv2.threshold(im_out, 254, 255, cv2.THRESH_OTSU)
    contours, hierar = cv2.findContours(thresh, 1, 2)

    threshes = []

    for idx, cnt in enumerate(contours):
        x,y,w,h = cv2.boundingRect(cnt)
        if w * h > 1:
            # Assuming that we select more than just a pixel, i.e., area > 1
            if verbose: 
                print(f"Countour {len(threshes)}: (x, y, w, h) - {x, y, w, h}")
            
            threshes.append(
                [x, y, w, h]
            )
            img_copy = cv2.rectangle(img_copy, (x, y), (x + w, y + h), (255, 255, 255), 2)

    if verbose:
        print("Final Bounding Box image")
        plt.imshow(img_copy, cmap='gray')
        plt.show()
    return threshes

# %%
get_bb('img1.png', verbose=False)

# %%
get_bb('img2.png', verbose=False)


