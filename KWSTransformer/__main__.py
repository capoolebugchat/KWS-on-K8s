import argparse
from kserve import ModelServer, model_server, model
from kws_transformer import Transformer
# from .transformer_model_repository import TransformerModelRepository


parser = argparse.ArgumentParser(parents=[model_server.parser])

parser.add_argument(
    "--predictor_host", help="The URL for the model predict function", required=True
)
parser.add_argument(
    "--model_name", help="The name that the model is served under."
)
# currently support v1 predictors only
# parser.add_argument(
#     "--protocol", help="The protocol for the predictor", default="v1"
# )

args, _ = parser.parse_known_args()

if __name__ == "__main__":
    model = Transformer(args.model_name, predictor_host=args.predictor_host, protocol="v1")
    ModelServer(workers=1).start([model])