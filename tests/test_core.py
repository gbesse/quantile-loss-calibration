import unittest,math
from quantile_loss_calibration.core import run
class DomainTests(unittest.TestCase):
 def test_loss(self):
  x=run({'quantiles':[.1,.9],'cases':[dict(id='a',actual=10,predictions=[8,12])]});self.assertAlmostEqual(x['quantiles'][0]['mean_pinball_loss'],.2);self.assertAlmostEqual(x['quantiles'][1]['mean_pinball_loss'],.2)
 def test_crossings(self):self.assertEqual(run({'quantiles':[.1,.9],'cases':[dict(id='a',actual=10,predictions=[12,8])]})['crossing_cases'][0]['id'],'a')
 def test_median_absolute_half(self):self.assertEqual(run({'quantiles':[.5],'cases':[dict(id='a',actual=10,predictions=[8])]})['quantiles'][0]['mean_pinball_loss'],1)
