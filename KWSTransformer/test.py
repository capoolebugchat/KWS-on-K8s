from kws_transformer import Transformer
from kserve import Model

def transformer_init_test(test_transformer: Transformer):
    
    assert str(test_transformer.__class__.__bases__) == "(<class 'kserve.model.Model'>,)", \
            f"wrong base class !{str(test_transformer.__class__.__bases__)}"

def transformer_preprocessing_test(test_transformer, test_data):

    import numpy as np
    test_data = np.array([1,2,3,4,5,6,7])
    print(test)

test_transformer = Transformer("test", "Blank", "gRPC")


transformer_init_test(test_transformer)