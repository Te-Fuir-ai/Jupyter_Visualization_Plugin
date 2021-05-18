
from datavalidator.handlers.statistics_handler import StatisticsHandler
from datavalidator.handlers.convert_handler import ConvertHandler


def data_visualize(dataframes):
    proto = StatisticsHandler().ProtoFromDataFrames(dataframes)
    ConvertHandler().data_convert(proto)
