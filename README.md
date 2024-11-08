# Image Compression using SVD

## Introduction to SVD
Singular Value Decomposition (SVD) is a powerful mathematical tool used in various applications like dimensionality reduction, image compression, and collaborative filtering in recommendation systems. Understanding SVD can provide deep insights into the structure of data and the underlying patterns.

## How SVD Works
Singular Value Decomposition (SVD) is a fundamental method in linear algebra that provides insights into the structure of data matrices. Given a matrix \(A\), SVD decomposes it into three matrices:

\[
A = U \Sigma V^T
\]

- **U (Left Singular Vectors):** An orthogonal matrix where the columns are the left singular vectors of \(A\).
- **\(\Sigma\) (Diagonal Matrix):** A diagonal matrix with non-negative singular values arranged in descending order.
- **V (Right Singular Vectors Transposed):** The transpose of an orthogonal matrix where the rows are the right singular vectors of \(A\).

## Problem Statement
Imagine you are part of a team responsible for enhancing the quality of images in a large digital museum. The museum’s digital collection contains thousands of images of artworks, many of which are old and of low resolution. Your task is to implement SVD and use it for image compression and enhancement, making these digital artworks look more appealing while preserving their details.

## Solution Overview
The input image matrix is split into three matrices: \(U\), \(\Sigma\), and \(V\). The images are then compressed by retaining only the top \(k\) singular values and vectors, where \(k\) is significantly smaller than the original dimensions. In the solution notebook, the value of \(k\) is chosen such that the most significant \(k\) values account for over 90% of the total sum of values in the diagonal matrix.

## Result
Increasing the value of \(k\) makes the image clearer but reduces the compression effect. Conversely, decreasing \(k\) increases compression but at the cost of image quality. The Streamlit application allows users to verify these results using a slider that adjusts the value of \(k\) and shows the resultant image.

## Running the Application
To run the application on your local device, use the following command:

```bash
streamlit run app.py
