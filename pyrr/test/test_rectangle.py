import unittest
import math

import numpy

from pyrr import rectangle


class test_matrix44( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_zero( self ):
        rect = rectangle.zero()

        self.assertEqual(
            rect[ (0,0) ],
            0,
            "Rectangle is not zero'ed"
            )
        self.assertEqual(
            rect[ (0,1) ],
            0,
            "Rectangle is not zero'ed"
            )
        self.assertEqual(
            rect[ (1,0) ],
            0,
            "Rectangle is not zero'ed"
            )
        self.assertEqual(
            rect[ (1,1) ],
            0,
            "Rectangle is not zero'ed"
            )

    def test_create_from_bounds( self ):
        left = 1.0
        right = 10.0
        bottom = -2.0
        top = 5.5

        rect = rectangle.create_from_bounds(
            left,
            right,
            bottom,
            top
            )
        
        self.assertEqual(
            rect[ (0,0) ],
            left,
            "Rectangle bounds incorrectly calculated"
            )
        self.assertEqual(
            rect[ (0,1) ],
            bottom,
            "Rectangle bounds incorrectly calculated"
            )
        self.assertEqual(
            rect[ (1,0) ],
            right - left,
            "Rectangle bounds incorrectly calculated"
            )
        self.assertEqual(
            rect[ (1,1) ],
            top - bottom,
            "Rectangle bounds incorrectly calculated"
            )

    def test_bounds( self ):
        left = 0.0
        right = 5.0
        bottom = 0.0
        top = 5.0

        rect = numpy.array(
            [
                [ left, bottom ],
                [ right - left, top - bottom ],
                ]
            )

        left2, right2, bottom2, top2 = rectangle.bounds( rect )

        self.assertEqual(
            left,
            left2,
            "Bounds not calculated correctly"
            )
        self.assertEqual(
            right,
            right2,
            "Bounds not calculated correctly"
            )
        self.assertEqual(
            bottom,
            bottom2,
            "Bounds not calculated correctly"
            )
        self.assertEqual(
            top,
            top2,
            "Bounds not calculated correctly"
            )

        left = 0.0
        right = 5.0
        bottom = 0.0
        top = 5.0

        # make rectangle inverse size
        rect = numpy.array(
            [
                [ right, top ],
                [ left - right, bottom - top ],
                ]
            )

        left2, right2, bottom2, top2 = rectangle.bounds( rect )

        self.assertEqual(
            left,
            left2,
            "Bounds not calculated correctly"
            )
        self.assertEqual(
            right,
            right2,
            "Bounds not calculated correctly"
            )
        self.assertEqual(
            bottom,
            bottom2,
            "Bounds not calculated correctly"
            )
        self.assertEqual(
            top,
            top2,
            "Bounds not calculated correctly"
            )

    def test_is_point_within_rect( self ):
        rect = numpy.array(
            [
                [0.0, 0.0],
                [5.0, 5.0]
                ]
            )

        self.assertTrue(
            rectangle.is_point_within_rect(
                [ 0.0, 0.0 ],
                rect
                )
            )
        self.assertTrue(
            rectangle.is_point_within_rect(
                [ 5.0, 5.0 ],
                rect
                )
            )
        self.assertTrue(
            rectangle.is_point_within_rect(
                [ 1.0, 1.0 ],
                rect
                )
            )
        self.assertFalse(
            rectangle.is_point_within_rect(
                [-1.0, 1.0 ],
                rect
                )
            )
        self.assertFalse(
            rectangle.is_point_within_rect(
                [ 1.0,10.0 ],
                rect
                )
            )
        self.assertFalse(
            rectangle.is_point_within_rect(
                [ 1.0,-1.0 ],
                rect
                )
            )

    def test_is_relative_point_within_rect( self ):
        rect = numpy.array(
            [
                [0.0, 0.0],
                [5.0, 5.0]
                ]
            )

        self.assertTrue(
            rectangle.is_relative_point_within_rect(
                [ 0.0, 0.0 ],
                rect
                )
            )
        self.assertTrue(
            rectangle.is_relative_point_within_rect(
                [ 5.0, 5.0 ],
                rect
                )
            )
        self.assertFalse(
            rectangle.is_relative_point_within_rect(
                [-1.0, 0.0 ],
                rect
                )
            )
        self.assertFalse(
            rectangle.is_relative_point_within_rect(
                [10.0, 0.0 ],
                rect
                )
            )

    def test_make_point_relative( self ):
        rect = numpy.array(
            [
                [ 5.0, 5.0],
                [10.0,10.0]
                ]
            )

        point = [5.0, 5.0]
        result = rectangle.make_point_relative(
            point,
            rect
            )

        self.assertEqual(
            point[ 0 ] - rect[ (0,0) ],
            result[ 0 ],
            "Failed to make point realtive to rectangle"
            )
        self.assertEqual(
            point[ 1 ] - rect[ (0,1) ],
            result[ 1 ],
            "Failed to make point realtive to rectangle"
            )

    def test_make_point_absolute( self ):
        rect = numpy.array(
            [
                [ 5.0, 5.0],
                [10.0,10.0]
                ]
            )

        point = [5.0, 5.0]
        result = rectangle.make_point_absolute(
            point,
            rect
            )

        self.assertEqual(
            point[ 0 ] + rect[ (0,0) ],
            result[ 0 ],
            "Failed to make point realtive to rectangle"
            )
        self.assertEqual(
            point[ 1 ] + rect[ (0,1) ],
            result[ 1 ],
            "Failed to make point realtive to rectangle"
            )

    def test_scale_by_vector( self ):
        rect = numpy.array(
            [
                [ 5.0, 5.0],
                [10.0,10.0]
                ]
            )

        scale = [ 2.0, 3.0 ]

        result = rectangle.scale_by_vector(
            rect,
            scale
            )

        self.assertEqual(
            rect[ (0,0) ] * scale[ 0 ],
            result[ (0,0) ],
            "Failed to scale rectangle"
            )
        self.assertEqual(
            rect[ (0,1) ] * scale[ 1 ],
            result[ (0,1) ],
            "Failed to scale rectangle"
            )
        self.assertEqual(
            rect[ (1,0) ] * scale[ 0 ],
            result[ (1,0) ],
            "Failed to scale rectangle"
            )
        self.assertEqual(
            rect[ (1,1) ] * scale[ 1 ],
            result[ (1,1) ],
            "Failed to scale rectangle"
            )

            
    
if __name__ == '__main__':
    unittest.main()

