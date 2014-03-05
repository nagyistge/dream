# ===========================================================================
# Copyright 2014 Nexedi SA
#
# This file is part of DREAM.
#
# DREAM is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DREAM is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with DREAM.  If not, see <http://www.gnu.org/licenses/>.
# ===========================================================================

from dream.simulation.RandomNumberGenerator import RandomNumberGenerator
from unittest import TestCase

from dream.simulation.Source import Source
obj = Source(id='dummy_obj', name="Dummy obj to instanciate RNG")

class RandomNumberGeneratorTestCase(TestCase):
    def testFixed(self):
        rng = RandomNumberGenerator(obj, distributionType='Fixed', mean=32)
        self.assertEquals(rng.generateNumber(), 32)
        self.assertEquals(rng.generateNumber(), 32)

    def testExp(self):
        rng = RandomNumberGenerator(obj, distributionType='Exp', avg=10)
        number = rng.generateNumber()
        # at least we make sure we generate a number
        self.assertTrue(number >= 0)

    def testErlang(self):
        rng = RandomNumberGenerator(obj,
            distributionType='Erlang', alpha=1, beta=2)
        number = rng.generateNumber()
        # at least we make sure we generate a number
        self.assertTrue(number >= 0)

    def testNormal(self):
        rng = RandomNumberGenerator(obj,
            distributionType='Normal',
            min=0,
            max=3,
            stdev=.5,
            avg=2)
        for i in range(10):
            number = rng.generateNumber()
            self.assertTrue(number >= 0)
            self.assertTrue(number <= 3)

    def testNormalWrongParameter(self):
        rng = RandomNumberGenerator(obj,
            distributionType='Normal',
            min=3,
            max=0, # here min > max
            stdev=.5,
            avg=2)
        self.assertRaises(ValueError, rng.generateNumber)

    def testUnkonwnDistribution(self):
        rng = RandomNumberGenerator(obj, distributionType='Unknown')
        self.assertRaises(ValueError, rng.generateNumber)

