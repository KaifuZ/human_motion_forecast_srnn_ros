from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import numpy as np
import copy
import theano
from datetime import datetime
import data_utils
from neuralmodels.loadcheckpoint import loadDRA
import viz

class Predictor:
    def __init__(self, checkpoint):
        data_utils.load_crf_graph(sys.path[0] + '/crf')
        print('loading checkpoint...')
        self._model = loadDRA(checkpoint)
        print('loaded!')

    def _predict_sequence(self, forecast, forecast_node_feature, length):
        teX = copy.deepcopy(forecast)
        nodeNames = teX.keys()

        teY = {}
        to_return = {}
        T = 0
        nodeFeatures_t_1 = {}
        for nm in nodeNames:
            [T,N,D] = teX[nm].shape
            to_return[nm] = np.zeros((T+length,N,D),dtype=theano.config.floatX)
            to_return[nm][:T,:,:] = teX[nm]
            teY[nm] = []
            nodeName = nm.split(':')[0]
            nodeFeatures_t_1[nodeName] = forecast_node_feature[nm][-1:,:,:]

        for i in range(length):
            nodeFeatures = {}
            for nm in nodeNames:
                nt = nm.split(':')[1]
                nodeName = nm.split(':')[0]
                prediction = self._model.predict_node[nt](to_return[nm][:(T+i),:,:],1e-5)
                nodeFeatures[nodeName] = prediction[-1:,:,:]
                teY[nm].append(nodeFeatures[nodeName][0,:,:])
            for nm in nodeNames:
                nt = nm.split(':')[1]
                nodeName = nm.split(':')[0]
                nodeRNNFeatures = data_utils.get_node_feature(nodeName, nodeFeatures)
                to_return[nm][T+i,:,:] = nodeRNNFeatures[0,:,:]
            nodeFeatures_t_1 = copy.deepcopy(nodeFeatures)
        for nm in nodeNames:
            teY[nm] = np.array(teY[nm])
        del teX
        return teY
    
    def predict(self, groud_truth_sequence, length):
        begin = datetime.now()
        features, data_mean, data_std, dimensions_to_ignore, new_idx = data_utils.skeleto_to_feature(groud_truth_sequence)
        forecast, forecast_node_feature = data_utils.get_predict_data(features)
        predicted_features = self._predict_sequence(forecast, forecast_node_feature, length)
        print('make a prediction take: ', datetime.now() - begin)
        return data_utils.feature_to_skeleto(predicted_features, data_mean, data_std, dimensions_to_ignore, new_idx)
