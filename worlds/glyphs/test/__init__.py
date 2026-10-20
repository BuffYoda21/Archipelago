from test.bases import WorldTestBase
from .. import GlyphsWorld

class GlyphsTestBase(WorldTestBase):
    game = "GLYPHS"
    world: GlyphsWorld
    player: int = 1