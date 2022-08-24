# grumpy_mw_forward_model

The jupyter notebooks in this repository contain the code to reproduce figures from [Manwadkar & Kravtsov 2022](https://arxiv.org/abs/2112.04511). The entire code is split into two notebooks. Part 1 includes the code to forward modeling the satellite population for comparison with observed samples in the DES, PS1 etc. Part 2 includes code for the rest of the figures in the paper. The data to reproduce all these figures is available at the Mendeley Data [here](https://data.mendeley.com/datasets/zmwh6wxyv3/1). Follow the below steps to reproduce the paper figures using the above jupyter notebooks.  


1. Download the data file <tt>MK22_data_files.tar.gz</tt> from [here](https://data.mendeley.com/datasets/zmwh6wxyv3/1). Place the <tt>MK22_data_files.tar.gz</tt> file into directory of your choice and unpack the file: 

``
gzip -d MK22_data_files.tar.gz

tar xvf MK22_data_files.tar
``
 

2. Assign the path of this data folder to the variable ```data_path``` in the first cell of both jupyter notebooks. Look at the notebooks for examples and further clarification. 

3. 

4. Run the notebooks cell-by-cell to produce the plots from the paper. 
