# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:

            if item.name == "Aged Brie":
                item.quality += 1

            elif item.name.startswith("Backstage passes"):
                if item.sell_in > 10:
                    item.quality += 1
                elif 10 >= item.sell_in > 5:
                    item.quality += 2
                elif 5 >= item.sell_in > 0:
                    item.quality += 3
                else:
                    item.quality = 0

            else:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    if item.quality > 0:
                        if item.sell_in > 0:
                            if item.name.startswith("Conjured"):
                                item.quality -= 2
                            else:
                                item.quality -= 1
                        else:
                            if item.name.startswith("Conjured"):
                                item.quality -= 4
                            else:
                                item.quality -= 2
                    else:
                        item.quality = 0

            if item.quality > 50 and item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = 50

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
