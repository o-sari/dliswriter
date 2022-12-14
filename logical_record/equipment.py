from .utils.core import EFLR


class Equipment(EFLR):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.logical_record_type = 'STATIC'
        self.set_type = 'EQUIPMENT'

        self.trademark_name = None
        self.status = None
        self._type = None
        self.serial_number = None
        self.location = None
        self.height = None
        self.length = None
        self.minimum_diameter = None
        self.maximum_diameter = None
        self.volume = None
        self.weight = None
        self.hole_size = None
        self.pressure = None
        self.temperature = None
        self.vertical_depth = None
        self.radial_drift = None
        self.angular_drift = None

        self.create_attributes()