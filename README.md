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
		(doi: 10.1088/1361-6560/ad965c)
	
	and include the reference.

	This calculation code is licensed under Apache License 2.0 


### Requirement
### """"""""""""
	numpy
 	csv
  	math
	tkinter

### Install
### """"""""""""
	No install method.

### Usage
### """""""""
	Import DEQ and create instance of DEQcalc class in your code.
	Then start DiffusionEquationQuantificationModule(img, dx, dy).
	Input one .csv image file.
 	Usually, calculation grid size dx and dy are 1.0.

### License
### """""""""
	Apache License 2.0 

### Author
### """""""""
	Yusuke Anetai 
 	anetaiys (atmark) hirakata.kmu.ac.jp

 
  	
## - - - - - - - - - - - - - - - - - - - - - - - -
