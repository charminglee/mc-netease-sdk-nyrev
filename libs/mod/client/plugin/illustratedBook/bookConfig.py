
#-*- coding: UTF-8 -*- 

class BookConfig:

    class TextSize:
        infotext = 6
        footprint = 8
        content = 10
        smallTitle = 12
        middleTitle = 14
        title = 16

    class Colors:
        TextDefault = (0.1875, 0.01171875, 0.01171875, 1.0)
        BookTitle = (249.0/255.0, 221.0/255.0, 166.0/255.0, 1.0)
        SubTitle = (72.0/255.0, 30.0/255.0, 23.0/255.0, 1.0)

    class TextAlign:
        Left = 0
        Right = 1
        Center = 2
        Fit_Center = 3
        Fit_Left = 4
        Fit_Right = 5

    class ImageReszieRule:
        Ninesliced = 0
        Fit = 1

    # 这里记录的是一些预设用到的数据
    class Images:
        blank = "textures/ui/book_gui/blank" 
        categoryDefaultIcon = "textures/items/book_normal"
        lockBtn_dark = "textures/ui/book_gui/icon02" 
        sqrtPanel_light = "textures/ui/book_gui/panel04"   
        progressBar_light = "textures/ui/book_gui/progressbar01_01"
        progressBar_dark = "textures/ui/book_gui/progressbar01_bg"   
