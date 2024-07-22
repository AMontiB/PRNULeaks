# Shedding Light on some Leaks in PRNU-based Source Attribution

Forensic image source attribution aims at deciding whether a query
image was taken by a specific camera. While various algorithms
leveraging forensic traces have been proposed, the most effective
techniques rely on Photo Response Non-Uniformity (PRNU), a pattern introduced by camera sensors during the image acquisition
process. In recent years, advances in image acquisition and processing technologies in modern devices have been found to impact
the performance of PRNU, seemingly challenging its uniqueness.
In this paper, we build upon recent discoveries of leaks in PRNU
uniqueness, focusing on the dataset recently published by Iuliani
et al. which has been instrumental in identifying numerous issues
related to source attribution. Specifically, we analyze the effects in
terms of false positive of visible watermarks applied to Xiaomi Mi 9
images, and reveal artifacts in the magnitude of the Discrete Fourier
Transform of Samsung A50 images, indicative of the absence of
non-unique artifacts. Furthermore, we demonstrate how several
false positive cases are attributed to mislabeled devices. Finally, we
show that a number of false negatives from the dataset are traceable
to radially corrected images, and to images processed by third-party
software that had not been previously noticed.

This is the official code implementation of the paper ["Shedding Light on some Leaks in PRNU-based Source Attribution"](https://dl.acm.org/doi/pdf/10.1145/3658664.3659654)
Authors: Andrea Montibeller, Roy Alia Asiku, Fernando Pérez-González, Giulia Boato
Contact: andrea.montibeller@unitn.it

## Requirements

Refer to this github [repository](https://github.com/AMontiB/AdaptivePRNUCameraAttribution) for code requirements and to use the radial correction inversion method used in our paper.

## List of Samsung A50 images affected by spikes
[Here](https://github.com/AMontiB/PRNULeaks/blob/main/) we report the images IDs affected by spikes in DFT. You can use ``dimples.m" to estimate them.

![Spikes](https://github.com/AMontiB/PRNULeaks/blob/main/figures/Samsung_A50_spikes.png?raw=true)

## List of Post-Processed Images
[Here](https://github.com/AMontiB/PRNULeaks/blob/main/list_postprocessed_dev.csv) we report complete list of images post-processed out-camera. Use "Software_outcamera_images.py" and modify line 35.


![Table](https://github.com/AMontiB/PRNULeaks/blob/main/figures/STPR_vs_NDR.png?raw=true)

