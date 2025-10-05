import logging
from typing import Union
from datasets import DatasetDict, IterableDatasetDict

logger = logging.getLogger('dsiter')

def calculate_num_rows(d: Union[DatasetDict, IterableDatasetDict]):
    result = 0
    
    if isinstance(d, IterableDatasetDict):
        result = sum(1 for _ in d)
    
    if isinstance(d, DatasetDict):
        result = len(d)

    return result