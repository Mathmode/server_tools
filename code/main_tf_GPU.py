#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 00:12:17 2024

@author: Ángel Javier Omella
"""
import sys
import argparse
import tensorflow as tf
#from your_module import your_main

# Execute in one GPU limiting its memory
# tensorflow version >=2.15.0

#FOR GOLIAT SERVER:
# nGPU = 0 --> 40LS (GPU 2 in nvidia-smi)
# nGPU = 1 --> 40LS (GPU 3 in nvidia-smi)
# nGPU = 2 --> 40LS (GPU 4 in nvidia-smi)
# nGPU = 3 --> GV100 (GPU 0 in nvidia-smi)
# nGPU = 4 --> GV100 (GPU 1 in nvidia-smi)


def run_code_in_GPU(GPU_number, memory_limit):
    gpus = tf.config.list_physical_devices('GPU')
    #print('list_physical_devices:', gpus)
   
    if gpus:
        # Restrict TensorFlow to only allocate memory_limit of memory on the GPU_number GPU
        try:
            tf.config.set_logical_device_configuration(gpus[GPU_number],[tf.config.LogicalDeviceConfiguration(memory_limit=memory_limit)])
            tf.config.set_visible_devices(gpus[GPU_number], 'GPU')
            logical_gpus = tf.config.list_logical_devices('GPU')
            #
            print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
            print('list_physical_devices:', gpus)
            print('list_logical_devices:', logical_gpus)

        except RuntimeError as e:
            # Visible devices must be set before GPUs have been initialized
            print(e)         
    return



def main_GPU(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=int, default=0, help='The integer of the GPU selected to run the program')
    parser.add_argument("--vram", type=int, default=8192, help='The integer to limit the GPU VRAM in MB')
    args = parser.parse_args(args)
    
    ###################
    # #To run in GPU, call the function to configure the GPU usage
    run_code_in_GPU(args.gpu, args.vram)
    
    # # and execute your code
    #your_main()



if __name__ == "__main__":
    main_GPU()
