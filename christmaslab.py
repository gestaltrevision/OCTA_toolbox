# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:28:23 2020

@author: u0090621
"""


# image as shape

random.seed(3)

stimulus = Grid(4,6, background_color = "white", x_margin = 0, y_margin = 0, row_spacing = 150, col_spacing = 150)
stimulus.positions = Positions.CreateSineGrid(n_rows = 5, n_cols = 6, row_spacing = 120, col_spacing = 100, A = 25, f = .1, axis = "xy")

stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([Image, Image, Image, Image, Image, Image, 
                                                Image, Image, Image, Image, Image, Image,
                                                Image, Image, Image, Image, Image, Image,
                                                Image, Image, Image, Image, Image, Image
                                                ])
stimulus.data = GridPattern.RepeatAcrossElements(["C:/Users/u0090621/Downloads/lab/Anne-Sofie_Maerten_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Charlotte_Boeykens_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Christophe_Bossens_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Christopher_Linden_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Cisem_Ozkul_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Claudia_Damiano_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Birte_Geusens_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Daniel_Hoffman_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Agna_Marien_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Eline_Van_Geert_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Emmelien_Mooyaert_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Joke_Dierckx_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Liesse_Frerart_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Tina_Ivancir_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Elisabeth_Van_der_Hulst_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Jaana_Van_Overwalle_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Johan_Wagemans_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Laurie-Anne_Sapey-Triomphe_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Miguel_Granja_Espirito_Santo_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Naomi_Couder_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Nathalie_Vissers_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Nofar_Ben_Itzhak_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Sander_Van_de_Cruys_HAT.png",
                                                  "C:/Users/u0090621/Downloads/lab/Thiago_Leiros_Costa_HAT.png"
                                                  ])
                                                        
stimulus.orientations = GridPattern.RepeatAcrossElements([0])
orientationjitter = Pattern(stimulus.orientations).AddNormalJitter(mu = 0, std = 20)
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(60,100)]) 

stimulus.orientations = GridPattern.RepeatAcrossElements(orientationjitter)


stimulus.positions.SetLocationJitter(distribution = "normal", mu = 0, std = 8)
                                                             
stimulus.Show()