<h1 style="font-size: 32px; font-weight: bold; color: black;">
  An Automated Deep Learning Algorithm for Polyp Segmentation in Colonoscopy
</h1>
The implementation and experimental setup are provided as supplementary materials to support the findings presented in our manuscript, "An Automated Deep Learning Algorithm for Polyp Segmentation in Colonoscopy".
<h1 style="font-size: 25px; font-weight: bold; color: black;">
Authors:
</h1>
Partho Deep Saha, Afia Adilah, Deponker Sarker Depto, Dr. Mahdy Rahman Chowdhury
<h1 style="font-size: 25px; font-weight: bold; color: black;">
Short Description:
</h1>
Colorectal cancer is one of the leading causes of cancer-related deaths worldwide, and early detection through colonoscopy is critical for improving survival rates. Our paper presents an innovative deep learning algorithm for the automated segmentation of polyps in colonoscopy images. By leveraging advanced neural network architectures, we aim to enhance the accuracy and efficiency of polyp detection, which is crucial for early diagnosis and treatment of colorectal cancer.
<br/><br/>
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/8bb475e3-6433-4b63-828a-251227f5e555" width="300"/><br/>
      <b>Original Image</b>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/17911e4e-a319-4b5f-96ab-7bd1c97a3254" width="300"/><br/>
      <b>Ground Truth</b>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/13121f44-18a2-427d-8d50-372419474342" width="300"/><br/>
      <b>Predicted Mask</b>
    </td>
  </tr>
</table>

<p align="center"><b>Figure 1:</b> Comparison of Original Image, Ground Truth, and Predicted Mask</p>

<h1 style="font-size: 25px; font-weight: bold; color: black;">
Requirements:
</h1>
<ul>
  <li><b>Python</b> = 3.8.10</li>
  <li><b>TensorFlow</b> = 2.8.0</li>
  <li><b>Keras</b> = 2.8.0</li>
</ul>  
<h1 style="font-size: 25px; font-weight: bold; color: black;">
Result:
</h1>
<h3 align="center">Table 1: Evaluation Metrics for EffPolypSegNet Model</h3>
<br></br>
<div align="center">
  <table style="width:90%; border-collapse: collapse; text-align: center;">
    <colgroup>
      <col style="width:25%;">
      <col style="width:25%;">
      <col style="width:25%;">
      <col style="width:25%;">
    </colgroup>
    <thead>
      <tr>
        <th style="border: 1px solid #ddd; padding: 8px;">Dataset</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Model</th>
        <th style="border: 1px solid #ddd; padding: 8px;">mIoU</th>
        <th style="border: 1px solid #ddd; padding: 8px;">DSC</th>
      </tr>
    </thead>
    <tbody>
      <tr><td style="border: 1px solid #ddd; padding: 8px;">BLI</td><td style="border: 1px solid #ddd; padding: 8px;">EffPolypSegNet</td><td style="border: 1px solid #ddd; padding: 8px;">0.8293</td><td style="border: 1px solid #ddd; padding: 8px;">0.9053</td></tr>
      <tr><td style="border: 1px solid #ddd; padding: 8px;">NBI</td><td style="border: 1px solid #ddd; padding: 8px;">EffPolypSegNet</td><td style="border: 1px solid #ddd; padding: 8px;">0.7828</td><td style="border: 1px solid #ddd; padding: 8px;">0.8436</td></tr>
      <tr><td style="border: 1px solid #ddd; padding: 8px;">FICE</td><td style="border: 1px solid #ddd; padding: 8px;">EffPolypSegNet</td><td style="border: 1px solid #ddd; padding: 8px;">0.9030</td><td style="border: 1px solid #ddd; padding: 8px;">0.9475</td></tr>
      <tr><td style="border: 1px solid #ddd; padding: 8px;">LCI</td><td style="border: 1px solid #ddd; padding: 8px;">EffPolypSegNet</td><td style="border: 1px solid #ddd; padding: 8px;">0.8965</td><td style="border: 1px solid #ddd; padding: 8px;">0.9446</td></tr>
      <tr><td style="border: 1px solid #ddd; padding: 8px;">WLI</td><td style="border: 1px solid #ddd; padding: 8px;">EffPolypSegNet</td><td style="border: 1px solid #ddd; padding: 8px;">0.8597</td><td style="border: 1px solid #ddd; padding: 8px;">0.9147</td></tr>
      <tr><td style="border: 1px solid #ddd; padding: 8px;">Kvasir-SEG</td><td style="border: 1px solid #ddd; padding: 8px;">EffPolypSegNet</td><td style="border: 1px solid #ddd; padding: 8px;">0.8672</td><td style="border: 1px solid #ddd; padding: 8px;">0.9199</td></tr>
      <tr><td style="border: 1px solid #ddd; padding: 8px;">CVC-ColonDB</td><td style="border: 1px solid #ddd; padding: 8px;">EffPolypSegNet</td><td style="border: 1px solid #ddd; padding: 8px;">0.8457</td><td style="border: 1px solid #ddd; padding: 8px;">0.9030</td></tr>
      <tr><td style="border: 1px solid #ddd; padding: 8px;">CVC-ClinicDB</td><td style="border: 1px solid #ddd; padding: 8px;">EffPolypSegNet</td><td style="border: 1px solid #ddd; padding: 8px;">0.9045</td><td style="border: 1px solid #ddd; padding: 8px;">0.9489</td></tr>
    </tbody>
  </table>
</div>
</table>
      




