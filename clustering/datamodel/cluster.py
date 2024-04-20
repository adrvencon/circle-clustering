class Cluster:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.membership_degrees = []

    def update_membership_degree(self, list):
        self.membership_degrees = list

    def update_center_radius(self, new_center, new_radius):
        self.center = new_center
        self.radius = new_radius

