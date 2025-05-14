# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    """
    Class created to perform unit testing.
    """

    def test_default_item_quality_decreases(self) -> None:
        """
        Test case created to check for default modification.
        """
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 19)
        self.assertEqual(items[0].sell_in, 9)

    def test_aged_brie_increases_quality(self) -> None:
        """
        Test case return to test item modification for item Aged Brie.
        """
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, 1)

    def test_backstage_pass_increases_quality(self) -> None:
        """
        Test case return to test item modification for item Backstage passes.
        """
        items = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20
            )
        ]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[0].sell_in, 14)

    def test_backstage_pass_quality_drops_to_zero_after_concert(self) -> None:
        """
        Test case return to test item modification for item Backstage passes.
        """
        items = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20
            )
        ]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -1)

    def test_sulfuras_does_not_change(self) -> None:
        """
        Test case return to test item modification for item Sulfuras.
        """
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)

    def test_sulfuras_negative_sell_in_does_not_change(self) -> None:
        """
        Test case return to test item modification for item Sulfuras.
        """
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_mana_cake(self) -> None:
        """
        Test case return to test item modification for item Conjured.
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 5)
        self.assertEqual(items[0].sell_in, 2)

    def test_default_item_quality_degrades_twice_as_fast_after_sell_in(self) -> None:
        """
        Test case return to test item modification for item Elixir.
        """
        items = [Item(name="Elixir of the Mongoose", sell_in=0, quality=7)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 6)
        self.assertEqual(items[0].sell_in, -1)


if __name__ == "__main__":
    unittest.main()
