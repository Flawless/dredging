from unittest import TestCase

from dredging import productivity


class TestProductivity(TestCase):
    def test_productivity(self):
        self.assertAlmostEqual(
            productivity(.296092, 1007.68, 0.6887, 1760, .3),
            .00143, places=5)
        self.assertAlmostEqual(
            productivity(.296092, 1011.27, 0.1734, 1760, .3, 1000, 0.9, 1.1),
            .00053, places=5)
        self.assertAlmostEqual(
            productivity(crosssectional_area=.496, mean_density=1111.27,
                         mean_speed=1.34, material_density=1760,
                         material_porosity=.3, water_density=1014,
                         coeff1=0.9, coeff2=1.1, time_delta=2.5),
            .02402, places=5)
        self.assertAlmostEqual(
            productivity(.296092, 1230.68, 2.6887, 1760, .3, time_delta=10.3),
            .01626, places=5)

        with self.assertRaises(ZeroDivisionError):
            productivity(.296092, 1230.68, 2.6887, 1760, .3, time_delta=0)

        with self.assertRaises(ZeroDivisionError):
            productivity(.296092, 1760, 2.6887, 1000, .3)
