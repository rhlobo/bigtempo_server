import numpy
import pandas
from datetime import datetime as dt


from . import engine


@engine.datasource('SAMPLE')
class SampleDatasource(object):

    def evaluate(self, context, symbol, start=None, end=None):
        if start is None:
            start = dt(2000, 1, 1)

        if end is None:
            end = dt(2005, 1, 1)

        rng = pandas.date_range(start, end)
        data = numpy.random.randn(len(rng))
        return pandas.DataFrame(data, index=rng, columns=[symbol])
