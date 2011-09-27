from neo.core.baseneo import BaseNeo

import numpy as np
import quantities as pq

class EventArray(BaseNeo):
    """
    Array of events. Introduced for performance reasons.
    An :class:`EventArray` is prefered to a list of :class:`Event` objects.
    
    *Usage*:
        TODO
    
    *Required attributes/properties*:
        :times: (quantity array 1D)
        :labels: (numpy.array 1D dtype='S')
    
    *Recommended attributes/properties*:
        :name:
        :description:
        :file_origin:            
    
    """
    def __init__(self, times=np.array([])*pq.s, labels=np.array([], dtype='S'), **kwargs):
        BaseNeo.__init__(self, **kwargs)
        self.times = times
        self.labels = labels

    def __repr__(self):
        return "<EventArray: %s>" % ", ".join('%s@%s' % item for item in zip(self.labels, self.times))
