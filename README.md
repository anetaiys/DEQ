# DEQ 
## Diffusion Equation Quantification
	DEQ is an image processing tool to quantify 0-1 in the image according to diffusion equation.

## - - - - - - - - - - - - - - - - - - - - - - - -

### Overview
### """""""""
	This calculation code provides:

	(1) DEQ calculation for input .csv image file (2D array)
		and output .csv images according to iterations as a list

	(2) Filter functions (DEQ_Filter_Function) are defined
		However, in the DEQ filter function, users can artbitrary 
		define a filter according to their puropose  

	If a researcher use this code, please refer to
		
		Diffusion equation quantification: selective enhancement algorithm
		for bone metastasis lesions in CT images
		(doi: xxxxxxxxx)
	
	and include the reference.

	This calculation code is licensed under Apache License 2.0 


### Requirement
### """"""""""""
	numpy
 	csv
  	math
	tkinter
 	numpy

### Install
### """"""""""""
	No install method.

### Usage
### """""""""
	Import DEQ and vreate instance of DEQ class.
	Then start DiffusionEquationQuantificationModule(img1, img2, dx, dy).
	Input two same shape (rows and columns) .csv image files (img1, img2).
 	Calculation grid size dx and dy are usually 1.0.

### License
### """""""""
	Apache License 2.0 

### Author
### """""""""
	Yusuke Anetai

 
  	
## - - - - - - - - - - - - - - - - - - - - - - - -
