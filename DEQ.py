# # # # # # # # # # # # # # # # # # # # # # # # #
"""

	Diffusion Equation Quantification (DEQ)

	This calculation cord provides:

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

	(c) Yusuke Anetai

"""
# # # # # # # # # # # # # # # # # # # # # # # # #

import sys;
import os;
import csv;
import math;
import numpy as np;
import tkinter as tk;
import tkinter.ttk as ttk;
import tkinter.filedialog as tkF;

##########################
class DEQcalc():
	def __init__(self):
		#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+
		INNER_LOOP = 10; #implicit calculation
		TK = 5; # Loop number for the iteration
		DC = 0.1 # Diffusion control parameter
		FUNCTION_TYPE = 0; # Filter function allocation
		FUNCTION_ORDER = 4; # Filter function order
		#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+
		self.deqparam = [INNER_LOOP,TK,DC,FUNCTION_TYPE,FUNCTION_ORDER];


	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
	#1. CSV image reader and writer
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

	def csvpathread(self):
		roottk = tk.Tk();
		fType = [("","*.csv")];
		iDir = os.path.abspath(os.path.dirname(__file__));
		filepath = tkF.askopenfilename(parent = roottk,filetypes = fType,initialdir = iDir);
		roottk.withdraw();
		roottk.destroy();
		print(filepath);
		return(filepath);

	def csvreadTXT(self,filepath):
		data0 = list();
		ftxt = np.genfromtxt(filepath,delimiter=',');
		#data0.append(np.array(ftxt,dtype='float64').transpose());
		data0.append(np.array(ftxt,dtype='float64'));
		return np.array(data0);

	def csvWriter2L(self,Data,filename):
		cdpath = os.getcwd();
		print(cdpath);
		## Directory:: _csvtmp
		newdir = '_csvtmp';
		if(os.path.exists(newdir)):
			print('path exists');
		else:
			os.mkdir(newdir);
		newpath = '%s/%s' % (cdpath,newdir);
		os.chdir(newpath);
		## Directory:: _DEQ
		newdirL = '_DEQ';
		if(os.path.exists(newdirL)):
			print('path exists');
		else:
			os.mkdir(newdirL);
		newpathL = '%s/%s/%s' % (cdpath,newdir,newdirL);
		os.chdir(newpathL);
		if(len(filename)==0):
			filename = 'mccArray.csv';
		filenameR = ('%s/%s')%(newpathL,filename);
		fid = open(filenameR,'w');
		#writer = csv.writer(fid,lineterminator = '\r\n');
		writer = csv.writer(fid,lineterminator = '\r');
		#writer.writerow(Data[:]);
		writer.writerows(np.array(Data[:],dtype='float64'));
		os.chdir(cdpath);
		fid.close();

	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
	#2. Define filter function
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
	def DEQ_Filter_Function(self,fpp,mode,order):
		## ## ## ## ## ## ## ## ## ## ## ##
		N = order;
		dc = self.deqparam[2];
		DD = np.zeros(fpp.shape);
		## ## ## ## ## ## ## ## ## ## ## ##

		if(mode == 0):
			#mode 0: superelipse positive exponential-like 
			DD = (1-np.power((1-np.power(fpp,N)),1/N))*dc;
		elif(mode == 1):
			#mode 1: superelipse negative exponential-like 
			DD = np.power((1-np.power(fpp,N)),1/N)*dc;
		elif(mode == 2):
			#mode 2: positive sigmoid-like 
			DD = (1-np.power((1-np.power(fpp,N)),N))*dc;
		elif(mode == 3):
			#mode 3: negative sigmoid-like 
			DD = np.power((1-np.power(fpp,N)),N)*dc;
		else:
			#mode default: superelipse exponential-like 
			DD = (1-np.power((1-np.power(fpp,N)),1/N))*ADJ;

		return(DD);

	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
	#3. Diffusion Equation Quantification
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

	def DiffusionEquationQuantificationModule(self,img,dx,dy):
		## initial condition ##
		q1 = self.deqparam[0]; q2 = self.deqparam[1]; q3 = self.deqparam[2]; 
		q4 = self.deqparam[3]; q5 = self.deqparam[4];
		NORM_IMGtoIMG = True;
		print("parameter:\n inner_loop: %d \n iteration: %d \n dc value: %.4f" % (q1,q2,q3));
		calcANSlist = list();
		LOOP = q1; tn = q2; dt = 1.0;
		## ## ## ## ## ## ## ##
		prepp = np.zeros(img.shape);
		pp = np.zeros(img.shape);
		phi = np.zeros(img.shape);
		ny = img.shape[0]; nx = img.shape[1];
		##
		phi = (img-np.min(img))/(np.max(img)-np.min(img));
		print("phi: size >>> ",phi.shape);
		print("phi: range >>> ", "min_val %.2f - max_val %.2f"%(np.min(phi),np.max(phi)));
		calcANSlist.append(phi);
		DD = [];
		DD = self.DEQ_Filter_Function(phi,q4,q5);	
		print("\n >>> DEQ calculation START \n");
		for kk in range(tn):
			prepp = phi if(kk == 0) else pp;		
			## Crank-Nicolson method (implicit calculator)
			for ss in range(LOOP):
				for jj in range(nx):
					for ii in range(ny):
						if(ii != 0 and jj !=0 and ii != ny-1 and jj != nx-1):
							c0 = 1+DD[ii,jj]/(dx*dx)+DD[ii,jj]/(dy*dy);
							c1 = 1-DD[ii,jj]/(dx*dx)-DD[ii,jj]/(dy*dy);
							cd = (DD[ii,jj]/2);
							cy = (pp[ii+1,jj]+pp[ii-1,jj]+prepp[ii+1,jj]+prepp[ii-1,jj])/(dy*dy);
							cx = (pp[ii,jj+1]+pp[ii,jj-1]+prepp[ii,jj+1]+prepp[ii,jj-1])/(dx*dx);
							pp[ii,jj] = (c1*prepp[ii,jj]+cd*(cx+cy))/c0;
							#print(kk,ii,jj,pp[ii,jj],prepp[ii,jj],c0,cd,cx,cy);
				pp = self.image_normalize_zeroone(pp) if(NORM_IMGtoIMG) else pp;
				prepp = pp;
			pp = self.image_normalize_zeroone(pp) if(NORM_IMGtoIMG) else pp;
			calcANSlist.append(pp);
			print((">>> iteration %d is calculated")%(kk+1));
		return (calcANSlist);

	def image_normalize_zeroone(self,img):
		newimg = (img-np.min(img))/(np.max(img)-np.min(img));
		return(newimg);

