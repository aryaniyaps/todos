from base64 import b64encode
from typing import Sequence, Optional


def paginate(
    dataset: Sequence, 
    first: Optional[int] = None, 
    last: Optional[int] = None, 
    after: Optional[str] = None, 
    before: Optional[str] = None
) -> Sequence:
    """
    Paginates the given dataset.

    :param dataset: The dataset to paginate.

    :param first: The number of items to slice
        from the dataset in the forward direction.

    :param last: The number of items to slice
        from the dataset in the backward direction.

    :param after: The cursor after which the 
        dataset must be sliced.

    :param before: The cursor before which the 
        dataset must be sliced.

    :return: The paginated dataset.
    """
    pass