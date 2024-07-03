# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            if item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality = item.quality + 1

            elif item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = item.quality

            elif item.name.split(" ")[0] == "Backstage" and item.name.split(" ")[1] == "passes":
                if item.sell_in > 10 and item.quality < 50:
                    item.quality = item.quality + 1
                elif 10 >= item.sell_in > 5:
                    item.quality = item.quality + 2
                elif 5 >= item.sell_in > 0:
                    item.quality = item.quality + 3
                else:
                    item.quality = 0

            elif item.name.split(" ")[0] == "Conjured":
                item.quality = item.quality - 2

            else:
                if item.quality > 0:
                    if item.sell_in > 0:
                        item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - 2
                else:
                    item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
