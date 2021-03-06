import random as rn
import numpy as np

class Circle(object):
    ''''
       Circle Class

       A circle is defined by its radius, center coordinates,
       background color and alpha component.
    '''

    def __init__(self, *args):

        # Define parameters for circle generation

        if len(args) == 3 :

            #  Explicit definition with parameters: height , width , max_opacity

            self.height = args[0]
            self.width = args[1]
            self.maxopacity = args[2]

            self.center = (rn.randint(0, self.width), rn.randint(0, self.height))
            self.radius = rn.randint(1, 40) #max( self.width / 10 , self.height  / 10 ))
            self.color = (rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255))
            self.alpha = self.maxopacity * rn.random()

        elif len(args) == 4 :

            # Implicit definition by taking: height , width , max_opacity, decoding gene string

            self.height = args[0]
            self.width = args[1]
            self.maxopacity = args[2]

            info = args[3].split('-')
            self.center = (int(info[0]), int(info[1]))
            self.radius = int(info[2])
            self.color = (int(info[3]), int(info[4]), int(info[5]))
            self.alpha = float(info[6])


    def getInfo( self ):

        # Retrive information about the object

        return ( self.center, self.radius , self.color , self.alpha )

    def encodeGene( self ):

        # Returns a string encoding the gene information

        return ("{0}-{1}-{2}-{3}-{4}-{5}-{6}\n".format(self.center[0], self.center[1],
                                                       self.radius,self.color[0],
                                                       self.color[1], self.color[2],
                                                       self.alpha))
    def randomize( self ):

        # Produces  variations in gene parameters to a certain degree specified

        new_center_x = int ( self.center[0] + np.random.normal(0,10) )
        new_center_y = int ( self.center[1] + np.random.normal(0,10) )
        new_radius = int ( self.radius + np.random.normal(0,10) )

        new_color_r = int ( self.color[0] + np.random.normal(0, 20) )
        new_color_g = int ( self.color[1] + np.random.normal(0, 20) )
        new_color_b = int ( self.color[2] + np.random.normal(0, 20) )
        new_alpha = self.alpha + np.random.normal(0, 0.5)

        # Update randomized values
        self.center = ( max ( 0 , min ( self.width , new_center_x ) ) ,
                        max ( 0 , min ( self.height, new_center_y ) ) )

        self.radius = max ( 1 , min ( max( self.width/3 , self.height/3 ), new_radius ) )

        self.color = ( max ( 0 , min ( 255 , new_color_r ) ) ,
                       max ( 0 , min ( 255 , new_color_g) ) ,
                       max ( 0 , min ( 255 , new_color_b) ) )

        self.alpha = max ( 0.0 , min ( self.maxopacity , new_alpha ) )

