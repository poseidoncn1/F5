import unittest
import ipywidgets as widget

class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = widget('the widget')

class DefaultWidgetTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.assertEqual(self.widget.size(),(50,50),'the incorrect size')

testcase = SimpleWidgetTestCase()
