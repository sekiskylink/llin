# -*- coding: utf-8 -*-

"""URL definitions of the application. Regex based URLs are mapped to their
class handlers.
"""

from app.controllers.main_handler import Index, Logout
from app.controllers.warehouse_handler import WarehouseData
from app.controllers.api import Location, LocationChildren, DistributionPoints, SubcountyLocations
from app.controllers.reporters_handler import Reporters
from app.controllers.users_handler import Users
from app.controllers.groups_handler import Groups
from app.controllers.distributionpoints_handler import DistPoints

URLS = (
    r'^/', Index,
    r'/warehousedata', WarehouseData,
    # "/dispatch", "Dispatch",
    "/distributionpoints", DistPoints,
    r'/api/v1/loc_children/(\d+)/?', LocationChildren,
    r'/api/v1/location/(\d+)/?', Location,
    r'/api/v1/distribution_points/(\d+)/?', DistributionPoints,
    r'/api/v1/subcountylocations/(\d+)/?', SubcountyLocations,
    r'/reporters', Reporters,
    # "/search", "Search",
    r'/users', Users,
    r'/groups', Groups,
    "/logout", Logout,
)
