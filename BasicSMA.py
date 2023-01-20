# Basic Simple Moving Average indicator for pyqtrader.
# This app does not have caching functionality.  No caching results in simpler code,
# but may lead to reduced performance

PQitemtype='CurveIndicator'

PERIOD=20

def PQcomputef(PQitem):
    result=[]
    closes=PQitem.series.closes

    for i,val in enumerate(closes):
        if i>=PERIOD-1:
            s=sum(closes[i-PERIOD+1:i+1])/PERIOD
            result.append(s)
    
    return result
