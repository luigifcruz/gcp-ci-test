from main import *
import numpy as np

def test_potato():
  assert potato() == "kartof"

def test_sum():
  np.testing.assert_allclose(sum(), np.array([2, 4, 6]))
