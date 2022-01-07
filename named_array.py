import numpy as np


class named_array(np.ndarray):

    def __init__(self, data, colnames=[], **kwargs):
        pass

    def __new__(cls, data, colnames=[], **kwargs):
        result = np.asarray(data, **kwargs).view(cls)
        result.colnames_range = {
            each[0] if isinstance(each, tuple) else each:
            each[1] if isinstance(each, tuple) else 1
            for each in colnames
        }
        result.colnames = [
            each[0] if isinstance(each, tuple) else each for each in colnames
        ]
        return result

    def set_colnames(self, colnames):
        self.colnames = colnames

    def __getitem__(self, ind):
        if isinstance(ind, str):
            if ind not in self.colnames:
                raise ValueError(f'no column has name {ind}')
            else:
                current_ind = self.colnames.index(ind)
                start = sum([
                    self.colnames_range[each]
                    for each in self.colnames[:current_ind]
                ])
                current_range = self.colnames_range[ind]
                if current_range == 1:
                    return self[:, start]
                else:
                    return self[:, start:start + current_range]
        elif (isinstance(ind, tuple) or isinstance(ind, list)) and all(isinstance(i, str) for i in ind):
            return np.column_stack(
                [self[:, self.colnames.index(i)] for i in ind])
        else:
            return np.ndarray.__getitem__(self, ind)
