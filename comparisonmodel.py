pip install segment-geospatial groundingdino-py leafmap localtileserver

import os
import leafmap
import samgeo
import torch
from samgeo import SamGeo, raster_to_vector, overlay_images
from samgeo import tms_to_geotiff
from samgeo.text_sam import LangSAM
import cv2
input_image1 = "/content/drive/MyDrive/geodam main project/data set/test dataset building change/A/test_80.png"
input_image2 = "/content/drive/MyDrive/geodam main project/data set/test dataset building change/B/test_80.png"
sam_kwargs = {
    "points_per_side": 32,
    "pred_iou_thresh": 0.86,
    "stability_score_thresh": 0.92,
    "crop_n_layers": 1,
    "crop_n_points_downscale_factor": 2,
    "min_mask_region_area": 80,
}
sam = SamGeo(
    model_type="vit_h",
    sam_kwargs=sam_kwargs,
)
sam.generate(input_image1, output="mask1.tif", foreground=True)
                              # Load the segmentation mask
segmentation_mask = cv2.imread('mask{i}.tif', cv2.IMREAD_GRAYSCALE)

                              # Find contours in the segmentation mask
contours, _ = cv2.findContours(segmentation_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                               # Get the number of objects (contours)
num_objects = len(contours)
#print("Number of objects detected:", num_objects)
sam.show_masks(cmap="binary_r", box_color='red',
    title='Automatic Segmentation of Trees',
    blend=True,)
