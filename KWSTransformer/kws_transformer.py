# Transformer class and light server initialization for simple TF model
# This files includes: Transformer class def: preprocessing, postprocessing
# along with: Transformer server initialization

import kserve
import logging
import time
from kserve import Model, model_server, ModelServer
import numpy as np
from typing import Dict, List
from scipy import signal
import argparse

def audio_transform(instance: List) -> np.array:
    """converts the audio data of Python List into padded numpy array
    Args:
        instance: The request input instance for one audio.
    Returns:
        List: Returns the data in a 2D numpy array (list of ONE audio data)
    """
    streaming_sr = 16000
    desired_length = int(round(float(len(instance)) / streaming_sr * 16000))
    instance = signal.resample(instance, desired_length)

    # convert from int16 to float 32
    instance = np.array(instance, np.float32) / 32768.0
    instance = np.pad(instance, (0, streaming_sr-len(instance)), 'constant')
    
    return instance


class Transformer(Model):

     
    def __init__(
        self, 
        name: str,
        predictor_host: str,
        protocol: str
    ):
        super().__init__(name)
        self.predictor_host = predictor_host
        self.explainer_host = predictor_host
        self.protocol = protocol
        self.ready = True

        logging.info("MODEL NAME %s", name)
        logging.info("PREDICTOR URL %s", self.predictor_host)
        logging.info("EXPLAINER URL %s", self.explainer_host)
        self.timeout = 100

    async def preprocess(self, input_request: Dict)-> Dict:
        """ Input follows the Tensorflow V1 HTTP API for binary values
        https://www.tensorflow.org/tfx/serving/api_rest#encoding_binary_values """
        
        start = time.time()
        input_tensors = [audio_transform(instance) for instance in input_request["instances"]]
        inputs = [input_tensor.tolist() for input_tensor in input_tensors]
        request = {"instances": inputs}
        end = time.time()
        logging.info(f"Transformer preprocessed request. Time: {end-start}")

        return request
    
    def postprocess(self, infer_response: Dict)->Dict:
        
        return infer_response