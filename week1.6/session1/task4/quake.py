# Week 1.6, Session 1: Task 4

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Quake:
    """
    Details of a single earthquake.
    """

    when: datetime
    longitude: float
    latitude: float
    depth: float
    magnitude: float



now = datetime.now()
q = Quake(now, 139.9, 28.0, 473.0, 7.0)
print(q)