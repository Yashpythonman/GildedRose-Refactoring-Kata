# -*- coding: utf-8 -*-
import abc


class Item:
    """
    Class created to represent items state and behaviour
    """

    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return f"{self.name}, {self.sell_in}, {self.quality}"


class ItemModifier:
    def __init__(self, item: Item) -> None:
        self.item = item

    @abc.abstractmethod
    def update(self) -> None:
        """
        Abstract method created to update the item.
        """
        pass

    def inc_quality(self, count: int = 1) -> None:
        """
        Function created to increase item quality by 1.
        """
        if self.item.quality < 50:
            self.item.quality += count

    def dec_quality(self, count: int = 1) -> None:
        """
        Function created to decrease item quality by 1.
        """
        if self.item.quality > 0:
            self.item.quality -= count

    def inc_sell_in(self, count: int = 1) -> None:
        """
        Function created to increase item sell in by 1.
        """
        self.item.sell_in += count

    def dec_sell_in(self, count: int = 1):
        """
        Function created to decrease item sell in by 1.
        """
        self.item.sell_in -= count


class DefaultItemModifier(ItemModifier):
    def update(self):
        """
        Implemented method from parent class
        """
        self.dec_sell_in()
        if self.item.quality > 0:
            self.dec_quality()


class AgedBrieModifier(ItemModifier):
    def update(self) -> None:
        """
        Implemented method from parent class
        """
        self.dec_sell_in()


class BackstagePassModifier(ItemModifier):

    def update_quality(self) -> None:
        """
        Utility function to update quality and sell in.
        """
        if self.item.sell_in <= 0:
            self.item.quality = 0
        elif self.item.sell_in <= 5:
            self.inc_quality(3)
        elif self.item.sell_in <= 10:
            self.inc_quality(2)
        else:
            self.inc_quality()

    def update(self) -> None:
        """
        Method created to update item quantity and sell in.
        """
        self.update_quality()
        self.dec_sell_in()


class SulfurasModifier(ItemModifier):
    def update(self):
        """
        Method created to update item quantity and sell in.
        """
        if self.item.sell_in < 0:
            self.item.quality = 0


class ItemTypeModifierFactory:
    """
    The factory class created to provide the instance for item type updator.
    """

    def __init__(self, item: Item) -> None:
        self.item = item

    def factory(self):
        """
        Function created to provide the instance of item type modifier.
        """
        if self.item.name == "Aged Brie":
            return AgedBrieModifier(self.item)
        elif self.item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassModifier(self.item)
        elif self.item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasModifier(self.item)
        else:
            return DefaultItemModifier(self.item)


class GildedRose:
    """
    Class provided to refactor the logic
    """

    def __init__(self, items: list) -> None:
        self.items = items

    def update_quality(self) -> None:
        """
        Function created to update the quality and sell in of the items.
        """
        for item in self.items:
            modifier = ItemTypeModifierFactory(item).factory()
            modifier.update()
