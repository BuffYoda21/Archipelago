from collections import Counter

from test.general import setup_multiworld
from . import GlyphsTestBase
from .. import GlyphsWorld, get_broken_button_ids

class TestGlyphsItems(GlyphsTestBase):
    auto_construct = False

    def test_button_to_shard_pairs_individual(self):
        self.sub_test_button_to_shard_pairs(1, 1)

    def test_button_to_shard_pairs_bundles(self):
        self.sub_test_button_to_shard_pairs(2, 5)

    def sub_test_button_to_shard_pairs(self, min_size, max_size):
        multiworld = setup_multiworld(
            GlyphsWorld,
            steps=("generate_early", "create_regions", "create_items"),
            seed=1234,
            options={
                "ButtonSanity": True,
                "ButtonShardPercent": 100,
                "ShardBundleMinSize": min_size,
                "ShardBundleMaxSize": max_size,
            },
        )
        world = multiworld.worlds[1]

        represented_shards = []
        for item in multiworld.itempool:
            if item.name.startswith("Button Shard "):
                represented_shards.append(int(item.name.rsplit(" ", 1)[1]))
            elif item.name.startswith("Shard Bundle "):
                bundle_number = int(item.name.rsplit(" ", 1)[1])
                represented_shards.extend(world.shard_bundles[bundle_number - 1].shards)

        assert Counter(represented_shards) == Counter(get_broken_button_ids(world))