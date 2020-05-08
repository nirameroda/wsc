"""Running label propagation."""

from model import LabelPropagator
from param_parser import parameter_parser
from print_and_read import graph_reader, argument_printer,content_reader,value_kshell

def create_and_run_model(args):
    """
    Method to run the model.
    :param args: Arguments object.
    """
    graph = graph_reader(args.input)
    result = content_reader(args.content)
    kshell=value_kshell(args.kshell)
    model = LabelPropagator(graph,args)
    model.do_a_series_of_propagations()

if __name__ == "__main__":
    args = parameter_parser()
    argument_printer(args)
    create_and_run_model(args)

